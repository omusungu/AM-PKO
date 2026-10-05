from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Any, Mapping


class AdmissibilityState(str, Enum):
    """AM-PKO three-valued admissibility outcome."""

    ADMISSIBLE = "ADMISSIBLE"
    INADMISSIBLE = "INADMISSIBLE"
    UNDETERMINED = "UNDETERMINED"


@dataclass(frozen=True)
class AdmissibilityResult:
    """
    Immutable result of an authority/admissibility evaluation.

    UNDETERMINED remains an explicit epistemic state. Execution and
    compilation must fail closed on it; I-8 does not reinterpret it.
    """

    record_id: str
    state: AdmissibilityState
    reason: str
    evidence: Mapping[str, Any]

    def __post_init__(self) -> None:
        if not isinstance(self.record_id, str):
            raise TypeError("record_id must be a string")

        if not self.record_id.strip():
            raise ValueError("record_id must not be empty")

        if not isinstance(self.state, AdmissibilityState):
            raise TypeError(
                "state must be an AdmissibilityState"
            )

        if not isinstance(self.reason, str):
            raise TypeError("reason must be a string")

        if not isinstance(self.evidence, Mapping):
            raise TypeError("evidence must be a mapping")


class AuthorityEvaluator(ABC):
    """
    AM-PKO authority/admissibility evaluation boundary.

    Implementations own the evaluation semantics. I-8 consumes the
    resulting decision and must not independently establish authority.
    """

    @abstractmethod
    def evaluate(
        self,
        record: Mapping[str, Any],
        *,
        context: Mapping[str, Any],
    ) -> AdmissibilityResult:
        """
        Evaluate one candidate against the active authority policy
        and structured assembly context.
        """
        raise NotImplementedError
