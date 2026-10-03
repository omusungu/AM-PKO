# AM-PKO Interface Contract

## Purpose

The AM-PKO interface contract defines the stable boundaries between major architectural components.

The purpose is to allow heterogeneous implementations to participate in the same architecture without coupling the system to one implementation.

## Core Types

The current conceptual contract defines the following types:

- **T-1 — KnowledgeRecord**
- **T-2 — EmbeddingDocument**
- **T-3 — VectorRecord**
- **T-4 — Payload**
- **T-5 — QueryRequest**
- **T-6 — RankedResult**
- **T-7 — EvaluationRun**

These types form the principal data boundaries of the embedding and retrieval architecture.

## KnowledgeRecord

`KnowledgeRecord` is the authoritative structured representation of personal knowledge.

It provides the source information from which canonical embedding documents and other downstream representations are derived.

The KnowledgeRecord should remain independent of any particular embedding model or vector database.

## EmbeddingDocument

`EmbeddingDocument` is the canonical representation generated from a KnowledgeRecord for embedding.

Its purpose is to provide deterministic and model-independent input to the embedding interface.

The same architectural representation should therefore remain stable when the underlying embedding model changes.

## VectorRecord

`VectorRecord` represents the vector produced by an embedding implementation together with the identity and payload required for retrieval.

A vector record is derived from the embedding process and does not replace the originating KnowledgeRecord.

## Payload

`Payload` carries supporting information associated with a vector or retrieval result.

It may include identifiers, metadata, provenance, or other information required to resolve a result back to the authoritative knowledge representation.

## QueryRequest

`QueryRequest` represents a retrieval request entering the retrieval architecture.

It defines the information required to transform a query into a representation suitable for semantic retrieval.

## RankedResult

`RankedResult` represents a retrieval result together with the information required to order and interpret the result.

Ranking may be based on vector similarity and may later incorporate explicit relationship structure or other validated signals.

## EvaluationRun

`EvaluationRun` represents an evaluation execution against a defined corpus, query set, judgments, candidate model configuration, and recorded results.

Evaluation is therefore treated as an explicit architectural activity rather than an informal model comparison.

## Core Interfaces

The architecture defines stable interfaces corresponding to major responsibilities:

- **I-1 — RecordStore**
- **I-2 — EmbeddingDocumentGenerator**
- **I-3 — EmbeddingModel**
- **I-4 — EmbeddingStore**
- **I-5 — Retriever**
- **I-6 — RelationshipStore**
- **I-7 — EvaluationRunner**

Each interface defines a responsibility rather than prescribing one implementation.

## RecordStore

`RecordStore` provides access to authoritative KnowledgeRecords.

Its implementation may change without requiring changes to the embedding model or retrieval architecture.

## EmbeddingDocumentGenerator

`EmbeddingDocumentGenerator` transforms a KnowledgeRecord into the canonical EmbeddingDocument.

This boundary protects the embedding layer from direct dependence on raw record storage.

## EmbeddingModel

`EmbeddingModel` defines the contract that candidate embedding implementations must satisfy.

Different model families may implement the interface differently internally while remaining substitutable at the architectural boundary.

Examples include:

- BGE-M3
- multilingual-e5-large
- Qwen3-Embedding

## EmbeddingStore

`EmbeddingStore` stores and retrieves VectorRecords.

The storage implementation is independent of the embedding model.

This permits changes in storage technology without changing the semantic contract of the embedding layer.

## Retriever

`Retriever` converts a QueryRequest into RankedResults.

It may use:

- vector similarity
- relationship structure
- metadata
- compatibility constraints
- validation state

The retrieval implementation must preserve the meaning of the returned ranking signals.

## RelationshipStore

`RelationshipStore` provides access to explicit typed relationships between KnowledgeRecords.

It must preserve relationship identity, direction, type, and relevant validation information.

## EvaluationRunner

`EvaluationRunner` executes defined evaluation runs and records their inputs, candidate configurations, metrics, and results.

This provides reproducibility for model and architecture evaluation.

## Adapter Boundary

Model-specific behavior belongs behind adapters.

The adapter translates between the stable `EmbeddingModel` contract and the requirements of a particular runtime or model implementation.

This is a primary substitutability boundary in AM-PKO.

## Contract Compliance

An implementation is not considered interchangeable merely because it produces vectors or exposes similarly named methods.

It must satisfy the required contract.

Contract compliance includes, where applicable:

- valid input handling
- valid output structure
- dimensional consistency
- deterministic behavior where required
- error handling
- parser behavior
- pooling behavior
- separator handling
- source integrity
- regression compatibility

## Fail-Closed Behavior

Implementations that cannot satisfy the contract should fail closed.

The system should not silently convert malformed, incomplete, or ambiguous model output into apparently valid vectors.

This protects retrieval quality and preserves architectural integrity.

## Substitutability

AM-PKO defines substitutability through the contract rather than through implementation similarity.

Two implementations can be materially different and still occupy the same architectural role if they satisfy the same relevant interface and compatibility requirements.

Therefore:

**same role + compatible contract + validation = potential substitutability**

while:

**similar implementation ≠ guaranteed substitutability**

## Validation Before Replacement

Replacing an implementation should follow a validation process.

A candidate implementation should be checked for:

1. interface compliance
2. compatibility
3. regression behavior
4. retrieval behavior
5. performance
6. operational reliability

Only then should it be considered a validated substitute within the relevant context.

## Architectural Principle

> **AM-PKO interfaces define stable contracts between heterogeneous modules, allowing implementation to change while preserving architectural roles and system coherence.**

The interface is therefore the mechanism that makes heterogeneous modularity operational.

