# I-5 Reference Embedding Service Validation

Status: VALIDATED

## Implementation

`src/embedding/services/reference.py`

Implementation class:

`ReferenceEmbeddingService`

## Dependency boundary

The service receives an injected I-3 `EmbeddingModel`.

It does not construct or select a model implementation.

## Canonical input

The service accepts:

`EmbeddingRequest(document: EmbeddingDocument)`

It does not accept arbitrary raw text through the I-5 request contract.

## Data flow

`I-2 EmbeddingDocument`
→ `I-5 EmbeddingRequest`
→ `I-5 ReferenceEmbeddingService`
→ `I-3 EmbeddingModel.embed(document.document_text)`
→ `I-5 EmbeddingResponse`

## Preserved identity

The response preserves:

- `record_id`
- `record_version`
- `embedding_spec_version`

The response additionally records:

- `model_id`
- `dimension`
- `vector`

## Responsibility boundaries

I-5 does not:

- generate EmbeddingDocuments
- define canonical document formatting
- select an embedding model
- implement model-specific runtime behavior
- perform retrieval
- perform vector storage
- define a vector database

## Validation results

Structural validation: PASS

Python syntax validation: PASS

I-5 subclass validation: PASS

Abstract method implementation validation: PASS

Dependency injection validation: PASS

End-to-end fake-model data-flow validation: PASS

Canonical document boundary validation: PASS

Retrieval/storage responsibility separation: PASS

## Production status

This is a reference implementation used to validate the frozen I-5 contract.

No production embedding model or deployment technology is selected by this implementation.

Production model selection remains governed by:

`EMBEDDING-MODEL-SELECTION-001`

and

`EMBEDDING-MODEL-DECISION-001`
