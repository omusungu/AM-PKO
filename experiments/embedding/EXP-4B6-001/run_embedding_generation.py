import json
import math
import os
import time
from pathlib import Path

from embedding.adapters.llama_cpp.adapter import LlamaCppEmbeddingAdapter
from embedding.generators.er10 import ER10EmbeddingDocumentGenerator


ROOT = Path(__file__).resolve().parent
CORPUS = ROOT / "corpus.json"
QUERIES = ROOT / "queries.json"
MODELS = ROOT / "models.json"


def protocol_for(model):
    protocol = model.get("protocol")
    input_protocol = model.get("input_protocol")

    if model["id"] == "M-000003":
        instruction = protocol["query_instruction"]
        return (
            f"Instruct: {instruction}\nQuery:",
            "",
            protocol["query_format"],
        )

    if model["id"] == "M-000002":
        return (
            input_protocol["query_prefix"],
            input_protocol["document_prefix"],
            "query/document prefix protocol",
        )

    return "", "", "content only"


def build_adapter(model):
    query_prefix, document_prefix, _ = protocol_for(model)

    return LlamaCppEmbeddingAdapter(
        model_path=model["local_file"],
        model_id=model["id"],
        model_family=model["family"],
        dimension=model["embedding_dimension"],
        max_input_tokens=model["context"],
        pooling=model["pooling"],
        normalize=model["normalization"],
        context_size=model["context"],
        threads=model["threads"],
        separator="\x1e",
        query_prefix=query_prefix,
        document_prefix=document_prefix,
    )


def finite(vector):
    return all(math.isfinite(float(x)) for x in vector)


def summarize(latencies):
    return {
        "count": len(latencies),
        "mean_latency_ms": round(sum(latencies) / len(latencies), 2),
        "min_latency_ms": round(min(latencies), 2),
        "max_latency_ms": round(max(latencies), 2),
    }


def main():
    corpus = json.loads(CORPUS.read_text())
    queries = json.loads(QUERIES.read_text())
    models = json.loads(MODELS.read_text())

    if corpus["status"] != "FROZEN":
        raise RuntimeError("Corpus is not FROZEN")

    if queries["status"] != "FROZEN":
        raise RuntimeError("Queries are not FROZEN")

    if models["status"] != "FROZEN_CONFIGURATION":
        raise RuntimeError("Model configuration is not frozen")

    if corpus["corpus_version"] != "0.1":
        raise RuntimeError("Unexpected corpus version")

    if queries["corpus_version"] != "0.1":
        raise RuntimeError("Query/corpus version mismatch")

    if corpus["record_count"] != len(corpus["records"]):
        raise RuntimeError("Corpus record count mismatch")

    if queries["query_count"] != len(queries["queries"]):
        raise RuntimeError("Query count mismatch")

    generator = ER10EmbeddingDocumentGenerator()

    print("=== EXP-4B6-001 EMBEDDING GENERATION ===")
    print("corpus:", len(corpus["records"]))
    print("queries:", len(queries["queries"]))
    print("candidates:", len(models["candidates"]))

    selected_model = os.environ.get("EXP_MODEL_ID")
    candidates = models["candidates"]

    if selected_model:
        candidates = [
            model for model in candidates
            if model["id"] == selected_model
        ]
        if not candidates:
            raise RuntimeError(
                f"Unknown EXP_MODEL_ID: {selected_model}"
            )

    for model in candidates:
        adapter = build_adapter(model)
        query_prefix, document_prefix, protocol_description = protocol_for(model)

        corpus_records = []
        corpus_latencies = []

        print(
            f"START {model['id']} {model['family']}: "
            f"100 embeddings",
            flush=True,
        )

        for index, record in enumerate(corpus["records"], 1):
            document = generator.generate(record)
            input_text = document_prefix + document.document_text

            start = time.perf_counter()
            vector = adapter.embed_document(document.document_text)
            latency_ms = (time.perf_counter() - start) * 1000

            if len(vector) != model["embedding_dimension"]:
                raise RuntimeError(
                    f"{model['id']} {record['id']}: dimension mismatch"
                )

            if not finite(vector):
                raise RuntimeError(
                    f"{model['id']} {record['id']}: non-finite vector"
                )

            token_count = adapter.token_count(input_text)

            corpus_records.append(
                {
                    "record_id": record["id"],
                    "embedding": [float(x) for x in vector],
                    "latency_ms": round(latency_ms, 2),
                    "token_count": token_count,
                    "document_hash": document.document_hash,
                    "embedding_spec_version": document.embedding_spec_version,
                }
            )
            corpus_latencies.append(latency_ms)

            print(
                f"{model['id']} corpus {index}/50 "
                f"{record['id']} latency_ms={latency_ms:.1f}",
                flush=True,
            )

        query_records = []
        query_latencies = []

        for index, query in enumerate(queries["queries"], 1):
            input_text = query_prefix + query["query"]

            start = time.perf_counter()
            vector = adapter.embed_query(query["query"])
            latency_ms = (time.perf_counter() - start) * 1000

            if len(vector) != model["embedding_dimension"]:
                raise RuntimeError(
                    f"{model['id']} {query['query_id']}: dimension mismatch"
                )

            if not finite(vector):
                raise RuntimeError(
                    f"{model['id']} {query['query_id']}: non-finite vector"
                )

            token_count = adapter.token_count(input_text)

            query_records.append(
                {
                    "query_id": query["query_id"],
                    "embedding": [float(x) for x in vector],
                    "latency_ms": round(latency_ms, 2),
                    "token_count": token_count,
                }
            )
            query_latencies.append(latency_ms)

            print(
                f"{model['id']} query {index}/50 "
                f"{query['query_id']} latency_ms={latency_ms:.1f}",
                flush=True,
            )

        corpus_output = {
            "experiment_id": "EXP-4B6-001",
            "model_id": model["id"],
            "model_family": model["family"],
            "embedding_dimension": model["embedding_dimension"],
            "pooling": model["pooling"],
            "normalization": model["normalization"],
            "context": model["context"],
            "threads": model["threads"],
            "input_protocol": protocol_description,
            "er10_spec_version": "0.1",
            "corpus_version": corpus["corpus_version"],
            "records": corpus_records,
            "summary": summarize(corpus_latencies),
        }

        query_output = {
            "experiment_id": "EXP-4B6-001",
            "model_id": model["id"],
            "model_family": model["family"],
            "embedding_dimension": model["embedding_dimension"],
            "pooling": model["pooling"],
            "normalization": model["normalization"],
            "context": model["context"],
            "threads": model["threads"],
            "query_protocol": protocol_description,
            "corpus_version": corpus["corpus_version"],
            "query_version": queries["query_version"],
            "queries": query_records,
            "summary": summarize(query_latencies),
        }

        corpus_path = ROOT / f"{model['id']}_corpus_embeddings.json"
        query_path = ROOT / f"{model['id']}_query_embeddings.json"

        corpus_path.write_text(
            json.dumps(corpus_output, indent=2) + "\n"
        )
        query_path.write_text(
            json.dumps(query_output, indent=2) + "\n"
        )

        print(
            f"{model['id']} {model['family']}: "
            f"corpus={len(corpus_records)} "
            f"queries={len(query_records)} "
            f"status=PASS"
        )

    print("RESULT: PASS")


if __name__ == "__main__":
    main()
