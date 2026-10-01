from __future__ import annotations

from dataclasses import dataclass
import math

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .interface import VectorRecord


@dataclass(frozen=True)
class VectorStoreMatch:
    """
    Transient I-4 retrieval match.

    Associates one immutable VectorRecord with the retrieval score
    produced by the I-4 search operation.
    """

    record: VectorRecord
    score: float

    def __post_init__(self) -> None:
        from .interface import VectorRecord

        if not isinstance(self.record, VectorRecord):
            raise TypeError("record must be a VectorRecord")

        if not isinstance(self.score, (int, float)) or isinstance(
            self.score, bool
        ):
            raise TypeError("score must be numeric")

        score = float(self.score)

        if math.isnan(score):
            raise ValueError("score must not be NaN")

        object.__setattr__(self, "score", score)
