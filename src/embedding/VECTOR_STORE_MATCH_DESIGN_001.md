# VectorStoreMatch Design Specification 001

Status: DESIGN_RECONSTRUCTED
Contract version: 0.1-design

## 1. Purpose

VectorStoreMatch is a transient retrieval-result primitive at the
I-4 EmbeddingStore boundary.

It associates an immutable VectorRecord with the numeric retrieval
score produced by the I-4 search operation.

It exists to transport query-dependent retrieval information without
contaminating the persistent T-4 VectorRecord payload.

## 2. Fields

VectorStoreMatch contains exactly:

- record: VectorRecord
- score: float

## 3. Score Semantics

`score` is the numeric retrieval score produced by the retrieval
boundary for this result.

The current I-4 reference implementation uses cosine similarity as
its retrieval metric.

VectorStoreMatch does not define, calculate, normalize, or recompute
the score.

## 4. Ordering

A collection of VectorStoreMatch values returned by I-4 is ordered
according to the retrieval ordering established by I-4.

VectorStoreMatch does not independently sort or rank results.

## 5. Responsibility Boundary

I-4 owns:

- query-vector validation
- vector compatibility
- filtering
- exclusion handling
- retrieval metric calculation
- retrieval score generation
- deterministic ordering
- top-k selection
- construction of VectorStoreMatch values

I-6 owns:

- receiving T-5 QueryRequest
- obtaining the query vector through the approved query-embedding
  capability
- invoking I-4 search
- converting VectorStoreMatch values into T-6 RankedResult values
- preserving record identity, score, and ordering

T-6 owns the external ranked-result representation:

- record_id
- score

## 6. Persistence Boundary

VectorStoreMatch is transient retrieval context.

It is not:

- a replacement for VectorRecord
- part of T-4 payload
- persisted as canonical vector metadata
- a KnowledgeRecord
- an EmbeddingDocument
- an embedding model
- an evaluation record

## 7. T-4 Protection

No `_retrieval_score` or equivalent transient retrieval field is added
to T-4 payload.

Existing VectorRecord payload semantics remain unchanged.

## 8. T-5 Relationship

T-5 QueryRequest supplies:

- query
- k
- filters
- include_excluded

VectorStoreMatch does not contain query text, query vectors, filters,
or request metadata.

## 9. T-6 Relationship

For each match:

VectorStoreMatch.record.identity.record_id
    -> RankedResult.record_id

VectorStoreMatch.score
    -> RankedResult.score

The ordering of the VectorStoreMatch collection is preserved.

I-6 does not independently rank or rescore the results.

## 10. T-7 Relationship

VectorStoreMatch is runtime retrieval data.

It does not perform or contain:

- relevance judgments
- Recall
- nDCG
- MRR
- other evaluation metrics

Evaluation remains the responsibility of T-7/evaluation components.

## 11. Architectural Constraints

VectorStoreMatch must not:

- modify frozen I-2
- modify frozen I-3
- redefine T-4
- perform KnowledgeRecord transformation
- generate embeddings
- select embedding models
- perform vector storage
- independently calculate cosine similarity
- independently rank results
- perform graph traversal
- perform hybrid-score fusion
- perform RAG synthesis
- select production infrastructure

## 12. Reconstruction Basis

This design is reconstructed from:

- frozen I-4 behavior
- frozen VectorRecord/T-4 semantics
- reconstructed T-5 QueryRequest
- reconstructed T-6 RankedResult
- historical EXP-4B4 retrieval artifacts
- historical EXP-4B5 retrieval artifacts
- historical EXP-4B5-002 retrieval benchmark behavior

Historical evidence establishes that retrieval scores existed and were
associated with record identities, but does not establish the exact
original I-4 transport type.

Therefore this document is a design reconstruction and is not yet a
frozen contract.

## 13. Proposed Flow

T-5 QueryRequest
    |
    v
QueryEmbedder
    |
    v
query vector
    |
    v
I-4 EmbeddingStore.search()
    |
    v
VectorStoreMatch[]
    |
    v
I-6 RetrievalService
    |
    v
T-6 RankedResult[]

## 14. Freeze Status

NOT_FROZEN

Implementation must not be treated as validated until this design
passes compatibility review and an explicit contract decision is made.
