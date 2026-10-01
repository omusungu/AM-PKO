# AM-PKO T-5 Freeze Manifest

Status: FROZEN_VALIDATED
Contract version: 0.2

## Contract

T-5 `QueryRequest` represents one natural-language retrieval request
before query embedding and vector search.

Fields:
- `query: str`
- `k: int`
- `filters: Mapping[str, Sequence[str]] | None`
- `include_excluded: bool`

Constraints:
- `query` must be a non-empty string.
- `k` must be an integer greater than zero.
- `filters` must be a mapping or `None`.
- `include_excluded` must be boolean.
- The object is immutable.

## Responsibilities

T-5 defines retrieval-request input only.

T-5 does not:
- generate embeddings;
- select embedding models;
- transform KnowledgeRecords;
- generate EmbeddingDocuments;
- perform vector similarity;
- rank vectors;
- traverse relationships;
- perform graph retrieval;
- perform RAG synthesis;
- mutate canonical KnowledgeRecords.

## I-4 relationship

I-6 forwards the T-5 retrieval controls to I-4:

- query vector;
- `k`;
- `filters`;
- `include_excluded`.

T-5 does not redefine I-4 search semantics.

## Query identity

Historical experiment `query_id` values remain experiment/evaluation
identifiers and are not part of the frozen runtime T-5 request contract.

## Compatibility

T-5 is compatible with:
- frozen I-4 EmbeddingStore v0.2;
- frozen I-6 RetrievalService v0.2;
- T-6 RankedResult v0.2.

No frozen I-2, I-3, I-4, I-5, or I-6 implementation is modified
by the T-5 freeze.

## Validation basis

- T-5 design reconstruction validated.
- T-5 implementation validated.
- T-5 field and type validation passed.
- T-5 architectural boundary checks passed.
- T-5/T-6 freeze-readiness gate passed.

Production embedding-model selection remains separate and undecided.
Production vector-database selection remains separate and undecided.
