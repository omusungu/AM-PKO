# AM-PKO I-4 Freeze Manifest

## Status

**FROZEN_VALIDATED**

Contract version: **0.2**

Interface: **I-4 EmbeddingStore**

Implementation status: **Validated reference implementation**

Production storage backend: **NOT_SELECTED**

---

## 1. Purpose

I-4 defines the storage boundary for AM-PKO T-3 VectorRecords.

The interface stores and retrieves canonical vectors together with their mandatory T-4 payload. The interface remains independent of the underlying storage engine.

---

## 2. Canonical Types

I-4 operates on:

- T-3 VectorIdentity
- T-3 VectorRecord
- T-4 payload

The VectorIdentity tuple is:

- record_id
- embedding_spec_version
- embedding_model_id
- record_version

The identity is immutable and functions as the primary identity of a stored vector.

---

## 3. T-4 Payload

Every vector entering the I-4 store must contain:

- record_id
- knowledge_type
- granularity
- domain
- project
- status
- topic
- skills[]
- source_type
- embedding_spec_version
- embedding_model_id
- record_version
- created_at

The payload provenance must agree with the T-3 identity.

Incomplete or inconsistent payloads are rejected.

---

## 4. Interface

I-4 provides:

- add()
- get()
- delete()
- search()
- count()
- health_check()

The `search()` operation returns an ordered collection of
`VectorStoreMatch` objects. Each match contains:

- the canonical `VectorRecord`
- the retrieval `score`

The score is transient retrieval output and is not added to the T-4
payload.

The interface does not expose storage-engine-specific behavior.

---

## 5. Reference Implementation

The validated reference implementation is:

`embedding.store.memory.InMemoryEmbeddingStore`

It exists to validate the I-4 contract before selecting persistent storage technology.

No production vector database has been selected by I-4.

---

## 6. Retrieval Behavior

The reference implementation supports:

- cosine similarity
- top-k retrieval
- payload filtering
- excluded-record handling
- deterministic tie-breaking
- retrieval-score preservation through `VectorStoreMatch`

I-4 constructs `VectorStoreMatch` objects after computing and ordering
retrieval scores.

Graph traversal is not performed.

Relationship data is not used for vector search.

---

## 7. Validation Evidence

### Interface validation

I-4 interface contract validation passed:

- required methods
- immutable VectorIdentity
- immutable VectorRecord
- abstract EmbeddingStore boundary

### T-4 validation

Passed:

- complete payload acceptance
- missing-field rejection
- identity mismatch rejection
- dimension mismatch rejection

### Behavioral validation

Passed:

- add/count
- get
- duplicate identity rejection
- cosine ranking
- payload filtering
- excluded-record handling
- include_excluded behavior
- delete/count
- deleted-record rejection
- zero-vector rejection
- invalid-k rejection
- missing-identity rejection
- health_check

### Validated-vector integration

The existing EXP-4B5-001 BGE-M3 embedding artifact was loaded without regenerating embeddings.

Evidence:

- corpus records: 25
- validated vectors: 25
- embedding dimension: 1024
- vectors stored: 25/25
- identities preserved: 25/25
- dimensions validated: 25/25
- model provenance validated
- filtered top-5 retrieval passed
- self-retrieval passed
- health_check passed

### Formal source/integrity audit

Result:

- Checks: 46
- Passed: 46
- Failed: 0

---

## 8. Architectural Boundary

I-4 does not:

- generate embeddings
- select embedding models
- transform KnowledgeRecords
- generate EmbeddingDocuments
- traverse relationships
- derive graph edges
- perform RAG synthesis
- perform semantic rewriting
- select a production vector database
- mutate canonical KnowledgeRecords

I-4 receives canonical VectorRecords and stores/searches them.

For retrieval, I-4 owns:

- similarity computation
- retrieval score generation
- filtering
- exclusion handling
- deterministic ordering
- top-k selection
- construction of `VectorStoreMatch`

The retrieval score is not stored in T-4 payloads.

---

## 9. Versioning

I-4 follows AM-PKO contract version 0.1.

Vector identity preserves:

- record_version
- embedding_spec_version
- embedding_model_id

Changing embedding model identity does not silently overwrite existing vectors.

Changing embedding specification requires vectors produced under the affected specification to be treated as a separate versioned vector population.

---

## 10. Freeze Decision

The previously frozen I-4 contract was deliberately evolved under
`I-4_T-6_SCORE_TRANSPORT_DECISION_001.md`.

The evolved contract now exposes `VectorStoreMatch` from `search()` so
retrieval scores can cross the I-4/I-6 boundary without contaminating
T-4 payloads.

Implementation and regression validation have passed. Re-freezing is
pending final contract-conformance validation.

The in-memory implementation is not designated as the production storage backend.

Persistent storage selection remains outside the I-4 contract and may be addressed later without changing the canonical I-4 interface.

---

## 11. Status

**FROZEN_VALIDATED**

I-4 EmbeddingStore has passed implementation and behavioral regression
validation for contract version 0.2.

Final contract-conformance validation against the approved
VectorStoreMatch score-transport decision passed.

I-4 is therefore re-frozen as a validated storage-interface boundary
under contract version 0.2.
