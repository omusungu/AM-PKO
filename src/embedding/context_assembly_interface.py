from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Mapping, Sequence

from .admissibility import AuthorityEvaluator
from .context_package import ContextPackage
from .retrieval_interface import QueryRequest
from .retrieval_result import RankedResult


class ContextAssembler(ABC):
    """
    AM-PKO I-8 — deterministic Context Assembly boundary.

    I-8 consumes frozen retrieval outputs, the current retrieval request,
    declared assembly context, and an injected authority/admissibility
    evaluator, then produces T-8 ContextPackage.

    I-8 does not define authority semantics itself.
    """

    @abstractmethod
    def assemble(
        self,
        candidates: Sequence[RankedResult],
        request: QueryRequest,
        *,
        context: Mapping[str, Any],
        authority_evaluator: AuthorityEvaluator,
    ) -> ContextPackage:
        """
        Compile eligible candidates and explicit structural context
        into a deterministic T-8 ContextPackage.
        """
        raise NotImplementedError
