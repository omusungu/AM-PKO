# AM-PKO T-6 Freeze Manifest

Status: FROZEN_VALIDATED
Contract version: 0.2

## Contract

T-6 `RankedResult` represents one ranked semantic-retrieval match.

Fields:
- `record_id: str`
- `score: float`

Constraints:
- `record_id` must be a non-empty string.
- `score` must be numeric.
- boolean scores are rejected.
- numeric scores are normalized to `float`.
- NaN scores are rejected.
- the object is immutable.

## Score semantics

T-6 exposes a generic retrieval `score`.

The current I-4 implementation produces that score using cosine
similarity. Cosine-specific computation and interpretation remain an
I-4 responsibility and are not duplicated by T-6.

## Ordering

A collection of T-6 results preserves the ordering supplied by I-4.

I-4 is responsible for similarity computation, score generation,
deterministic tie-breaking, and top-k ordering.

T-6 does not independently recompute similarity or reorder results.

## I-4 relationship

I-4 returns ordered `VectorStoreMatch` objects.

Each `VectorStoreMatch` contains:
- the canonical T-3 `VectorRecord`;
- the transient retrieval `score`.

The score is transported without being added to the T-4 payload.

## I-6 relationship

I-6 converts:

`VectorStoreMatch.record.identity.record_id`
→ `RankedResult.record_id`

and:

`VectorStoreMatch.score`
→ `RankedResult.score`

I-6 preserves I-4 ordering.

## Boundary

T-6 does not contain:
- query text;
- query embedding;
- KnowledgeRecord content;
- relevance judgments;
- evaluation metrics;
- relationship traversal data;
- RAG-generated content;
- experiment-level `query_id`.

## Compatibility

T-6 is compatible with:
- frozen I-4 EmbeddingStore v0.2;
- frozen I-6 RetrievalService v0.2;
- T-5 QueryRequest v0.2.

No frozen I-2, I-3, I-4, I-5, or I-6 implementation is modified
by the T-6 freeze.

## Validation basis

- T-6 design reconstruction validated.
- T-6 design reconciliation validated.
- T-6 implementation validated.
- T-6 field and type validation passed.
- T-6 architectural boundary checks passed.
- T-5/T-6 freeze-readiness gate passed.

Production embedding-model selection remains separate and undecided.
Production vector-database selection remains separate and undecided.
