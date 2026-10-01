# AM-PKO I-2 FREEZE MANIFEST

Status: FROZEN_VALIDATED
Contract version: 0.1
Interface: I-2 EmbeddingDocumentGenerator
Specification: ER-10
Specification version: 0.1

## Purpose

I-2 deterministically transforms a canonical AM-PKO KnowledgeRecord into
a T-2 EmbeddingDocument.

The transformation is formatting-only. It does not semantically rewrite,
summarize, infer, enrich, or otherwise modify the meaning of the source
record.

## Canonical T-2 Output

Each generated EmbeddingDocument contains:

- record_id
- record_version
- embedding_spec_version
- document_text
- document_hash

## ER-10 Document Structure

The canonical document contains:

[KNOWLEDGE_TYPE / GRANULARITY]
Domain:
Project:
Topic:
Title:
Content:
Skills:

Empty approved fields retain their labels without trailing whitespace.

## Included Record Content

ER-10 includes only:

- knowledge_type
- granularity
- domain
- project
- topic
- title
- content
- skills

## Excluded Record Content

The following are excluded from document_text:

- id
- status
- source
- metadata
- assets
- actions
- relationships

The record identifier and record version remain part of T-2 identity.

## Determinism

For the same KnowledgeRecord and embedding_spec_version:

- document_text is byte-identical
- document_hash is byte-identical
- no LLM or nondeterministic component is used
- whitespace formatting is deterministic

## Hashing

document_hash is SHA-256 over UTF-8 encoded document_text with the
canonical prefix:

sha256:

## Validation Record

Validated against the canonical EXP-4B5-001 corpus:

- Corpus records: 25
- Records generated: 25
- Identity/version mapping: PASS
- Canonical formatting: PASS
- Hash presence: PASS
- Deterministic repeat generation: PASS
- Independent SHA-256 verification: PASS
- Excluded-field isolation: PASS
- Metadata version identity behavior: PASS
- Fail-closed malformed-input validation: PASS
- Final source-integrity checks: 21/21 PASS

## Architecture Boundary

I-2 owns only:

KnowledgeRecord
    ->
EmbeddingDocument

I-2 does not:

- select embedding models
- execute embedding models
- generate vectors
- store vectors
- retrieve vectors
- rank results
- traverse relationships
- perform graph fusion
- perform semantic rewriting
- perform RAG synthesis

I-3 consumes the canonical EmbeddingDocument.

## Versioning

embedding_spec_version identifies the exact ER-10 formatting specification.

Changing embedding_spec_version invalidates vectors generated under the
previous specification and requires re-embedding affected records.

Changing record_version changes T-2 identity but does not itself alter
document_text unless the canonical record content also changes.

## Freeze Decision

I-2 and ER-10 are frozen as a validated deterministic transformation
boundary.

No embedding model is selected by I-2.

No vector database or retrieval implementation is coupled to I-2.

Status: FROZEN_VALIDATED
