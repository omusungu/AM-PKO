from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Mapping, Any

from .service_interface import EmbeddingResponse
from .store.interface import VectorRecord


class VectorRecordMapper(ABC):
    """AM-PKO boundary for mapping source records and embeddings to T-3."""

    @abstractmethod
    def map(
        self,
        record: Mapping[str, Any],
        embedding: EmbeddingResponse,
    ) -> VectorRecord:
        """Construct one validated canonical T-3 VectorRecord."""
        raise NotImplementedError
