from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence


@dataclass(frozen=True)
class QueryRequest:
    """
    AM-PKO T-5 — semantic retrieval request.

    This contract carries retrieval intent only.
    It does not generate embeddings or execute vector search.
    """

    query: str
    k: int
    filters: Mapping[str, Sequence[str]] | None = None
    include_excluded: bool = False

    def __post_init__(self) -> None:
        if not isinstance(self.query, str):
            raise TypeError("query must be a string")

        if not self.query.strip():
            raise ValueError("query must not be empty")

        if not isinstance(self.k, int) or isinstance(self.k, bool):
            raise TypeError("k must be an integer")

        if self.k <= 0:
            raise ValueError("k must be greater than zero")

        if self.filters is not None and not isinstance(self.filters, Mapping):
            raise TypeError("filters must be a mapping or None")

        if not isinstance(self.include_excluded, bool):
            raise TypeError("include_excluded must be a boolean")
