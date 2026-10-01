# AM-PKO T-5 — QueryRequest Design

Status: DESIGN_RECONSTRUCTED
Contract version: 0.1-design

## Purpose

T-5 represents one natural-language retrieval request before query embedding and vector search.

## Fields

### query
Natural-language query text supplied for semantic retrieval.

Type:
`str`

### k
Maximum number of ranked vector matches requested from I-4.

Type:
`int`

Constraint:
`k > 0`

### filters
I-4-compatible metadata filters forwarded without semantic reinterpretation.

Type:
`Mapping[str, Sequence[str]] | None`

Default:
`None`

### include_excluded
Controls whether records marked as excluded are eligible for I-4 search.

Type:
`bool`

Default:
`False`

## Boundary

T-5 does not:

- generate embeddings
- select an embedding model
- transform KnowledgeRecords
- generate EmbeddingDocuments
- perform cosine similarity
- rank vectors
- traverse relationships
- perform graph retrieval
- perform RAG synthesis
- mutate canonical KnowledgeRecords

## Relationship to I-4

The retrieval orchestration layer passes:

- query vector
- `k`
- `filters`
- `include_excluded`

to `EmbeddingStore.search()`.

T-5 does not redefine I-4 search semantics.

## Query identity

Historical experiment files use `query_id` for evaluation and experiment tracking. `query_id` is not included in this initial T-5 request design because its runtime identity semantics were not recoverable from the production repository.

## Reconstruction status

This is a design reconstruction, not a frozen historical contract.

The exact historical field names and validation rules were not recoverable.

No frozen I-2, I-3, I-4, or I-5 contract is modified by this design.
