from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Sequence

from .document_interface import EmbeddingDocument


@dataclass(frozen=True)
class EmbeddingRequest:
    document: EmbeddingDocument


@dataclass(frozen=True)
class EmbeddingResponse:
    record_id: str
    record_version: str
    embedding_spec_version: str
    model_id: str
    dimension: int
    vector: Sequence[float]


class EmbeddingService(ABC):
    """AM-PKO I-5 production embedding service contract."""

    @abstractmethod
    def embed(self, request: EmbeddingRequest) -> EmbeddingResponse:
        """Embed one canonical I-2 EmbeddingDocument."""
        raise NotImplementedError

    @abstractmethod
    def health_check(self) -> bool:
        """Report whether the embedding service is operational."""
        raise NotImplementedError
