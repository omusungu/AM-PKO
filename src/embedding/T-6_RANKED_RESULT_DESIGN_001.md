# AM-PKO T-6 — RankedResult Design

Status: DESIGN_RECONSTRUCTED
Contract version: 0.1-design

## Purpose

T-6 represents one ranked semantic-retrieval match returned from the vector-search boundary.

## Fields

### record_id

Identifier of the KnowledgeRecord represented by the retrieved vector.

Type:
`str`

### score

Generic retrieval score produced by the I-4 vector-search boundary. The current I-4 implementation uses cosine similarity; T-6 does not make cosine-specific assumptions about the score.

Type:
`float`

## Ordering

A collection of T-6 RankedResult objects is ordered from highest retrieval score to lowest retrieval score.

I-4 remains responsible for similarity computation and deterministic tie-breaking.

T-6 does not independently recompute similarity or reorder results.

## Boundary

T-6 does not contain:

- query text
- query embedding
- KnowledgeRecord content
- relevance judgments
- evaluation metrics
- relationship traversal data
- RAG-generated content

`query_id` belongs to query-level experiment/evaluation grouping and is not part of the individual ranked match.

## Relationship to I-4

I-4 `EmbeddingStore.search()` returns an ordered collection of
`VectorStoreMatch` objects.

Each `VectorStoreMatch` contains:

- the canonical `VectorRecord`
- the transient retrieval `score` produced by I-4

The I-6 retrieval orchestration layer converts each selected
`VectorStoreMatch` into the T-6 representation.

That conversion must preserve:

- record identity
- retrieval score
- I-4 ordering

No semantic transformation of the KnowledgeRecord is performed.

## Reconstruction status

This is a design reconstruction, not a frozen historical contract.

Existing experiment artifacts directly evidence the `record_id` and `score` fields.

The exact historical Python interface and validation rules were not recoverable. The current T-6 contract is reconciled against the frozen I-4 VectorStoreMatch boundary and the frozen I-6 retrieval mapping.

No frozen I-2, I-3, I-4, or I-5 contract is modified by this design.
