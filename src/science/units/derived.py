from science.dimensions import Dimension
from science.units.unit import Unit
from science.units.si import (
    SECOND,
    METRE,
    KILOGRAM,
    AMPERE,
    CANDELA,
)


# Fundamental dimensions used to construct derived units.
TIME = SECOND.dimension
LENGTH = METRE.dimension
MASS = KILOGRAM.dimension


# Derived SI units

STERADIAN = Unit(
    name="steradian",
    symbol="sr",
    dimension=Dimension(),
)

LUMEN = Unit(
    name="lumen",
    symbol="lm",
    dimension=CANDELA.dimension,
)

HERTZ = Unit(
    name="hertz",
    symbol="Hz",
    dimension=TIME ** -1,
)

NEWTON = Unit(
    name="newton",
    symbol="N",
    dimension=MASS * LENGTH / (TIME ** 2),
)

PASCAL = Unit(
    name="pascal",
    symbol="Pa",
    dimension=NEWTON.dimension / (LENGTH ** 2),
)

JOULE = Unit(
    name="joule",
    symbol="J",
    dimension=NEWTON.dimension * LENGTH,
)

WATT = Unit(
    name="watt",
    symbol="W",
    dimension=JOULE.dimension / TIME,
)

COULOMB = Unit(
    name="coulomb",
    symbol="C",
    dimension=AMPERE.dimension * TIME,
)


SI_DERIVED_UNITS = {
    "sr": STERADIAN,
    "lm": LUMEN,
    "Hz": HERTZ,
    "N": NEWTON,
    "Pa": PASCAL,
    "J": JOULE,
    "W": WATT,
    "C": COULOMB,
}
