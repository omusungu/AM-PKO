from dataclasses import dataclass

from science.units import Unit, CompoundUnit


@dataclass(frozen=True)
class Constant:
    """
    Represents a named scientific constant with a physical unit.

    The value is stored numerically while the unit preserves
    its physical meaning.
    """

    name: str
    symbol: str
    value: float
    unit: Unit | CompoundUnit
    description: str = ""
    source: str = ""

    def __str__(self) -> str:
        return f"{self.symbol} = {self.value} {self.unit}"
