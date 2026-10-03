# AM-PKO Embedding Architecture

## Purpose

The AM-PKO embedding architecture provides a replaceable mechanism for transforming structured knowledge into vector representations for semantic retrieval.

The embedding model is an implementation component, not the architecture itself.

## Architectural Flow

The embedding pipeline is:

**KnowledgeRecord → Canonical EmbeddingDocument → Embedding Interface → Candidate Model → VectorRecord → Retrieval**

This separates the stable AM-PKO knowledge representation from model-specific implementation details.

## KnowledgeRecord

The `KnowledgeRecord` is the authoritative structured representation of a unit of personal knowledge.

It contains information such as:

- domain
- project
- knowledge type
- topic
- granularity
- title
- content
- status
- source
- skills
- assets
- actions
- relationships
- metadata

The embedding system consumes this structured representation rather than coupling directly to arbitrary source documents.

## Canonical EmbeddingDocument

Before embedding, a KnowledgeRecord is transformed into a deterministic canonical representation.

The purpose of the canonical representation is to ensure that the same KnowledgeRecord produces a stable embedding input independent of the particular embedding model.

This creates a boundary between:

**knowledge representation**

and

**vector representation**

## Embedding Interface

Candidate models are accessed through a stable embedding interface.

The interface defines the contract required from an embedding implementation without requiring the architecture to depend on a specific model family.

This allows candidate models to be evaluated and replaced without changing the surrounding knowledge architecture.

## Candidate Models

The current candidate families include:

- BGE-M3
- multilingual-e5-large
- Qwen3-Embedding

These are evaluation candidates, not architectural commitments.

A candidate becomes usable only when it satisfies the required interface and passes the relevant contract, compatibility, regression, and evaluation checks.

## Heterogeneous Model Substitutability

The candidate models are heterogeneous implementations.

They may differ in:

- architecture
- tokenizer
- dimensionality
- pooling behavior
- inference runtime
- resource requirements
- embedding characteristics
- performance

They can nevertheless occupy the same architectural role when they satisfy the embedding interface.

Therefore, substitutability is conditional rather than absolute.

A model is substitutable for another model only within the contract and evaluation context in which both are valid implementations.

## VectorRecord

The output of the embedding model is represented as a vector record.

A vector record associates a vector with the identity and relevant payload needed for retrieval.

The vector representation should not replace the original KnowledgeRecord.

The KnowledgeRecord remains the authoritative semantic representation.

## Retrieval

Embedding vectors support semantic similarity retrieval.

A simplified retrieval flow is:

**Query → Query Representation → Vector Similarity → Ranked Results**

The retrieval layer may then combine semantic similarity with explicit relationship structure.

Therefore:

**vector similarity ≠ relationship**

A high vector similarity does not automatically establish a semantic relationship between two knowledge records.

## Graph and Vector Separation

AM-PKO maintains a conceptual separation between graph relationships and vector representations.

The graph expresses explicit typed relationships.

Vectors express learned numerical representations useful for similarity-based retrieval.

Both can contribute to reasoning, but they represent different kinds of information.

## Evaluation

Candidate embedding implementations are evaluated rather than selected solely by architectural preference.

Relevant evaluation dimensions include:

- retrieval quality
- embedding runtime
- retrieval latency
- interface compliance
- regression behavior
- resource requirements
- operational reliability

The AM-PKO experiments include:

- `EXP-4B4-001` — embedding evaluation corpus
- `EXP-4B5-001` — embedding quality and runtime evaluation
- `EXP-4B5-002` — retrieval latency benchmark

## Runtime Adapter

Model-specific runtime behavior is isolated behind adapters.

This allows the core embedding interface to remain stable while different runtimes or model implementations change underneath it.

The adapter boundary is therefore an architectural substitutability boundary.

## Fail-Closed Principle

Where an embedding implementation cannot satisfy the required contract or produce a valid representation, the system should fail closed rather than silently producing an invalid vector.

This protects downstream retrieval from corrupted or ambiguous representations.

## Architectural Principle

> **AM-PKO does not choose an embedding model first and build the architecture around it. It defines the architectural contract first and evaluates heterogeneous embedding implementations against that contract.**

This preserves model independence and allows the embedding layer to evolve without destabilizing the broader AM-PKO architecture.
