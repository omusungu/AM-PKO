from science.constants.constant import Constant


class ConstantRegistry:
    """
    Controlled registry for scientific constants.

    Constants can be resolved by symbol or canonical name.
    """

    def __init__(self, constants: list[Constant] | None = None):
        self._by_symbol: dict[str, Constant] = {}
        self._by_name: dict[str, Constant] = {}

        if constants:
            for constant in constants:
                self.register(constant)

    def register(self, constant: Constant) -> None:
        if constant.symbol in self._by_symbol:
            raise ValueError(
                f"Constant symbol already registered: {constant.symbol}"
            )

        name_key = constant.name.lower()

        if name_key in self._by_name:
            raise ValueError(
                f"Constant name already registered: {constant.name}"
            )

        self._by_symbol[constant.symbol] = constant
        self._by_name[name_key] = constant

    def get(self, identifier: str) -> Constant:
        if identifier in self._by_symbol:
            return self._by_symbol[identifier]

        name_key = identifier.lower()

        if name_key in self._by_name:
            return self._by_name[name_key]

        raise KeyError(f"Unknown constant: {identifier}")

    def __contains__(self, identifier: str) -> bool:
        return (
            identifier in self._by_symbol
            or identifier.lower() in self._by_name
        )

    def __len__(self) -> int:
        return len(self._by_symbol)


from science.constants.si_defining import SI_DEFINING_CONSTANTS


SI_CONSTANT_REGISTRY = ConstantRegistry(
    list(SI_DEFINING_CONSTANTS.values())
)
