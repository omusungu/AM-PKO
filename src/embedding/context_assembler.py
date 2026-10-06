from __future__ import annotations

from typing import Any, Mapping, Sequence

from .admissibility import AdmissibilityState, AuthorityEvaluator
from .context_assembly_interface import ContextAssembler
from .context_package import ContextPackage
from .knowledge_record_resolver import KnowledgeRecordResolver
from .retrieval_interface import QueryRequest
from .retrieval_result import RankedResult


class DeterministicContextAssembler(ContextAssembler):
    """
    AM-PKO I-8 — minimal deterministic Context Assembly implementation.

    This implementation establishes the authority/admissibility filtering
    boundary only. Relationship traversal, provenance expansion, and
    resource-budget enforcement remain explicit future implementation
    boundaries and are not inferred here.
    """

    def assemble(
        self,
        candidates: Sequence[RankedResult],
        request: QueryRequest,
        *,
        context: Mapping[str, Any],
        authority_evaluator: AuthorityEvaluator,
        record_resolver: KnowledgeRecordResolver,
    ) -> ContextPackage:
        if not isinstance(candidates, Sequence) or isinstance(
            candidates, (str, bytes)
        ):
            raise TypeError("candidates must be a sequence")

        if not isinstance(request, QueryRequest):
            raise TypeError("request must be a QueryRequest")

        if not isinstance(context, Mapping):
            raise TypeError("context must be a mapping")

        if not isinstance(authority_evaluator, AuthorityEvaluator):
            raise TypeError(
                "authority_evaluator must be an AuthorityEvaluator"
            )

        if not isinstance(record_resolver, KnowledgeRecordResolver):
            raise TypeError(
                "record_resolver must be a KnowledgeRecordResolver"
            )

        compiled_records: list[Mapping[str, Any]] = []
        excluded: list[Mapping[str, Any]] = []

        for candidate in candidates:
            if not isinstance(candidate, RankedResult):
                raise TypeError("each candidate must be a RankedResult")

            record = record_resolver.resolve(candidate.record_id)
            if not isinstance(record, Mapping):
                raise TypeError("resolved KnowledgeRecord must be a mapping")
            if record.get("id") != candidate.record_id:
                raise ValueError(
                    "resolved KnowledgeRecord id does not match candidate record_id"
                )
            evaluation = authority_evaluator.evaluate(
                record,
                context=context,
            )

            entry = {
                "record_id": candidate.record_id,
                "score": candidate.score,
                "state": evaluation.state.value,
                "reason": evaluation.reason,
            }

            if evaluation.state is AdmissibilityState.ADMISSIBLE:
                compiled_records.append(record)
            else:
                excluded.append(entry)

        return ContextPackage(
            context_id=str(context.get("context_id", "I8-CONTEXT-UNSPECIFIED")),
            compiled_records=tuple(compiled_records),
            provenance_map={},
            active_relationship_subgraph=(),
            epistemic_validation_summary={
                "included": tuple(
                    {
                        "record_id": record["id"],
                        "status": "INCLUDED",
                    }
                    for record in compiled_records
                ),
                "excluded": tuple(excluded),
            },
            budget_utilization={},
        )
