from science.formulas.formula import Formula
from science.formulas.dimensional import validate_formula_dimensions
from science.quantities import Quantity


def evaluate_formula(
    formula: Formula,
    values: dict[str, Quantity],
) -> Quantity:
    """
    Evaluate a dimensionally valid controlled formula.

    The formula output variable is derived from the declared operation
    and therefore does not require an input value.

    Numerical evaluation is performed only through the formula's
    structured operation tree. No Python expression is evaluated.
    """

    validate_formula_dimensions(formula)

    input_variables = set(formula.variables) - {formula.output}

    missing = input_variables - set(values)

    if missing:
        raise ValueError(
            f"Missing values for variables: "
            f"{', '.join(sorted(missing))}"
        )

    unexpected = set(values) - input_variables

    if unexpected:
        raise ValueError(
            f"Values provided for undeclared or output variables: "
            f"{', '.join(sorted(unexpected))}"
        )

    for name in input_variables:
        if not isinstance(values[name], Quantity):
            raise TypeError(
                f"Value for variable '{name}' must be a Quantity."
            )

    operands = [
        values[name]
        for name in formula.operation.operands
    ]

    if formula.operation.operation == "multiply":
        result = operands[0]

        for operand in operands[1:]:
            result = result * operand

    elif formula.operation.operation == "divide":
        if len(operands) != 2:
            raise ValueError(
                "Divide operation requires exactly two operands."
            )

        result = operands[0] / operands[1]

    elif formula.operation.operation == "power":
        if len(operands) != 1:
            raise ValueError(
                "Power operation requires exactly one operand."
            )

        result = operands[0] ** formula.operation.power

    else:
        raise NotImplementedError(
            "Numerical evaluation currently supports "
            "multiply, divide, and power operations."
        )

    if result.dimension != formula.output_dimension:
        raise ValueError(
            "Formula evaluation produced an incompatible dimension: "
            f"{result.dimension}; expected {formula.output_dimension}"
        )

    return Quantity(
        value=result.value,
        unit=result.unit,
    )
