from types import MappingProxyType

from science.units import Unit
from science.units.compound import CompoundUnit


def multiply_units(
    left: Unit | CompoundUnit,
    right: Unit | CompoundUnit,
) -> CompoundUnit:
    """
    Multiply two units and combine their factor exponents.

    Zero exponents are removed so equivalent factors cancel.
    """

    factors: dict[Unit, int] = {}

    def add_factors(unit_expression: Unit | CompoundUnit) -> None:
        if isinstance(unit_expression, Unit):
            factors[unit_expression] = factors.get(unit_expression, 0) + 1
            return

        for unit, exponent in unit_expression.factors.items():
            factors[unit] = factors.get(unit, 0) + exponent

    add_factors(left)
    add_factors(right)

    factors = {
        unit: exponent
        for unit, exponent in factors.items()
        if exponent != 0
    }

    return CompoundUnit(MappingProxyType(factors))


def divide_units(
    left: Unit | CompoundUnit,
    right: Unit | CompoundUnit,
) -> CompoundUnit:
    """
    Divide two units and combine their factor exponents.

    Factors from the right-hand unit are subtracted.
    Zero exponents are removed automatically.
    """

    factors: dict[Unit, int] = {}

    def add_factors(
        unit_expression: Unit | CompoundUnit,
        multiplier: int,
    ) -> None:
        if isinstance(unit_expression, Unit):
            factors[unit_expression] = (
                factors.get(unit_expression, 0) + multiplier
            )
            return

        for unit, exponent in unit_expression.factors.items():
            factors[unit] = (
                factors.get(unit, 0) + multiplier * exponent
            )

    add_factors(left, 1)
    add_factors(right, -1)

    factors = {
        unit: exponent
        for unit, exponent in factors.items()
        if exponent != 0
    }

    return CompoundUnit(MappingProxyType(factors))


def power_unit(
    unit_expression: Unit | CompoundUnit,
    power: int,
) -> CompoundUnit:
    """
    Raise a unit expression to an integer power.

    Example:
        m^2
        (m/s)^2 -> m^2/s^2
        (m/s)^0 -> 1
    """

    if not isinstance(power, int):
        raise TypeError("Unit powers must be integers.")

    if isinstance(unit_expression, Unit):
        factors = {
            unit_expression: power,
        }
    else:
        factors = {
            unit: exponent * power
            for unit, exponent in unit_expression.factors.items()
        }

    factors = {
        unit: exponent
        for unit, exponent in factors.items()
        if exponent != 0
    }

    return CompoundUnit(MappingProxyType(factors))
