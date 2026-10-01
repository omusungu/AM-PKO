# EXP-4B5-001 — Expanded Embedding Evaluation

## Purpose
Evaluate the three candidate embedding models from EXP-4B4-001 on a larger 25-record AM-PKO corpus and 25-query evaluation set.

## Fixed Inputs
- Corpus: 25 records
- Queries: 25
- Relevance judgments: fixed before embedding generation
- Candidate models: M-000001, M-000002, M-000003
- Retrieval: cosine similarity
- Evaluation: Recall@1, Recall@3, Recall@5, HighRelevanceRecall@1, HighRelevanceRecall@3, HighRelevanceRecall@5, nDCG@1, nDCG@3, nDCG@5, MRR
- Runtime: llama.cpp embedding runtime on Android ARM64
- Experiment context: 512 tokens
- Threads: 8

## Method
1. Generate corpus embeddings for each candidate model.
2. Generate query embeddings using the model-specific query protocol.
3. Run cosine-similarity retrieval against the complete 25-record corpus.
4. Record rankings, similarity scores, and latency.
5. Evaluate rankings against the frozen relevance judgments.
6. Compare retrieval quality and encoding cost.
7. Do not modify corpus, queries, or judgments after observing model results.

## Selection Policy
This experiment does not assume that a model will win. Results will be reported for all candidates. A production model will not be selected solely from this small evaluation set.

## Reproducibility
Model identity, local model file, quantization, checksum, embedding dimension, runtime configuration, and model-specific prompting/protocol must remain recorded in models.json and generated result artifacts.

## Status
INPUTS_FROZEN
RESULTS_NOT_GENERATED
