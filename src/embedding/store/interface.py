from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from .match import VectorStoreMatch


@dataclass(frozen=True)
class VectorIdentity:
    """Immutable T-3 vector identity."""

    record_id: str
    embedding_spec_version: str
    embedding_model_id: str
    record_version: str


@dataclass(frozen=True)
class VectorRecord:
    """
    AM-PKO T-3 — canonical vector record.

    The vector and its payload are inseparable at the I-4 boundary.
    """

    identity: VectorIdentity
    dimension: int
    vector: Sequence[float]
    payload: Mapping[str, Any]


class EmbeddingStore(ABC):
    """
    AM-PKO I-4 — storage interface for canonical VectorRecords.

    Implementations must remain independent of the underlying
    storage engine.
    """

    @abstractmethod
    def add(self, vector_record: VectorRecord) -> None:
        """Add one vector record."""

    @abstractmethod
    def get(self, identity: VectorIdentity) -> VectorRecord:
        """Retrieve one vector record by immutable identity."""

    @abstractmethod
    def delete(self, identity: VectorIdentity) -> None:
        """Delete one vector record without affecting the canonical record."""

    @abstractmethod
    def search(
        self,
        query_vector: Sequence[float],
        *,
        k: int,
        filters: Mapping[str, Sequence[str]] | None = None,
        include_excluded: bool = False,
    ) -> list[VectorStoreMatch]:
        """Search vectors and return ordered records with retrieval scores."""

    @abstractmethod
    def count(self) -> int:
        """Return the number of stored vector records."""

    @abstractmethod
    def health_check(self) -> bool:
        """Return whether the store is healthy and usable."""
