import json
import statistics
import time
from pathlib import Path

import numpy as np

SOURCE = Path.home() / "AM-PKO/experiments/embedding/EXP-4B5-001"
OUT = Path.home() / "AM-PKO/experiments/embedding/EXP-4B5-002"

MODELS = [
    ("M-000001", "BGE-M3"),
    ("M-000002", "E5"),
    ("M-000003", "Qwen3-Embedding"),
]

WARMUPS = 3
REPETITIONS = 10
TOP_K = 5


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_records(data):
    if isinstance(data, dict):
        return data["records"]
    return data


def extract_queries(data):
    if isinstance(data, dict):
        return data["queries"]
    return data


def normalize_records(records, key):
    vectors = []
    ids = []

    for item in records:
        record_id = item[key]
        vector = np.asarray(item["embedding"], dtype=np.float32)
        ids.append(record_id)
        vectors.append(vector)

    matrix = np.vstack(vectors)
    return ids, matrix


def retrieve(query_vector, corpus_ids, corpus_matrix):
    q = np.asarray(query_vector, dtype=np.float32)

    q_norm = np.linalg.norm(q)
    corpus_norms = np.linalg.norm(corpus_matrix, axis=1)

    similarities = np.dot(corpus_matrix, q) / (corpus_norms * q_norm)

    order = np.argsort(-similarities, kind="stable")[:TOP_K]

    return [
        {
            "record_id": corpus_ids[i],
            "similarity": float(similarities[i]),
        }
        for i in order
    ]


