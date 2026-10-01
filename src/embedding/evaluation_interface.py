from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence


@dataclass(frozen=True)
class EvaluationRun:
    """
    AM-PKO T-7 — one reproducible retrieval evaluation run.

    T-7 belongs to the evaluation boundary and does not participate
    in runtime retrieval.
    """

    evaluation_id: str
    experiment_id: str
    model_id: str
    model_family: str
    judgment_scale: Mapping[str, Any]
    per_query: Sequence[Mapping[str, Any]]
    metrics: Mapping[str, float]
