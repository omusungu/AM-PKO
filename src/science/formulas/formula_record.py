from dataclasses import dataclass

from science.formulas.formula import Formula


@dataclass(frozen=True)
class FormulaRecord:
    """
    Knowledge-oriented projection of a scientific Formula.

    This is deliberately separate from the AM-PKO KnowledgeRecord schema.
    It provides a stable bridge without coupling the science layer to
    knowledge storage or retrieval infrastructure.
    """

    id: str
    domain: str
    knowledge_type: str
    topic: str
    granularity: str
    status: str
    title: str
    symbol: str
    expression: str
    description: str
    variables: tuple[str, ...]
    output: str
    source: str
    provenance: object | None = None

    @classmethod
    def from_formula(
        cls,
        formula: Formula,
        record_id: str,
    ) -> "FormulaRecord":
        if not isinstance(formula, Formula):
            raise TypeError(
                "FormulaRecord requires a Formula instance."
            )

        if not record_id:
            raise ValueError(
                "FormulaRecord requires a non-empty record ID."
            )

        return cls(
            id=record_id,
            domain="Science",
            knowledge_type="FACT",
            topic="Scientific Formula",
            granularity="Principle",
            status="VALIDATED",
            title=formula.name,
            symbol=formula.symbol,
            expression=formula.expression,
            description=formula.description,
            variables=formula.variables,
            output=formula.output,
            source=formula.source,
            provenance=formula.provenance,
        )
