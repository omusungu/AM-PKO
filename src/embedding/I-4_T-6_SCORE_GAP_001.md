# I-4 / T-6 Retrieval Score Gap — Design Record 001

Status: DESIGN_GAP_IDENTIFIED
Contract version: 0.1-design

## Finding

The frozen I-4 EmbeddingStore.search() contract returns:

list[VectorRecord]

The reference InMemoryEmbeddingStore computes cosine similarity
internally and uses the score for ordering, but discards the score
before returning the VectorRecord collection.

Therefore I-6 cannot obtain the retrieval score required by the
reconstructed T-6 RankedResult contract.

## Confirmed I-4 Behavior

I-4 performs:

1. query-vector validation
2. dimension compatibility checks
3. exclusion handling
4. metadata filtering
5. cosine similarity calculation
6. deterministic ordering
7. top-k selection

The returned value contains VectorRecord objects only.

## T-6 Requirement

The reconstructed T-6 contract contains:

- record_id
- score

The score represents the retrieval score produced by vector search.

## Invalid Solutions

The following are prohibited:

- adding an undocumented `_retrieval_score` payload field
- changing T-4 payload semantics solely to transport transient scores
- recomputing cosine similarity inside I-6
- independently ranking or rescoring results in I-6
- silently removing score from T-6
- modifying frozen I-4 without an explicit contract review

## Architectural Gap

Current reconstructed flow:

T-5 QueryRequest
→ QueryEmbedder
→ query vector
→ I-4 EmbeddingStore.search()
→ VectorRecord collection

Required T-6 flow:

T-5 QueryRequest
→ QueryEmbedder
→ query vector
→ I-4 similarity search
→ ordered record identity + retrieval score
→ T-6 RankedResult

The missing information is the retrieval score.

## Reconstruction Status

Historical transport semantics for the retrieval score are not
recoverable from the currently inspected I-4 interface.

The EXP-4B5 retrieval artifacts demonstrate that retrieval scores
existed at evaluation time, but they do not establish the historical
Python interface used to transport those scores.

## Freeze Protection

No frozen I-2, I-3, I-4, or I-5 implementation is modified by this
record.

I-6 remains NOT_FROZEN.

A contract decision is required before I-6 implementation can be
validated.
