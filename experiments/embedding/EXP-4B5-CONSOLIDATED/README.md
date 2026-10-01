# EXP-4B5-CONSOLIDATED — Embedding Evaluation Record

## Purpose

Provide one auditable record combining embedding retrieval quality,
embedding-generation runtime, and retrieval runtime for the three
AM-PKO embedding candidates evaluated in EXP-4B5-001 and EXP-4B5-002.

## Source Experiments

- EXP-4B5-001 — 25-record / 25-query embedding quality and generation-runtime evaluation
- EXP-4B5-002 — brute-force cosine retrieval-latency benchmark

Both source experiments remain frozen and are not modified by this record.

## Evaluation Scope

- Corpus: 25 knowledge records
- Queries: 25
- Relevance judgments: fixed before evaluation
- Models: 3
- Embedding dimension: 1024
- Similarity: cosine
- Retrieval: brute-force
- Retrieval top-k: 5

## Candidate Models

- M-000001 — BGE-M3
- M-000002 — multilingual E5-large
- M-000003 — Qwen3-Embedding-0.6B

## Quality Results

| Model | R@1 | R@3 | R@5 | HighRel@1 | HighRel@3 | HighRel@5 | nDCG@1 | nDCG@3 | nDCG@5 | MRR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BGE-M3 | 0.588000 | 0.869333 | 0.907333 | 0.871333 | 0.922667 | 0.940667 | 1.000000 | 0.937322 | 0.938382 | 1.000000 |
| E5 | 0.588000 | 0.836000 | 0.877333 | 0.831333 | 0.922667 | 0.950667 | 0.973333 | 0.917560 | 0.920593 | 1.000000 |
| Qwen3-Embedding | 0.588000 | 0.816000 | 0.928667 | 0.831333 | 0.922667 | 0.972000 | 0.973333 | 0.907977 | 0.936706 | 1.000000 |

## Mean Embedding-Generation Runtime

| Model | Corpus mean | Query mean | Combined mean |
|---|---:|---:|---:|
| BGE-M3 | 7224.50 ms | 5792.49 ms | 13016.99 ms |
| E5 | 6618.75 ms | 5853.71 ms | 12472.47 ms |
| Qwen3-Embedding | 4248.88 ms | 4790.28 ms | 9039.16 ms |

## Retrieval Runtime

EXP-4B5-002 used three warm-up passes and ten timed repetitions per
query.

| Model | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| BGE-M3 | 0.291401 ms | 0.289173 ms | 0.248962 ms | 0.395000 ms |
| E5 | 0.291354 ms | 0.290231 ms | 0.246923 ms | 0.458192 ms |
| Qwen3-Embedding | 0.238978 ms | 0.234942 ms | 0.230269 ms | 0.289884 ms |

## Ranking Reproducibility

All three models reproduced the existing EXP-4B5-001 top-5 retrieval
rankings for all 25 queries.

- BGE-M3: 25/25
- E5: 25/25
- Qwen3-Embedding: 25/25

## Interpretation

The evaluation shows that retrieval quality and runtime have different
trade-offs across the three candidates.

Embedding generation is substantially more expensive than brute-force
retrieval at the current 25-record corpus size.

Actual retrieval is sub-millisecond for all three candidates on the
benchmark device at this corpus size.

The results do not establish a universal production model choice.

## Limitations

- Only 25 corpus records were evaluated.
- Only 25 queries were evaluated.
- The relevance judgments are manually fixed for this experiment.
- The benchmark uses brute-force retrieval.
- Retrieval latency was measured on one Android ARM64 environment.
- Larger corpora may require a different retrieval architecture.
- The evaluation does not establish production-scale throughput,
  memory consumption, or concurrent-request performance.

## Production Selection

NOT_SELECTED

No production embedding model is selected from this evaluation alone.

## Reproducibility

The canonical experiment artifacts remain in:

- `../EXP-4B5-001/`
- `../EXP-4B5-002/`

The machine-readable consolidated record is:

`EXP-4B5-CONSOLIDATED_evaluation.json`

## Status

CONSOLIDATED_VALIDATED
