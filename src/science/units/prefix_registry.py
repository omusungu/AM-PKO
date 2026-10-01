from science.units.prefix import Prefix


class PrefixRegistry:
    """
    Controlled registry for SI decimal prefixes.

    Prefixes can be resolved by symbol or canonical name.
    """

    def __init__(self, prefixes: list[Prefix] | None = None):
        self._by_symbol: dict[str, Prefix] = {}
        self._by_name: dict[str, Prefix] = {}

        if prefixes:
            for prefix in prefixes:
                self.register(prefix)

    def register(self, prefix: Prefix) -> None:
        if prefix.symbol in self._by_symbol:
            raise ValueError(
                f"Prefix symbol already registered: {prefix.symbol}"
            )

        name_key = prefix.name.lower()

        if name_key in self._by_name:
            raise ValueError(
                f"Prefix name already registered: {prefix.name}"
            )

        self._by_symbol[prefix.symbol] = prefix
        self._by_name[name_key] = prefix

    def get(self, identifier: str) -> Prefix:
        if identifier in self._by_symbol:
            return self._by_symbol[identifier]

        name_key = identifier.lower()

        if name_key in self._by_name:
            return self._by_name[name_key]

        raise KeyError(f"Unknown prefix: {identifier}")

    def __contains__(self, identifier: str) -> bool:
        return (
            identifier in self._by_symbol
            or identifier.lower() in self._by_name
        )

    def __len__(self) -> int:
        return len(self._by_symbol)


from science.units.prefixes import SI_PREFIXES

SI_PREFIX_REGISTRY = PrefixRegistry(SI_PREFIXES.values())
