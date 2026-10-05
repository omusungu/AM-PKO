from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence


@dataclass(frozen=True)
class ContextPackage:
    """
    AM-PKO T-8 — deterministic ContextPackage.

    T-8 represents the result of I-8 Context Assembly. It packages
    authoritative/admissible knowledge and explicit relationship
    structure without creating or establishing epistemic authority.
    """

    context_id: str
    compiled_records: Sequence[Mapping[str, Any]]
    provenance_map: Mapping[str, Any]
    active_relationship_subgraph: Sequence[Mapping[str, Any]]
    epistemic_validation_summary: Mapping[str, Any]
    budget_utilization: Mapping[str, Any]

    def __post_init__(self) -> None:
        if not isinstance(self.context_id, str):
            raise TypeError("context_id must be a string")

        if not self.context_id.strip():
            raise ValueError("context_id must not be empty")

        if not isinstance(self.compiled_records, Sequence) or isinstance(
            self.compiled_records, (str, bytes)
        ):
            raise TypeError("compiled_records must be a sequence")

        for record in self.compiled_records:
            if not isinstance(record, Mapping):
                raise TypeError("each compiled record must be a mapping")

        if not isinstance(self.provenance_map, Mapping):
            raise TypeError("provenance_map must be a mapping")

        if not isinstance(
            self.active_relationship_subgraph, Sequence
        ) or isinstance(self.active_relationship_subgraph, (str, bytes)):
            raise TypeError(
                "active_relationship_subgraph must be a sequence"
            )

        for relationship in self.active_relationship_subgraph:
            if not isinstance(relationship, Mapping):
                raise TypeError(
                    "each relationship must be a mapping"
                )

        if not isinstance(self.epistemic_validation_summary, Mapping):
            raise TypeError(
                "epistemic_validation_summary must be a mapping"
            )

        if not isinstance(self.budget_utilization, Mapping):
            raise TypeError("budget_utilization must be a mapping")
