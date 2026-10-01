from science.dimensions import Dimension
from science.formulas.formula import Formula
from science.formulas.operations import FormulaOperation


def evaluate_operation_dimension(
    operation: FormulaOperation,
    dimensions: dict[str, Dimension],
) -> Dimension:
    """
    Derive the physical dimension produced by a controlled operation.
    """

    try:
        operand_dimensions = [
            dimensions[name]
            for name in operation.operands
        ]
    except KeyError as exc:
        raise ValueError(
            f"Unknown variable in formula operation: {exc.args[0]}"
        ) from exc

    if operation.operation == "multiply":
        result = Dimension()

        for dimension in operand_dimensions:
            result = result * dimension

        return result

    if operation.operation == "divide":
        if len(operand_dimensions) != 2:
            raise ValueError(
                "Divide operation requires exactly two operands."
            )

        return operand_dimensions[0] / operand_dimensions[1]

    if operation.operation == "power":
        return operand_dimensions[0] ** operation.power

    raise ValueError(
        f"Unsupported formula operation: {operation.operation}"
    )


def validate_formula_dimensions(formula: Formula) -> None:
    """
    Verify that a formula's operation produces its declared output dimension.
    """

    derived_dimension = evaluate_operation_dimension(
        formula.operation,
        formula.dimensions,
    )

    if derived_dimension != formula.output_dimension:
        raise ValueError(
            "Formula dimensional inconsistency: "
            f"derived {derived_dimension}, "
            f"expected {formula.output_dimension}"
        )
