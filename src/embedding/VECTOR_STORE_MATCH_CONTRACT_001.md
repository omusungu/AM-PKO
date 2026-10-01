# VectorStoreMatch Contract 001

Status: CONTRACT_RECONSTRUCTED
Contract version: 0.1-design

## 1. Type Identity

Type name: VectorStoreMatch

Purpose:
Transient immutable transport of one I-4 retrieval match from the
vector-store boundary to retrieval orchestration.

## 2. Fields

VectorStoreMatch contains exactly two fields:

### record

Type:
VectorRecord

Meaning:
The immutable stored vector record associated with this retrieval
match.

### score

Type:
float

Meaning:
The numeric retrieval score produced by I-4 for the associated
VectorRecord.

## 3. Immutability

VectorStoreMatch is immutable.

It must not mutate:

- VectorRecord
- VectorIdentity
- VectorRecord payload
- retrieval score after construction

## 4. Score Rules

The type:

- accepts the score produced by I-4
- does not calculate the score
- does not normalize the score
- does not reinterpret the score
- does not independently validate it as cosine-specific
- does not rank or sort matches

The current I-4 metric is cosine similarity.

The field name remains the generic `score` because T-6 defines a
generic retrieval score rather than a cosine-specific field.

## 5. Ordering

VectorStoreMatch represents one match only.

Ordering belongs to the collection returned by I-4.

I-4 must return VectorStoreMatch values in its established retrieval
order.

VectorStoreMatch itself must not implement ranking behavior.

## 6. T-3 Relationship

VectorStoreMatch wraps an existing T-3 VectorRecord.

It does not replace, duplicate, or alter T-3.

The VectorRecord remains the source of:

- record identity
- vector
- dimension
- persistent payload

## 7. T-4 Relationship

The retrieval score is transient.

It must not be inserted into VectorRecord.payload.

No `_retrieval_score` field or equivalent is permitted.

## 8. I-4 Relationship

I-4 is responsible for:

1. validating the query vector
2. applying filters
3. applying exclusion rules
4. calculating the retrieval metric
5. producing the retrieval score
6. determining deterministic ordering
7. selecting top-k
8. constructing VectorStoreMatch values

## 9. I-6 Relationship

I-6 consumes ordered VectorStoreMatch values.

For each match:

    match.record.identity.record_id
        -> RankedResult.record_id

    match.score
        -> RankedResult.score

I-6 preserves the collection order and does not recalculate or
rescore the match.

## 10. T-5 Relationship

VectorStoreMatch does not contain:

- query text
- query vector
- k
- filters
- include_excluded
- query identifier

These remain outside the match type.

## 11. T-7 Relationship

VectorStoreMatch contains no:

- relevance judgment
- evaluation metric
- evaluation identifier
- aggregate result

Evaluation remains outside runtime retrieval transport.

## 12. Validation Requirements

A concrete implementation must validate at minimum:

- record is a VectorRecord
- score is numeric
- boolean is not accepted as a score
- score is represented as float
- NaN is rejected

No cosine-specific range restriction is introduced at this boundary.

## 13. Architectural Constraints

VectorStoreMatch must not:

- modify T-3
- modify T-4
- modify T-5
- modify T-6
- generate embeddings
- perform vector storage
- calculate similarity
- perform ranking
- perform filtering
- traverse graph relationships
- perform evaluation
- perform RAG synthesis
- select models
- select persistent infrastructure

## 14. Compatibility Decision

This contract is compatible with the approved I-4/T-6 score-transport
decision.

Required I-4 boundary evolution:

    list[VectorRecord]

to:

    list[VectorStoreMatch]

The existing I-4 implementation must not be modified until this
contract completes implementation review and regression planning.

## 15. Freeze Status

NOT_FROZEN

Next required gate:

Concrete implementation review and I-4 regression impact analysis.
