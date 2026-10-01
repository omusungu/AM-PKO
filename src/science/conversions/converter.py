from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from science.quantities import Quantity


def convert_quantity(
    quantity: "Quantity",
    target_unit,
) -> "Quantity":
    """
    Convert a quantity to a dimensionally compatible target unit.

    This implementation handles multiplicative unit scaling.
    Affine temperature conversion is intentionally not implemented here.
    """

    from science.quantities import Quantity

    if not isinstance(quantity, Quantity):
        raise TypeError("Conversion requires a Quantity.")

    if quantity.dimension != target_unit.dimension:
        raise ValueError(
            f"Incompatible dimensions: "
            f"{quantity.dimension} and {target_unit.dimension}"
        )

    value = quantity.value * quantity.scale / target_unit.scale

    return Quantity(
        value=value,
        unit=target_unit,
    )
