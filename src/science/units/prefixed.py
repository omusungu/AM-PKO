from dataclasses import dataclass

from science.units.prefix import Prefix
from science.units.unit import Unit


@dataclass(frozen=True)
class PrefixedUnit(Unit):
    """
    A unit formed by applying an SI prefix to another unit.

    The base unit and prefix are retained explicitly so that
    scientific meaning and construction provenance are preserved.
    """

    prefix: Prefix | None = None
    base_unit: Unit | None = None


def make_prefixed_unit(
    prefix: Prefix,
    unit: Unit,
) -> PrefixedUnit:
    """
    Construct a prefixed unit while preserving its prefix and base unit.
    """

    return PrefixedUnit(
        name=f"{prefix.name}{unit.name}",
        symbol=f"{prefix.symbol}{unit.symbol}",
        dimension=unit.dimension,
        scale=unit.scale * prefix.factor,
        offset=unit.offset,
        prefix=prefix,
        base_unit=unit,
    )
