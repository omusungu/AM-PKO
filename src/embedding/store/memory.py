from __future__ import annotations

import math
from collections.abc import Mapping, Sequence

from .errors import (
    InvalidSearch,
    InvalidVector,
    VectorAlreadyExists,
    VectorNotFound,
)
from .interface import (
    EmbeddingStore,
    VectorIdentity,
    VectorRecord,
)
from .payload import validate_vector_record
from .match import VectorStoreMatch


class InMemoryEmbeddingStore(EmbeddingStore):
    """
    I-4 reference implementation.

    This implementation is intentionally storage-engine independent.
    It exists to validate the I-4 contract before selecting persistent
    storage technology.
    """

    def __init__(self) -> None:
        self._records: dict[VectorIdentity, VectorRecord] = {}

    def add(self, vector_record: VectorRecord) -> None:
        try:
            validate_vector_record(vector_record)
        except (TypeError, ValueError) as exc:
            raise InvalidVector(str(exc)) from exc

        identity = vector_record.identity

        if identity in self._records:
            raise VectorAlreadyExists(
                f"Vector already exists: {identity}"
            )

        self._records[identity] = vector_record

    def get(self, identity: VectorIdentity) -> VectorRecord:
        try:
            return self._records[identity]
        except KeyError as exc:
            raise VectorNotFound(
                f"Vector not found: {identity}"
            ) from exc

    def delete(self, identity: VectorIdentity) -> None:
        if identity not in self._records:
            raise VectorNotFound(
                f"Vector not found: {identity}"
            )

        del self._records[identity]

    def search(
        self,
        query_vector: Sequence[float],
        *,
        k: int,
        filters: Mapping[str, Sequence[str]] | None = None,
        include_excluded: bool = False,
    ) -> list[VectorStoreMatch]:
        if k <= 0:
            raise InvalidSearch("k must be greater than zero")
        if filters is not None and not isinstance(filters, Mapping):
            raise InvalidSearch("filters must be a mapping or None")

        if not query_vector:
            raise InvalidSearch("query_vector cannot be empty")

        try:
            query = tuple(float(value) for value in query_vector)
        except (TypeError, ValueError) as exc:
            raise InvalidSearch(
                "query_vector must contain numeric values"
            ) from exc

        query_norm = math.sqrt(sum(value * value for value in query))

        if query_norm == 0.0:
            raise InvalidSearch("query_vector cannot have zero norm")

        candidates: list[tuple[float, VectorRecord]] = []

        for record in self._records.values():
            if record.dimension != len(query):
                continue

            if not include_excluded and bool(
                record.payload.get("excluded", False)
            ):
                continue

            if not self._matches_filters(record, filters):
                continue

            vector = tuple(float(value) for value in record.vector)
            vector_norm = math.sqrt(
                sum(value * value for value in vector)
            )

            if vector_norm == 0.0:
                continue

            score = sum(
                query_value * vector_value
                for query_value, vector_value in zip(query, vector)
            ) / (query_norm * vector_norm)

            candidates.append((score, record))

        candidates.sort(
            key=lambda item: (
                -item[0],
                item[1].identity.record_id,
                item[1].identity.embedding_model_id,
            )
        )

        return [
            VectorStoreMatch(record=record, score=score)
            for score, record in candidates[:k]
        ]

    @staticmethod
    def _matches_filters(
        record: VectorRecord,
        filters: Mapping[str, Sequence[str]] | None,
    ) -> bool:
        if not filters:
            return True

        for field, accepted_values in filters.items():
            if field not in record.payload:
                return False

            value = record.payload[field]

            if isinstance(value, (list, tuple)):
                if not any(
                    item in accepted_values
                    for item in value
                ):
                    return False
            elif value not in accepted_values:
                return False

        return True

    def count(self) -> int:
        return len(self._records)

    def health_check(self) -> bool:
        return True
