from __future__ import annotations

from abc import abstractmethod
from typing import Sequence

from embedding.model_interface import EmbeddingModel, InputTooLong


class CheckpointEmbeddingAdapter(EmbeddingModel):
    """
    Base adapter for one pinned embedding checkpoint.

    Concrete adapters provide the runtime-specific implementation
    while AM-PKO depends only on the I-3 EmbeddingModel contract.
    """

    @abstractmethod
    def _count_tokens(self, text: str) -> int:
        """Return the exact token count used by the checkpoint runtime."""

    @abstractmethod
    def _embed_text(self, text: str) -> Sequence[float]:
        """Run the concrete checkpoint and return its vector."""

    def token_count(self, text: str) -> int:
        count = self._count_tokens(text)

        if count < 0:
            raise ValueError("Token count cannot be negative")

        return count

    def embed(self, text: str) -> Sequence[float]:
        count = self.token_count(text)

        if count > self.max_input_tokens():
            raise InputTooLong(
                f"Input has {count} tokens; "
                f"maximum is {self.max_input_tokens()}"
            )

        vector = self._embed_text(text)

        if len(vector) != self.dimension():
            raise ValueError(
                f"Embedding dimension mismatch: "
                f"expected {self.dimension()}, got {len(vector)}"
            )

        return vector
