from __future__ import annotations

import json
import os
from pathlib import Path

from embedding.store.interface import VectorIdentity, VectorRecord
from embedding.store.memory import InMemoryEmbeddingStore
from embedding.store.payload import validate_vector_record


ROOT = Path(__file__).resolve().parent
TOP_K = 5

MODELS = {
    "M-000001": "BGE-M3",
    "M-000002": "E5",
    "M-000003": "Qwen",
}


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_model_corpus(model_id: str) -> dict:
    return load_json(ROOT / f"{model_id}_corpus_embeddings.json")


def load_model_queries(model_id: str) -> dict:
    return load_json(ROOT / f"{model_id}_query_embeddings.json")


def build_store(corpus: dict, embedding_data: dict) -> InMemoryEmbeddingStore:
    store = InMemoryEmbeddingStore()
    embeddings_by_id = {
        item["record_id"]: item
        for item in embedding_data["records"]
    }

    for record in corpus["records"]:
        record_id = record["id"]
        embedding = embeddings_by_id[record_id]

        identity = VectorIdentity(
            record_id=record_id,
            embedding_spec_version=embedding["embedding_spec_version"],
            embedding_model_id=embedding_data["model_id"],
            record_version=str(record["metadata"]["version"]),
        )

        payload = {
            "record_id": record_id,
            "knowledge_type": record["knowledge_type"],
            "granularity": record["granularity"],
            "domain": record["domain"],
            "project": record["project"],
            "status": record["status"],
            "topic": record["topic"],
            "skills": record["skills"],
            "source_type": record["source"]["type"],
            "embedding_spec_version": embedding["embedding_spec_version"],
            "embedding_model_id": embedding_data["model_id"],
            "record_version": str(record["metadata"]["version"]),
            "created_at": record["metadata"]["created_at"],
        }

        vector_record = VectorRecord(
            identity=identity,
            dimension=int(embedding_data["embedding_dimension"]),
            vector=embedding["embedding"],
            payload=payload,
        )

        validate_vector_record(vector_record)
        store.add(vector_record)

    return store


def run_model(model_id: str, corpus: dict) -> None:
    embedding_data = load_model_corpus(model_id)
    query_data = load_model_queries(model_id)

    if embedding_data["experiment_id"] != "EXP-4B6-001":
        raise ValueError("Corpus embedding artifact has wrong experiment_id")

    if query_data["experiment_id"] != "EXP-4B6-001":
        raise ValueError("Query embedding artifact has wrong experiment_id")

    if embedding_data["model_id"] != model_id:
        raise ValueError("Corpus embedding artifact model_id mismatch")

    if query_data["model_id"] != model_id:
        raise ValueError("Query embedding artifact model_id mismatch")

    if len(embedding_data["records"]) != len(corpus["records"]):
        raise ValueError("Corpus embedding count does not match frozen corpus")

    if len(query_data["queries"]) != 50:
        raise ValueError("Query embedding count must be 50")

    store = build_store(corpus, embedding_data)

    results = []

    for index, query in enumerate(query_data["queries"], start=1):
        matches = store.search(
            query["embedding"],
            k=TOP_K,
        )

        ranked = [
            {
                "record_id": match.record.identity.record_id,
                "score": float(match.score),
            }
            for match in matches
        ]

        if len(ranked) != TOP_K:
            raise ValueError(
                f"{query['query_id']}: expected {TOP_K} results, got {len(ranked)}"
            )

        results.append(
            {
                "query_id": query["query_id"],
                "top_k": ranked,
            }
        )

        print(
            f"{model_id} {index}/50 {query['query_id']}: "
            f"{ranked[0]['record_id']} ({ranked[0]['score']:.9f})"
        )

    output = {
        "experiment_id": "EXP-4B6-001",
        "model_id": model_id,
        "model_family": MODELS[model_id],
        "similarity": "cosine",
        "search_type": "in_memory_store",
        "retrieval_k": TOP_K,
        "corpus_count": len(corpus["records"]),
        "query_count": len(results),
        "embedding_dimension": int(embedding_data["embedding_dimension"]),
        "results": results,
    }

    output_path = ROOT / f"{model_id}_retrieval.json"
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(output, handle, indent=2)

    print(f"RESULT: PASS — {output_path}")


def main() -> None:
    corpus = load_json(ROOT / "corpus.json")

    if corpus["experiment_id"] != "EXP-4B6-001":
        raise ValueError("Wrong experiment_id")

    if corpus["status"] != "FROZEN":
        raise ValueError("Corpus must be FROZEN")

    if corpus["corpus_version"] != "0.1":
        raise ValueError("Unexpected corpus version")

    if len(corpus["records"]) != 50:
        raise ValueError("Frozen corpus must contain 50 records")

    requested = os.environ.get("EXP_MODEL_ID")

    if requested:
        if requested not in MODELS:
            raise ValueError(f"Unknown EXP_MODEL_ID: {requested}")
        model_ids = [requested]
    else:
        model_ids = list(MODELS)

    print("=== EXP-4B6-001 RETRIEVAL GENERATION ===")
    print(f"Models selected: {model_ids}")
    print(f"Corpus records: {len(corpus['records'])}")
    print(f"Queries: 50")
    print(f"Similarity: cosine")
    print(f"Search: InMemoryEmbeddingStore")
    print(f"Top-k: {TOP_K}")

    for model_id in model_ids:
        run_model(model_id, corpus)


if __name__ == "__main__":
    main()
