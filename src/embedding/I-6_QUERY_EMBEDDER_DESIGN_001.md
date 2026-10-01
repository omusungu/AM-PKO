# I-6 Query Embedder — Design Record 001

Status: DESIGN_RECONSTRUCTED
Contract version: 0.1-design

## Purpose

Define the minimal capability required by I-6 to transform a
retrieval query string into a query vector.

## Proposed Capability

The query-embedding capability exposes exactly one operation:

embed_query(text: str) -> Sequence[float]

## Responsibility

The capability is responsible only for query embedding execution.

It may delegate to a concrete embedding adapter that implements
model-specific query behavior, including configured query prefixes.

## I-6 Relationship

I-6 consumes this capability.

I-6 does not:

- implement model-specific embedding behavior
- hard-code query prefixes
- call llama.cpp directly
- select an embedding model
- modify I-3
- generate T-2 EmbeddingDocuments for runtime queries
- perform cosine similarity
- rank or reorder results

## I-3 Relationship

The frozen I-3 EmbeddingModel interface remains unchanged.

The query-embedding capability is an orchestration dependency,
not a modification or replacement of I-3.

A concrete adapter may implement both the I-3 `embed()` contract
and this additional query-specific capability.

## I-4 Relationship

The resulting query vector is passed to:

EmbeddingStore.search(
    query_vector,
    k=request.k,
    filters=request.filters,
    include_excluded=request.include_excluded,
)

I-4 remains responsible for vector similarity, filtering,
exclusion handling, and deterministic ordering.

## T-5 Relationship

T-5 supplies:

- query
- k
- filters
- include_excluded

The query string is passed unchanged to the query-embedding
capability.

## T-6 Relationship

I-6 converts I-4's ordered VectorRecord search results into:

RankedResult(
    record_id=vector_record.identity.record_id,
    score=retrieval_score,
)

The original I-4 ordering is preserved.

## Architectural Boundary

T-5 QueryRequest
→ QueryEmbedder
→ query vector
→ I-4 EmbeddingStore.search()
→ ordered T-6 RankedResult collection

## Reconstruction Note

This is a design reconstruction because the historical query
embedding capability interface is not recoverable from the repository.

No frozen I-2, I-3, I-4, or I-5 contract is modified by this design.

No production model is selected.
