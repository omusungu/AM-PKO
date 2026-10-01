from dataclasses import dataclass

from science.dimensions import Dimension
from science.formulas.operations import FormulaOperation
from science.formulas.source import FormulaSource


@dataclass(frozen=True)
class Formula:
    """
    Represents a scientific formula definition.

    A formula contains its identity, variables, dimensional contract,
    and a controlled operation describing how the output is derived.
    Numerical evaluation is handled separately.
    """

    name: str
    symbol: str
    variables: tuple[str, ...]
    output: str
    dimensions: dict[str, Dimension]
    operation: FormulaOperation
    expression: str = ""
    description: str = ""
    source: str = ""
    provenance: FormulaSource | None = None

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("Formula name cannot be empty.")

        if not self.symbol:
            raise ValueError("Formula symbol cannot be empty.")

        if not self.variables:
            raise ValueError("Formula must define at least one variable.")

        if self.provenance is not None and not isinstance(
            self.provenance,
            FormulaSource,
        ):
            raise TypeError(
                "Formula provenance must be a FormulaSource or None."
            )

        if self.output not in self.variables:
            raise ValueError(
                "Formula output must be one of the declared variables."
            )

        missing = set(self.variables) - set(self.dimensions)

        if missing:
            raise ValueError(
                f"Missing dimensions for variables: "
                f"{', '.join(sorted(missing))}"
            )

        unexpected = set(self.dimensions) - set(self.variables)

        if unexpected:
            raise ValueError(
                f"Dimensions provided for undeclared variables: "
                f"{', '.join(sorted(unexpected))}"
            )

        missing_operands = (
            set(self.operation.operands) - set(self.variables)
        )

        if missing_operands:
            raise ValueError(
                f"Operation references undeclared variables: "
                f"{', '.join(sorted(missing_operands))}"
            )

    @property
    def output_dimension(self) -> Dimension:
        return self.dimensions[self.output]

    def __str__(self) -> str:
        return f"{self.symbol}: {self.expression}"
