from dataclasses import dataclass
from typing import Literal


OperationType = Literal[
    "multiply",
    "divide",
    "power",
]


@dataclass(frozen=True)
class FormulaOperation:
    """
    Represents one controlled operation in a formula.

    No Python expression is evaluated from this structure.
    """

    operation: OperationType
    operands: tuple[str, ...]
    power: int | None = None

    def __post_init__(self) -> None:
        if self.operation not in {"multiply", "divide", "power"}:
            raise ValueError(
                f"Unsupported formula operation: {self.operation}"
            )

        if not self.operands:
            raise ValueError(
                "Formula operation must have at least one operand."
            )

        if self.operation == "power":
            if len(self.operands) != 1:
                raise ValueError(
                    "Power operation requires exactly one operand."
                )

            if self.power is None:
                raise ValueError(
                    "Power operation requires an integer power."
                )

            if not isinstance(self.power, int):
                raise TypeError(
                    "Formula powers must be integers."
                )

        elif self.power is not None:
            raise ValueError(
                "Power is only valid for power operations."
            )
