from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LlamaCppEmbeddingConfig:
    """Immutable runtime configuration for one pinned llama.cpp adapter."""

    executable: str
    model_path: str
    model_id: str
    model_family: str
    dimension: int
    max_input_tokens: int
    pooling: str | None
    normalize: int
    context_size: int
    threads: int
    separator: str
    query_prefix: str
    document_prefix: str
