from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Sequence


class EmbeddingError(Exception):
    """Base error for I-3 embedding operations."""


class InputTooLong(EmbeddingError):
    """Raised when input exceeds the model's declared token limit."""


class InvalidEmbedding(EmbeddingError):
    """Raised when a model returns an invalid embedding."""


@dataclass(frozen=True)
class ModelIdentity:
    """Immutable identity of one exact embedding checkpoint."""

    model_id: str
    model_family: str
    dimension: int
    max_input_tokens: int


class EmbeddingModel(ABC):
    """
    AM-PKO I-3 — model-agnostic embedding interface.

    Implementations must represent one pinned checkpoint for the
    lifetime of the instance.
    """

    @abstractmethod
    def model_id(self) -> str:
        """Return the exact pinned checkpoint identifier."""

    @abstractmethod
    def model_family(self) -> str:
        """Return the model family identifier."""

    @abstractmethod
    def dimension(self) -> int:
        """Return the declared embedding dimension."""

    @abstractmethod
    def max_input_tokens(self) -> int:
        """Return the maximum accepted input-token count."""

    @abstractmethod
    def token_count(self, text: str) -> int:
        """Return the model-specific token count for text."""

    @abstractmethod
    def embed(self, text: str) -> Sequence[float]:
        """
        Embed text into a vector.

        Implementations must raise InputTooLong when the declared
        input limit is exceeded.
        """

    def identity(self) -> ModelIdentity:
        """Return the complete immutable checkpoint identity."""
        return ModelIdentity(
            model_id=self.model_id(),
            model_family=self.model_family(),
            dimension=self.dimension(),
            max_input_tokens=self.max_input_tokens(),
        )
