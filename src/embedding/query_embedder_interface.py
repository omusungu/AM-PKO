from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Sequence


class QueryEmbedder(ABC):
    """
    AM-PKO — query-embedding capability consumed by I-6.

    This boundary exposes only query embedding. It does not define
    model identity, vector storage, ranking, filtering, or evaluation.
    """

    @abstractmethod
    def embed_query(self, text: str) -> Sequence[float]:
        raise NotImplementedError
