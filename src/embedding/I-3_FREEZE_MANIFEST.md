# AM-PKO I-3 — EmbeddingModel Adapter Layer

Status: FROZEN_VALIDATED
Contract version: 0.1

## Canonical interface

`embedding/model_interface.py`

Defines the model-agnostic `EmbeddingModel` interface:

- `model_id()`
- `model_family()`
- `dimension()`
- `max_input_tokens()`
- `token_count(text)`
- `embed(text)`

## Adapter boundary

`embedding/adapters/base.py`

Defines the checkpoint adapter boundary used by concrete runtime adapters.

## Runtime adapter

`embedding/adapters/llama_cpp/adapter.py`

Supports pinned embedding checkpoints executed through llama.cpp
`llama-embedding`.

Validated candidates:

- BGE-M3
- multilingual E5-large
- Qwen3-Embedding-0.6B

The ontology and I-3 interface remain model-agnostic.

## Runtime configuration

`embedding/adapters/llama_cpp/config.py`

Configuration is immutable and supports:

- checkpoint provenance
- model identity
- dimension
- token limit
- pooling mode, including model-default (`None`)
- normalization
- context size
- thread count
- separator
- query prefix
- document prefix

## Safety and integrity properties

- Input token limits fail closed with `InputTooLong`.
- Embedding output dimension is validated.
- Empty embedding output fails closed.
- Non-numeric embedding output fails closed.
- Raw embedding output is explicitly requested.
- Embedding sequence separation is explicitly controlled.
- No vector caching is implemented.
- Model identity is supplied explicitly by the adapter configuration.

## Validation record

Structural validation:
PASS

Python syntax validation:
PASS

BGE-M3 real adapter validation:
PASS

E5 real adapter validation:
PASS

Qwen3 real adapter validation:
PASS

Checkpoint provenance validation:
PASS

Three-candidate adapter instantiation:
PASS

Qwen model-default pooling validation:
PASS

Fail-closed parser validation:
PASS

## Note on three-model regression

A combined BGE-M3/E5/Qwen regression was started after parser hardening.
BGE-M3 and E5 completed successfully. The Qwen subprocess was still
running when the test was manually interrupted.

This interrupted run is not treated as a failed model validation because
the standalone Qwen real-adapter regression had already passed.

## Architectural boundary

I-3 provides:

KnowledgeRecord-independent embedding model execution through the
canonical `EmbeddingModel` interface.

I-3 does not define:

- KnowledgeRecord schema
- EmbeddingDocument generation
- vector storage
- retrieval
- ranking
- graph relationships
- model selection
- RAG synthesis

## Freeze decision

I-3 adapter layer is frozen as a validated implementation boundary.

No candidate model is selected as the production embedding model by I-3.
Model selection remains an evaluation concern outside the interface contract.

Status: FROZEN_VALIDATED
