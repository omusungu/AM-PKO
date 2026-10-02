from __future__ import annotations

import json
import math
import os
from pathlib import Path

from embedding.evaluation_interface import EvaluationRun


ROOT = Path(__file__).resolve().parent

EXPERIMENT_ID = "EXP-4B6-001"
CORPUS_VERSION = "0.1"
QUERY_VERSION = "0.1"
JUDGMENT_VERSION = "0.1"
TOP_K = 5
QUERY_COUNT = 50
JUDGMENT_ASSIGNMENTS = 102

MODELS = {
    "M-000001": "BGE-M3",
    "M-000002": "E5",
    "M-000003": "Qwen",
}

JUDGMENT_SCALE = {
    "0": "not relevant",
    "1": "partially relevant",
    "2": "highly relevant",
}


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dcg(grades: list[int], k: int) -> float:
    return sum(
        (2 ** grade - 1) / math.log2(rank + 1)
        for rank, grade in enumerate(grades[:k], start=1)
    )


def validate_judgments(judgments: list[dict]) -> dict[str, dict[str, int]]:
    if len(judgments) != QUERY_COUNT:
        raise ValueError(
            f"Expected {QUERY_COUNT} judgment entries, got {len(judgments)}"
        )

    by_query: dict[str, dict[str, int]] = {}
    assignment_count = 0

    for entry in judgments:
        query_id = entry.get("query_id")
        relevance = entry.get("relevance")

        if not isinstance(query_id, str):
            raise ValueError("Judgment query_id must be a string")

        if query_id in by_query:
            raise ValueError(f"Duplicate judgment query_id: {query_id}")

        if not isinstance(relevance, dict):
            raise ValueError(f"{query_id}: relevance must be an object")

        normalized: dict[str, int] = {}

        for record_id, grade in relevance.items():
            if not isinstance(record_id, str):
                raise ValueError(f"{query_id}: record_id must be a string")

            if grade not in (1, 2):
                raise ValueError(
                    f"{query_id}/{record_id}: expected grade 1 or 2, got {grade!r}"
                )

            normalized[record_id] = int(grade)
            assignment_count += 1

        by_query[query_id] = normalized

    if assignment_count != JUDGMENT_ASSIGNMENTS:
        raise ValueError(
            f"Expected {JUDGMENT_ASSIGNMENTS} relevance assignments, "
            f"got {assignment_count}"
        )

    return by_query


def validate_retrieval(
    retrieval: dict,
    model_id: str,
) -> list[dict]:
    if retrieval.get("experiment_id") != EXPERIMENT_ID:
        raise ValueError(
            f"{model_id}: retrieval artifact has wrong experiment_id"
        )

    if retrieval.get("model_id") != model_id:
        raise ValueError(
            f"{model_id}: retrieval artifact has wrong model_id"
        )

    if retrieval.get("similarity") != "cosine":
        raise ValueError(
            f"{model_id}: expected cosine similarity"
        )

    if retrieval.get("retrieval_k") != TOP_K:
        raise ValueError(
            f"{model_id}: expected retrieval_k={TOP_K}"
        )

    results = retrieval.get("results")

    if not isinstance(results, list):
        raise ValueError(f"{model_id}: results must be a list")

    if len(results) != QUERY_COUNT:
        raise ValueError(
            f"{model_id}: expected {QUERY_COUNT} retrieval results, "
            f"got {len(results)}"
        )

    query_ids: set[str] = set()

    for result in results:
        query_id = result.get("query_id")
        ranked = result.get("top_k")

        if query_id in query_ids:
            raise ValueError(
                f"{model_id}: duplicate query_id {query_id}"
            )

        query_ids.add(query_id)

        if not isinstance(ranked, list) or len(ranked) != TOP_K:
            raise ValueError(
                f"{model_id}/{query_id}: expected exactly {TOP_K} ranked results"
            )

        record_ids: set[str] = set()
        previous_score = float("inf")

        for rank in ranked:
            record_id = rank.get("record_id")
            score = rank.get("score")

            if not isinstance(record_id, str):
                raise ValueError(
                    f"{model_id}/{query_id}: record_id must be a string"
                )

            if record_id in record_ids:
                raise ValueError(
                    f"{model_id}/{query_id}: duplicate record_id {record_id}"
                )

            record_ids.add(record_id)

            if not isinstance(score, (int, float)) or not math.isfinite(score):
                raise ValueError(
                    f"{model_id}/{query_id}/{record_id}: score must be finite"
                )

            if not -1.0 <= float(score) <= 1.0:
                raise ValueError(
                    f"{model_id}/{query_id}/{record_id}: "
                    f"cosine score outside [-1, 1]"
                )

            if float(score) > previous_score:
                raise ValueError(
                    f"{model_id}/{query_id}: scores are not non-increasing"
                )

            previous_score = float(score)

    return results


def evaluate_query(
    relevance: dict[str, int],
    ranked: list[dict],
) -> dict[str, float]:
    grades = [
        relevance.get(result["record_id"], 0)
        for result in ranked
    ]

    relevant_total = sum(
        grade >= 1
        for grade in relevance.values()
    )

    high_relevance_total = sum(
        grade == 2
        for grade in relevance.values()
    )

    if relevant_total == 0:
        raise ValueError("A query must have at least one relevant judgment")

    if high_relevance_total == 0:
        raise ValueError(
            "A query must have at least one highly relevant judgment"
        )

    metrics: dict[str, float] = {}

    for k in (1, 3, 5):
        top = grades[:k]

        metrics[f"Recall@{k}"] = (
            sum(grade >= 1 for grade in top) / relevant_total
        )

        metrics[f"HighRelevanceRecall@{k}"] = (
            sum(grade == 2 for grade in top)
            / high_relevance_total
        )

        ideal_grades = sorted(
            relevance.values(),
            reverse=True,
        )

        ideal_dcg = dcg(ideal_grades, k)

        metrics[f"nDCG@{k}"] = (
            dcg(top, k) / ideal_dcg
            if ideal_dcg
            else 0.0
        )

    metrics["MRR"] = next(
        (
            1.0 / rank
            for rank, grade in enumerate(grades, start=1)
            if grade >= 1
        ),
        0.0,
    )

    return metrics


