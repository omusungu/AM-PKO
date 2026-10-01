from dataclasses import dataclass
from types import MappingProxyType

from science.units import Unit


@dataclass(frozen=True)
class CompoundUnit:
    """
    Represents a product of units raised to integer powers.

    Example:
        m/s → {metre: 1, second: -1}
    """

    factors: MappingProxyType

    @property
    def dimension(self):
        """
        Calculate the resulting physical dimension from all factors.
        """

        dimension = None

        for unit, exponent in self.factors.items():
            unit_dimension = unit.dimension ** exponent

            if dimension is None:
                dimension = unit_dimension
            else:
                dimension = dimension * unit_dimension

        if dimension is None:
            from science.dimensions import Dimension
            return Dimension()

        return dimension

    @property
    def scale(self) -> float:
        """
        Calculate the combined scale relative to SI base units.
        """

        scale = 1.0

        for unit, exponent in self.factors.items():
            scale *= unit.scale ** exponent

        return scale

    def __str__(self) -> str:
        numerator = []
        denominator = []

        for unit, exponent in self.factors.items():
            if exponent > 0:
                numerator.append(
                    unit.symbol if exponent == 1
                    else f"{unit.symbol}^{exponent}"
                )
            elif exponent < 0:
                power = -exponent
                denominator.append(
                    unit.symbol if power == 1
                    else f"{unit.symbol}^{power}"
                )

        if not numerator:
            numerator.append("1")

        result = "*".join(numerator)

        if denominator:
            result += "/" + "*".join(denominator)

        return result
