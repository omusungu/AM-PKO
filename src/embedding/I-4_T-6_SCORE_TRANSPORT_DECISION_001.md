# I-4 / T-6 Score Transport Decision 001

Status: DESIGN_DECISION_APPROVED
Contract version: 0.1-design

## 1. Decision

Adopt the intermediary `VectorStoreMatch` boundary for transport of
transient retrieval scores from I-4 to I-6.

VectorStoreMatch contains exactly:

- record: VectorRecord
- score: float

## 2. Rationale

The current frozen I-4 implementation computes retrieval scores but
does not expose them in its public search result.

T-6 RankedResult requires:

- record_id
- score

The historical experiment artifacts establish that retrieval scores
were retained with retrieved record identities, but the original
Python transport contract is not recoverable.

Therefore the score must cross the I-4/I-6 boundary explicitly.

VectorStoreMatch provides that transport without adding transient
retrieval data to the persistent T-4 payload.

## 3. Boundary Evolution

Current:

I-4 EmbeddingStore.search()
    -> list[VectorRecord]

Approved design direction:

I-4 EmbeddingStore.search()
    -> ordered collection of VectorStoreMatch

where each VectorStoreMatch contains:

    record: VectorRecord
    score: float

## 4. Responsibility

I-4 owns:

- similarity calculation
- retrieval score generation
- filtering
- exclusion handling
- deterministic ordering
- top-k selection
- construction of VectorStoreMatch

I-6 owns:

- query orchestration
- query embedding
- invocation of I-4
- conversion of VectorStoreMatch to T-6 RankedResult
- preservation of ordering and score

T-6 remains:

- record_id
- score

## 5. Prohibited Alternatives

The following are rejected:

- `_retrieval_score` in T-4 payload
- recomputation of cosine similarity in I-6
- independent ranking or rescoring in I-6
- removal of score from T-6
- silent modification of frozen I-4
- coupling score transport to a specific embedding model

## 6. Compatibility

Verified unchanged:

- T-3 VectorRecord structure
- T-4 payload semantics
- T-5 QueryRequest structure
- T-6 RankedResult structure
- I-2 contract
- I-3 contract
- I-5 contract

The required change is isolated to the I-4 retrieval-result boundary.

## 7. Freeze Protection

This decision authorizes design evolution of I-4 but does not itself
modify or freeze the I-4 implementation.

Before implementation:

- VectorStoreMatch must be specified as a concrete type.
- I-4 interface compatibility must be reviewed.
- I-4 implementation behavior must be updated deliberately.
- Existing I-4 regression tests must be rerun.
- I-6 must then be implemented against the approved boundary.

## 8. Future Compatibility

The match boundary keeps transient retrieval context separate from
persistent vector data.

The current score remains generic:

`score` = numeric retrieval score.

The current I-4 metric remains cosine similarity.

Future retrieval methods may require additional contract evolution;
such evolution must be explicit rather than encoded through T-4
payload fields.

## 9. Decision Status

APPROVED AS DESIGN DIRECTION

VectorStoreMatch is not yet frozen.

I-4 implementation is not yet modified.

I-6 implementation is not yet validated.

Production model selection remains unchanged and undecided.