def benchmark_model(model_id, model_name):
    corpus_path = SOURCE / f"{model_id}_corpus_embeddings.json"
    query_path = SOURCE / f"{model_id}_query_embeddings.json"
    retrieval_path = SOURCE / f"{model_id}_retrieval.json"

    corpus_data = load_json(corpus_path)
    query_data = load_json(query_path)
    expected = load_json(retrieval_path)

    corpus_records = extract_records(corpus_data)
    query_records = extract_queries(query_data)

    corpus_ids, corpus_matrix = normalize_records(corpus_records, "record_id")

    query_ids = [item["query_id"] for item in query_records]
    query_vectors = [
        np.asarray(item["embedding"], dtype=np.float32)
        for item in query_records
    ]

    # Warm-up: execute retrieval without recording latency.
    for _ in range(WARMUPS):
        for q in query_vectors:
            retrieve(q, corpus_ids, corpus_matrix)

    per_query = []
    ranking_matches = 0

    if isinstance(expected, dict):
        expected_items = expected["results"]
    else:
        expected_items = expected

    expected_by_query = {}

    for item in expected_items:
        if "results" in item:
            ranked = item["results"]
        elif "top_k" in item:
            ranked = item["top_k"]
        else:
            raise ValueError(
                f"Unknown retrieval result schema for {item['query_id']}"
            )

        expected_by_query[item["query_id"]] = ranked

    for query_id, query_vector in zip(query_ids, query_vectors):
        samples = []

        for _ in range(REPETITIONS):
            start = time.perf_counter_ns()
            results = retrieve(query_vector, corpus_ids, corpus_matrix)
            end = time.perf_counter_ns()

            samples.append((end - start) / 1_000_000)

        final_results = retrieve(query_vector, corpus_ids, corpus_matrix)

        actual_ids = [item["record_id"] for item in final_results]
        expected_ids = [
            item["record_id"]
            for item in expected_by_query[query_id][:TOP_K]
        ]

        matches = actual_ids == expected_ids

        if matches:
            ranking_matches += 1

        per_query.append(
            {
                "query_id": query_id,
                "repetitions": REPETITIONS,
                "mean_latency_ms": statistics.mean(samples),
                "median_latency_ms": statistics.median(samples),
                "min_latency_ms": min(samples),
                "max_latency_ms": max(samples),
                "top_k": final_results,
                "ranking_matches_existing": matches,
            }
        )

    all_samples = [
        sample
        for item in per_query
        for sample in []
    ]

    mean_latencies = [x["mean_latency_ms"] for x in per_query]
    median_latencies = [x["median_latency_ms"] for x in per_query]
    min_latencies = [x["min_latency_ms"] for x in per_query]
    max_latencies = [x["max_latency_ms"] for x in per_query]

    result = {
        "experiment_id": "EXP-4B5-002",
        "source_experiment": "EXP-4B5-001",
        "model_id": model_id,
        "model_name": model_name,
        "method": {
            "similarity": "cosine",
            "search_type": "brute_force",
            "corpus_size": len(corpus_ids),
            "query_count": len(query_ids),
            "embedding_dimension": int(corpus_matrix.shape[1]),
            "top_k": TOP_K,
            "warmup_passes": WARMUPS,
            "timed_repetitions_per_query": REPETITIONS,
        },
        "ranking_verification": {
            "queries_checked": len(query_ids),
            "top_k_rankings_matching": ranking_matches,
            "all_rankings_match": ranking_matches == len(query_ids),
        },
        "latency_ms": {
            "mean_of_query_means": statistics.mean(mean_latencies),
            "median_of_query_medians": statistics.median(median_latencies),
            "minimum": min(min_latencies),
            "maximum": max(max_latencies),
        },
        "per_query": per_query,
    }

    output_path = OUT / f"{model_id}_retrieval_benchmark.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(f"\n{model_id} {model_name}")
    print(f"Queries: {len(query_ids)}")
    print(f"Corpus: {len(corpus_ids)}")
    print(f"Dimensions: {corpus_matrix.shape[1]}")
    print(f"Mean retrieval latency: {result['latency_ms']['mean_of_query_means']:.6f} ms")
    print(f"Median retrieval latency: {result['latency_ms']['median_of_query_medians']:.6f} ms")
    print(f"Minimum: {result['latency_ms']['minimum']:.6f} ms")
    print(f"Maximum: {result['latency_ms']['maximum']:.6f} ms")
    print(
        f"Ranking matches: {ranking_matches}/{len(query_ids)}"
    )
    print(f"Saved: {output_path}")

    return result


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    results = []

    print("=== EXP-4B5-002 RETRIEVAL LATENCY BENCHMARK ===")
    print(f"Source: {SOURCE}")
    print(f"Warmups: {WARMUPS}")
    print(f"Repetitions/query: {REPETITIONS}")
    print(f"Top-k: {TOP_K}")

    for model_id, model_name in MODELS:
        results.append(benchmark_model(model_id, model_name))

    summary = {
        "experiment_id": "EXP-4B5-002",
        "source_experiment": "EXP-4B5-001",
        "benchmark_type": "RETRIEVAL_LATENCY",
        "method": {
            "similarity": "cosine",
            "search_type": "brute_force",
            "top_k": TOP_K,
            "warmup_passes": WARMUPS,
            "timed_repetitions_per_query": REPETITIONS,
        },
        "models": [
            {
                "model_id": r["model_id"],
                "model_name": r["model_name"],
                "mean_retrieval_latency_ms": r["latency_ms"][
                    "mean_of_query_means"
                ],
                "median_retrieval_latency_ms": r["latency_ms"][
                    "median_of_query_medians"
                ],
                "minimum_ms": r["latency_ms"]["minimum"],
                "maximum_ms": r["latency_ms"]["maximum"],
                "ranking_matches": r["ranking_verification"][
                    "top_k_rankings_matching"
                ],
                "queries_checked": r["ranking_verification"][
                    "queries_checked"
                ],
                "all_rankings_match": r["ranking_verification"][
                    "all_rankings_match"
                ],
            }
            for r in results
        ],
        "status": "COMPLETED",
    }

    summary_path = OUT / "EXP-4B5-002_retrieval_latency_summary.json"

    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print("\n=== FINAL SUMMARY ===")
    for item in summary["models"]:
        print(
            f"{item['model_id']} {item['model_name']}: "
            f"{item['mean_retrieval_latency_ms']:.6f} ms mean, "
            f"ranking {item['ranking_matches']}/{item['queries_checked']}"
        )

    print(f"\nSaved: {summary_path}")
    print("RESULT: PASS — retrieval benchmark completed")


if __name__ == "__main__":
    main()
