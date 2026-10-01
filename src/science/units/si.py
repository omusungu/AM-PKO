from science.dimensions import Dimension
from science.units.unit import Unit


SECOND = Unit(
    name="second",
    symbol="s",
    dimension=Dimension(time=1),
)

METRE = Unit(
    name="metre",
    symbol="m",
    dimension=Dimension(length=1),
)

KILOGRAM = Unit(
    name="kilogram",
    symbol="kg",
    dimension=Dimension(mass=1),
)

AMPERE = Unit(
    name="ampere",
    symbol="A",
    dimension=Dimension(current=1),
)

KELVIN = Unit(
    name="kelvin",
    symbol="K",
    dimension=Dimension(temperature=1),
)

MOLE = Unit(
    name="mole",
    symbol="mol",
    dimension=Dimension(amount=1),
)

CANDELA = Unit(
    name="candela",
    symbol="cd",
    dimension=Dimension(luminous_intensity=1),
)


SI_BASE_UNITS = {
    "s": SECOND,
    "m": METRE,
    "kg": KILOGRAM,
    "A": AMPERE,
    "K": KELVIN,
    "mol": MOLE,
    "cd": CANDELA,
}
