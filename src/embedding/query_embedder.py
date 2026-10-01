from __future__ import annotations

from typing import Sequence

from .adapters.llama_cpp.adapter import LlamaCppEmbeddingAdapter
from .query_embedder_interface import QueryEmbedder


class LlamaCppQueryEmbedder(QueryEmbedder):
    """
    Reference bridge from the concrete llama.cpp adapter to the
    model-agnostic I-6 QueryEmbedder capability.

    The bridge delegates query embedding without reproducing or
    modifying adapter-specific query-prefix behavior.
    """

    def __init__(self, adapter: LlamaCppEmbeddingAdapter) -> None:
        self._adapter = adapter

    def embed_query(self, text: str) -> Sequence[float]:
        return self._adapter.embed_query(text)
