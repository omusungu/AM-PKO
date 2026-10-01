from science.formulas.formula import Formula


class FormulaRegistry:
    """
    Controlled registry for scientific formulas.

    Formulas can be resolved by symbol or canonical name.
    """

    def __init__(self, formulas: list[Formula] | None = None):
        self._by_symbol: dict[str, Formula] = {}
        self._by_name: dict[str, Formula] = {}

        if formulas:
            for formula in formulas:
                self.register(formula)

    def register(self, formula: Formula) -> None:
        if not isinstance(formula, Formula):
            raise TypeError("Only Formula instances can be registered.")

        if formula.symbol in self._by_symbol:
            raise ValueError(
                f"Formula symbol already registered: {formula.symbol}"
            )

        name_key = formula.name.lower()

        if name_key in self._by_name:
            raise ValueError(
                f"Formula name already registered: {formula.name}"
            )

        self._by_symbol[formula.symbol] = formula
        self._by_name[name_key] = formula

    def get(self, identifier: str) -> Formula:
        if identifier in self._by_symbol:
            return self._by_symbol[identifier]

        name_key = identifier.lower()

        if name_key in self._by_name:
            return self._by_name[name_key]

        raise KeyError(f"Unknown formula: {identifier}")

    def __contains__(self, identifier: str) -> bool:
        return (
            identifier in self._by_symbol
            or identifier.lower() in self._by_name
        )

    def __len__(self) -> int:
        return len(self._by_symbol)


from science.formulas.basic import BASIC_FORMULAS

BASIC_FORMULA_REGISTRY = FormulaRegistry(
    list(BASIC_FORMULAS.values())
)
