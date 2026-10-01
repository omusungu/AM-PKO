# AM-PKO I-5 — Embedding Service Contract

Status: FROZEN_VALIDATED
Contract version: 0.1

## Purpose

I-5 defines the production embedding service boundary that
orchestrates the canonical AM-PKO embedding pipeline without
coupling the ontology to a specific embedding model or storage
technology.

## Canonical flow

KnowledgeRecord
→ I-2 EmbeddingDocumentGenerator
→ T-2 EmbeddingDocument
→ I-5 EmbeddingService
→ I-3 EmbeddingModel
→ embedding vector
→ I-4 EmbeddingStore

## Interface

`embedding/service_interface.py`

### EmbeddingRequest

Contains exactly one field:

- `document: EmbeddingDocument`

The service does not accept arbitrary raw text as its canonical
request input.

### EmbeddingResponse

Contains:

- `record_id`
- `record_version`
- `embedding_spec_version`
- `model_id`
- `dimension`
- `vector`

## Service methods

### embed(request)

Embeds one canonical I-2 `EmbeddingDocument` through the I-3
`EmbeddingModel` boundary.

### health_check()

Reports whether the embedding service is operational.

## Architectural boundaries

I-5 does not:

- generate EmbeddingDocuments
- define embedding-document formatting
- select the production embedding model
- implement model-specific runtime behavior
- define persistent vector storage
- perform vector retrieval
- define a vector database
- alter canonical knowledge content

I-5 preserves the independence of:

- I-2 EmbeddingDocument generation
- I-3 model execution
- I-4 vector storage and retrieval

## Validation

Structural validation: PASS

Python syntax validation: PASS

Import validation: PASS

I-5/I-4 responsibility separation: PASS

I-5 type contract validation: PASS

## Production status

This manifest freezes the I-5 service contract only.

No production embedding service implementation or deployment
technology is selected by I-5.

Production model selection remains governed by the separate
embedding model-selection framework and decision record.
