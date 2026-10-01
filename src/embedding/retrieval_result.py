from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RankedResult:
    """
    AM-PKO T-6 — one ranked semantic-retrieval match.

    The retrieval score is produced by the I-4 vector-search
    boundary. T-6 does not recompute or reorder results.
    """

    record_id: str
    score: float

    def __post_init__(self) -> None:
        if not isinstance(self.record_id, str):
            raise TypeError("record_id must be a string")

        if not self.record_id.strip():
            raise ValueError("record_id must not be empty")

        if not isinstance(self.score, (int, float)) or isinstance(self.score, bool):
            raise TypeError("score must be numeric")

        if not isinstance(self.score, float):
            object.__setattr__(self, "score", float(self.score))

        if self.score != self.score:
            raise ValueError("score must not be NaN")
