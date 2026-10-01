from dataclasses import dataclass

from science.conversions import convert_quantity
from science.units import (
    Unit,
    CompoundUnit,
    multiply_units,
    divide_units,
    power_unit,
)


@dataclass(frozen=True)
class Quantity:
    """
    A numerical physical quantity paired with a unit expression.

    The unit expression carries physical dimension and scale.
    """

    value: float
    unit: Unit | CompoundUnit

    @property
    def dimension(self):
        return self.unit.dimension

    @property
    def scale(self) -> float:
        return self.unit.scale

    def _require_compatible(self, other: "Quantity") -> None:
        if not isinstance(other, Quantity):
            raise TypeError("Quantity operations require another Quantity.")

        if self.dimension != other.dimension:
            raise ValueError(
                f"Incompatible dimensions: "
                f"{self.dimension} and {other.dimension}"
            )

    def to(self, target_unit) -> "Quantity":
        """
        Convert this quantity to a dimensionally compatible target unit.
        """

        return convert_quantity(self, target_unit)

    def __add__(self, other: "Quantity") -> "Quantity":
        self._require_compatible(other)

        other_converted = other.to(self.unit)

        return Quantity(
            value=self.value + other_converted.value,
            unit=self.unit,
        )

    def __sub__(self, other: "Quantity") -> "Quantity":
        self._require_compatible(other)

        other_converted = other.to(self.unit)

        return Quantity(
            value=self.value - other_converted.value,
            unit=self.unit,
        )

    def __mul__(self, other: "Quantity") -> "Quantity":
        if not isinstance(other, Quantity):
            raise TypeError(
                "Quantity multiplication requires another Quantity."
            )

        unit = multiply_units(self.unit, other.unit)

        return Quantity(
            value=self.value * other.value,
            unit=unit,
        )

    def __truediv__(self, other: "Quantity") -> "Quantity":
        if not isinstance(other, Quantity):
            raise TypeError(
                "Quantity division requires another Quantity."
            )

        if other.value == 0:
            raise ZeroDivisionError("Cannot divide a quantity by zero.")

        unit = divide_units(self.unit, other.unit)

        return Quantity(
            value=self.value / other.value,
            unit=unit,
        )

    def __pow__(self, power: int) -> "Quantity":
        if not isinstance(power, int):
            raise TypeError("Quantity powers must be integers.")

        return Quantity(
            value=self.value ** power,
            unit=power_unit(self.unit, power),
        )

    def __str__(self) -> str:
        return f"{self.value} {self.unit}"
