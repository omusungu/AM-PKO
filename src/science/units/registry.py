from science.units.unit import Unit
from science.units.si import SI_BASE_UNITS
from science.units.derived import SI_DERIVED_UNITS


class UnitRegistry:
    """
    Controlled registry for scientific units.

    Units can be resolved by symbol or canonical name.
    """

    def __init__(self, units: list[Unit] | None = None):
        self._by_symbol: dict[str, Unit] = {}
        self._by_name: dict[str, Unit] = {}

        if units:
            for unit in units:
                self.register(unit)

    def register(self, unit: Unit) -> None:
        if unit.symbol in self._by_symbol:
            raise ValueError(
                f"Unit symbol already registered: {unit.symbol}"
            )

        name_key = unit.name.lower()

        if name_key in self._by_name:
            raise ValueError(
                f"Unit name already registered: {unit.name}"
            )

        self._by_symbol[unit.symbol] = unit
        self._by_name[name_key] = unit

    def get(self, identifier: str) -> Unit:
        if identifier in self._by_symbol:
            return self._by_symbol[identifier]

        name_key = identifier.lower()

        if name_key in self._by_name:
            return self._by_name[name_key]

        raise KeyError(f"Unknown unit: {identifier}")

    def __contains__(self, identifier: str) -> bool:
        return (
            identifier in self._by_symbol
            or identifier.lower() in self._by_name
        )

    def __len__(self) -> int:
        return len(self._by_symbol)


SI_REGISTRY = UnitRegistry(
    list(SI_BASE_UNITS.values()) +
    list(SI_DERIVED_UNITS.values())
)
