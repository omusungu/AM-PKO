# AM-PKO I-6 — Retrieval Service Contract

Status: FROZEN_VALIDATED
Contract version: 0.2

## Purpose

I-6 defines the retrieval-orchestration boundary for AM-PKO.

It coordinates T-5 QueryRequest input, query-vector generation,
I-4 EmbeddingStore retrieval, and T-6 RankedResult output.

I-6 does not redefine embedding-model behavior, vector storage,
similarity computation, knowledge transformation, or evaluation
semantics.

## Canonical flow

T-5 QueryRequest
→ query embedding path
→ query vector
→ I-4 EmbeddingStore.search()
→ VectorStoreMatch collection
→ T-6 RankedResult collection

The I-4 result boundary is:

VectorStoreMatch
- record: T-3 VectorRecord
- score: transient retrieval score

I-6 maps each match to T-6 while preserving record identity,
retrieval score, and I-4 ordering.

## Interface

`embedding/retrieval_service.py`

### RetrievalService

Constructor dependencies:

- `QueryEmbedder`
- `EmbeddingStore`

### retrieve(request)

Accepts exactly one canonical T-5 `QueryRequest`.

The method:

1. validates the T-5 request type;
2. obtains a query vector through `QueryEmbedder`;
3. calls I-4 `EmbeddingStore.search()`;
4. forwards `k`, `filters`, and `include_excluded`;
5. requires I-4 results to be `VectorStoreMatch` values;
6. maps each match to a T-6 `RankedResult`;
7. preserves I-4 ordering and retrieval scores.

## Query embedding boundary

I-6 consumes the separate `QueryEmbedder` capability:

`embed_query(text)`

The current reference path delegates through the existing llama.cpp
adapter query-embedding capability.

I-6 does not modify the frozen I-3 `EmbeddingModel` contract and does
not define model-specific embedding behavior.

## T-5 relationship

I-6 consumes:

- query text;
- positive `k`;
- optional metadata filters;
- `include_excluded`.

I-6 does not alter T-5 semantics.

## I-4 relationship

I-4 owns:

- vector compatibility validation;
- metadata filtering;
- exclusion handling;
- similarity computation;
- retrieval-score generation;
- deterministic ordering;
- top-k selection;
- `VectorStoreMatch` construction.

I-6 consumes these results and does not recompute, normalize,
reinterpret, or independently rank them.

## T-6 relationship

Each I-4 match is mapped as:

`match.record.identity.record_id`
→ `RankedResult.record_id`

`match.score`
→ `RankedResult.score`

The returned T-6 collection preserves I-4 ordering.

I-6 performs no additional ranking.

## T-4 protection

Retrieval scores are transient query-dependent values.

They are transported through `VectorStoreMatch` and are not stored in
the T-4 payload.

I-6 does not depend on an undocumented `_retrieval_score` payload field.

## Architectural boundaries

I-6 does not:

- redefine I-3 `EmbeddingModel`;
- generate T-2 `EmbeddingDocuments`;
- transform `KnowledgeRecord` values;
- generate or mutate `VectorRecord` values;
- implement vector storage;
- implement similarity computation;
- independently reorder or rescore retrieval results;
- traverse relationship graphs;
- perform graph/vector fusion;
- perform RAG synthesis;
- calculate retrieval evaluation metrics;
- select a production embedding model;
- select a persistent vector database.

## Validation

I-6 freeze conformance gate: PASS

I-6 design reconciliation: PASS

VectorStoreMatch boundary validation: PASS

T-5 QueryRequest boundary validation: PASS

T-6 RankedResult boundary validation: PASS

I-4 frozen-contract compatibility: PASS

Retrieval-score preservation: PASS

I-4 ordering preservation: PASS

Similarity recomputation protection: PASS

T-4 score-contamination protection: PASS

Python syntax validation: PASS

## Production status

This manifest freezes the I-6 retrieval-orchestration contract only.

No production embedding model is selected by I-6.

No production vector database is selected by I-6.

Production model selection remains governed by the separate embedding
model-selection framework and decision record.

## Freeze basis

I-6 was reconstructed because a complete historical I-6 contract was
not recoverable from the repository.

The frozen I-6 contract is based on:

- T-5 QueryRequest;
- T-6 RankedResult;
- I-4 EmbeddingStore;
- I-4 VectorStoreMatch score transport;
- I-3 EmbeddingModel;
- I-5 EmbeddingService;
- EXP-4B5 retrieval behavior;
- validated reference implementation behavior.

The I-4/T-6 score-transport decision authorizes the use of
`VectorStoreMatch` as the transient boundary between I-4 retrieval and
I-6 orchestration.

No frozen I-2, I-3, I-4, or I-5 contract is modified by this manifest.
