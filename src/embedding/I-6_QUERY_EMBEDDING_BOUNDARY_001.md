# I-6 Query Embedding Boundary — Design Record 001

Status: DESIGN_RECONSTRUCTED
Contract version: 0.1-design

## Purpose

Define how I-6 obtains a query vector without modifying the frozen
I-3 EmbeddingModel contract.

## Frozen I-3 Boundary

I-3 exposes:

- model_id()
- model_family()
- dimension()
- max_input_tokens()
- token_count(text)
- embed(text)
- identity()

I-3 does not expose embed_query() or embed_document().

## Concrete Adapter Capability

The existing llama.cpp adapter additionally exposes:

- embed_query(text)
- embed_document(text)

These methods are adapter-specific extensions and are not part of
the frozen I-3 interface.

## Query Embedding Rule

I-6 must not implement model-specific query-prefix behavior itself.

When a concrete embedding adapter provides query-specific embedding
behavior, that behavior remains inside the adapter.

I-6 may depend on an explicitly validated query-embedding capability
boundary, but must not alter I-3 merely to expose adapter-specific
behavior.

## Prohibited I-6 Behavior

I-6 must not:

- hard-code BGE/E5/Qwen query prefixes
- duplicate adapter query-prefix logic
- rewrite the query semantically
- modify the canonical KnowledgeRecord
- generate a T-2 EmbeddingDocument merely to perform query embedding
- perform cosine similarity itself
- rank or reorder I-4 results independently
- perform graph traversal or graph fusion
- calculate evaluation metrics
- select a production embedding model

## Architectural Position

The intended retrieval flow remains:

T-5 QueryRequest
→ approved query-embedding capability
→ query vector
→ I-4 EmbeddingStore.search()
→ ordered T-6 RankedResult collection

The frozen I-2, I-3, I-4, and I-5 contracts remain unchanged.

## Reconstruction Note

The historical I-6 query-embedding interface is not recoverable from
the repository. This document therefore records a design boundary,
not a recovered historical implementation.

No production model is selected by this design.
