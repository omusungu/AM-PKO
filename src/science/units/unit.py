from dataclasses import dataclass

from science.dimensions import Dimension


@dataclass(frozen=True)
class Unit:
    """
    Represents a physical unit.

    scale converts the unit to its corresponding SI base-unit scale.
    offset is reserved for affine temperature conversions.
    """

    name: str
    symbol: str
    dimension: Dimension
    scale: float = 1.0
    offset: float = 0.0

    def __str__(self) -> str:
        return self.symbol
