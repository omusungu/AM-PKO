# AM-PKO Retrieval Contract Reconstruction

Status: DESIGN_RECONSTRUCTION

## Recovered contract identities

- T-5: QueryRequest
- T-6: RankedResult
- T-7: EvaluationRun

These contracts are not currently implemented or frozen in the repository.

## Evidence recovered

### T-5 QueryRequest

Existing experiment queries establish the canonical query primitive:

- `query_id`
- natural-language `query`

I-4 independently defines the validated retrieval controls:

- `k`
- `filters`
- `include_excluded`

Therefore the reconstructed T-5 semantic boundary is:

- query text
- positive `k`
- I-4-compatible metadata filters
- I-4-compatible excluded-record handling

No alternative filter vocabulary is introduced.

### T-6 RankedResult

Existing retrieval artifacts establish the individual ranked-match representation:

- `record_id`
- `score`

Historical retrieval results are ordered top-k collections of these matches.

`query_id` belongs to the query-level result grouping, not the individual ranked match.

Evaluation metrics and relevance judgments are not part of T-6.

### T-7 EvaluationRun

Existing evaluation artifacts establish evaluation as a separate concern containing:

- experiment/model identity
- relevance judgments
- per-query evaluation
- aggregate metrics

Evaluation data is not part of T-6 retrieval results.

## Architectural boundary

The recovered retrieval flow is:

T-5 QueryRequest
→ query embedding
→ embedding model execution
→ I-4 EmbeddingStore.search()
→ ordered T-6 RankedResult collection

I-3 remains the model execution boundary.

I-4 remains the vector storage and primitive similarity-search boundary.

The future retrieval orchestration layer must not duplicate I-4 cosine similarity, metadata filtering, exclusion handling, or deterministic tie-breaking.

## Query/document embedding distinction

The frozen I-3 interface exposes only:

`EmbeddingModel.embed(text)`

The llama.cpp adapter additionally exposes:

- `embed_query(text)`
- `embed_document(text)`

The EXP-4B5-001 model configuration contains:

- `query_prefix: "query: "`
- `document_prefix: "passage: "`

Therefore query/document prefix behavior is treated as adapter/runtime behavior and does not modify the frozen I-3 contract.

## Reconstruction limitations

The exact historical field names, validation rules, and implementation interfaces for T-5, T-6, and T-7 were not recoverable from the repository.

The definitions above distinguish:

1. behavior directly evidenced by existing contracts and experiments; and
2. semantics reconstructed for future design.

No frozen I-2, I-3, I-4, or I-5 contract is modified by this reconstruction.
