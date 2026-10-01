from dataclasses import dataclass


@dataclass(frozen=True)
class Prefix:
    """
    Represents an SI decimal prefix.

    factor is the multiplier applied to the underlying unit.
    """

    name: str
    symbol: str
    factor: float

    def __str__(self) -> str:
        return self.symbol
