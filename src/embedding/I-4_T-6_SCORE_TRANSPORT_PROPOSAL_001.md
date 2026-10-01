# I-4 / T-6 Score Transport — Contract Evolution Proposal 001

Status: PROPOSAL_ONLY
Contract version: 0.1-design

## Problem

I-4 computes cosine similarity and uses it for deterministic ranking,
but the frozen EmbeddingStore.search() contract returns only VectorRecord.
T-6 requires the retrieval score.

## Evidence

Historical EXP-4B4 and EXP-4B5 retrieval artifacts contain record identity
and retrieval similarity/score values.

No historical Python score-transport implementation is recoverable.

## Proposed Boundary

Introduce a retrieval-specific transient result type at the I-4 retrieval
boundary containing:

- VectorRecord
- retrieval score

The score remains outside T-4 payload and VectorRecord.

## Proposed Flow

T-5 QueryRequest
→ QueryEmbedder
→ query vector
→ I-4 similarity search
→ retrieval match {VectorRecord, score}
→ I-6
→ T-6 RankedResult {record_id, score}

## Invariants

- I-4 remains the sole owner of cosine similarity calculation.
- I-4 remains the sole owner of similarity ordering.
- I-6 does not recompute cosine similarity.
- I-6 does not independently rank or rescore.
- T-4 payload is unchanged.
- VectorRecord is unchanged.
- I-2 remains unchanged.
- I-3 remains unchanged.
- I-5 remains unchanged.
- T-6 remains record_id + score.
- T-7 remains outside runtime retrieval.
- No production model or persistent vector database is selected.

## Contract Impact

This proposal would evolve the currently frozen I-4 search return
contract and therefore MUST NOT be implemented without explicit
contract review and a new validation/freeze decision.

## Current Decision

NOT_APPROVED