def aggregate_metrics(
    per_query: list[dict],
) -> dict[str, float]:
    metric_names = (
        "Recall@1",
        "Recall@3",
        "Recall@5",
        "HighRelevanceRecall@1",
        "HighRelevanceRecall@3",
        "HighRelevanceRecall@5",
        "nDCG@1",
        "nDCG@3",
        "nDCG@5",
        "MRR",
    )

    return {
        name: sum(
            result["metrics"][name]
            for result in per_query
        ) / len(per_query)
        for name in metric_names
    }


def run_model(
    model_id: str,
    judgments: dict[str, dict[str, int]],
) -> None:
    retrieval = load_json(
        ROOT / f"{model_id}_retrieval.json"
    )

    results = validate_retrieval(
        retrieval,
        model_id,
    )

    per_query = []

    for result in results:
        query_id = result["query_id"]

        if query_id not in judgments:
            raise ValueError(
                f"{model_id}: no frozen judgment exists for {query_id}"
            )

        metrics = evaluate_query(
            judgments[query_id],
            result["top_k"],
        )

        per_query.append(
            {
                "query_id": query_id,
                "metrics": metrics,
            }
        )

    if len(per_query) != QUERY_COUNT:
        raise ValueError(
            f"{model_id}: expected {QUERY_COUNT} per-query results"
        )

    aggregate = aggregate_metrics(per_query)

    evaluation = EvaluationRun(
        evaluation_id=f"{EXPERIMENT_ID}:{model_id}",
        experiment_id=EXPERIMENT_ID,
        model_id=model_id,
        model_family=MODELS[model_id],
        judgment_scale=JUDGMENT_SCALE,
        per_query=per_query,
        metrics=aggregate,
    )

    output = {
        "evaluation_id": evaluation.evaluation_id,
        "experiment_id": evaluation.experiment_id,
        "model_id": evaluation.model_id,
        "model_family": evaluation.model_family,
        "judgment_scale": dict(evaluation.judgment_scale),
        "per_query": list(evaluation.per_query),
        "metrics": dict(evaluation.metrics),
    }

    output_path = ROOT / f"{model_id}_evaluation.json"

    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(output, handle, indent=2)

    print(
        f"{model_id}: evaluated {len(per_query)}/{QUERY_COUNT} queries"
    )

    for name, value in aggregate.items():
        print(f"  {name}: {value:.9f}")

    print(f"RESULT: PASS — {output_path}")


def main() -> None:
    corpus = load_json(ROOT / "corpus.json")
    queries = load_json(ROOT / "queries.json")
    judgments_raw = load_json(ROOT / "judgments.json")
    models = load_json(ROOT / "models.json")

    if corpus["experiment_id"] != EXPERIMENT_ID:
        raise ValueError("Wrong corpus experiment_id")

    if corpus["status"] != "FROZEN":
        raise ValueError("Corpus must be FROZEN")

    if corpus["corpus_version"] != CORPUS_VERSION:
        raise ValueError("Unexpected corpus version")

    if len(corpus["records"]) != QUERY_COUNT:
        raise ValueError(
            f"Expected {QUERY_COUNT} frozen corpus records"
        )

    if queries["experiment_id"] != EXPERIMENT_ID:
        raise ValueError("Wrong query experiment_id")

    if queries["status"] != "FROZEN":
        raise ValueError("Queries must be FROZEN")

    if queries["query_version"] != QUERY_VERSION:
        raise ValueError("Unexpected query version")

    if len(queries["queries"]) != QUERY_COUNT:
        raise ValueError(
            f"Expected {QUERY_COUNT} frozen queries"
        )

    if models["experiment_id"] != EXPERIMENT_ID:
        raise ValueError("Wrong models experiment_id")

    if models["status"] != "FROZEN_CONFIGURATION":
        raise ValueError("Model configuration must be frozen")

    if models["production_selection"]["status"] != "NOT_SELECTED":
        raise ValueError(
            "Production model must remain NOT_SELECTED"
        )

    judgments = validate_judgments(judgments_raw)

    query_ids = {
        query["query_id"]
        for query in queries["queries"]
    }

    if set(judgments) != query_ids:
        raise ValueError(
            "Judgment query IDs do not exactly match frozen query IDs"
        )

    requested = os.environ.get("EXP_MODEL_ID")

    if requested:
        if requested not in MODELS:
            raise ValueError(
                f"Unknown EXP_MODEL_ID: {requested}"
            )

        model_ids = [requested]
    else:
        model_ids = list(MODELS)

    print("=== EXP-4B6-001 T-7 EVALUATION ===")
    print(f"Models selected: {model_ids}")
    print(f"Frozen queries: {QUERY_COUNT}")
    print(f"Frozen relevance assignments: {JUDGMENT_ASSIGNMENTS}")
    print(f"Retrieval k: {TOP_K}")
    print("Production model selection: NOT_SELECTED")

    for model_id in model_ids:
        run_model(model_id, judgments)


if __name__ == "__main__":
    main()
