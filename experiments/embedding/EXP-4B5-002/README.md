# EXP-4B5-002 — Retrieval Latency Benchmark

## Purpose

Measure the actual runtime cost of cosine-similarity retrieval using the
already-generated embeddings from EXP-4B5-001.

This experiment does not regenerate embeddings and does not modify
EXP-4B5-001.

## Scope

- 3 candidate embedding models
- 25 corpus vectors per model
- 25 query vectors per model
- 1024-dimensional vectors
- cosine similarity
- brute-force search over the full 25-record corpus
- top-k = 5
- retrieval latency measured separately from embedding generation

## Source Experiment

EXP-4B5-001

## Models

- M-000001 BGE-M3
- M-000002 E5
- M-000003 Qwen3-Embedding

## Benchmark Method

For each model:

1. Load the saved corpus embeddings.
2. Load the saved query embeddings.
3. Perform cosine-similarity search for every query.
4. Return the top 5 records.
5. Measure retrieval latency independently.
6. Record per-query latency.
7. Calculate mean, median, minimum, and maximum latency.
8. Verify that benchmark rankings reproduce the existing EXP-4B5-001 retrieval results.

## Status

FROZEN_VALIDATED
