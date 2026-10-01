from science.dimensions import Dimension
from science.formulas.formula import Formula
from science.formulas.operations import FormulaOperation
from science.formulas.source import FormulaSource
from science.units import KILOGRAM, METRE, SECOND


NEWTON_SECOND_LAW = Formula(
    name="Newton's second law",
    symbol="F",
    variables=("F", "m", "a"),
    output="F",
    dimensions={
        "F": Dimension(mass=1, length=1, time=-2),
        "m": KILOGRAM.dimension,
        "a": Dimension(length=1, time=-2),
    },
    operation=FormulaOperation(
        operation="multiply",
        operands=("m", "a"),
    ),
    expression="F = m * a",
    description="Force equals mass multiplied by acceleration.",
    source="Classical mechanics; Newtonian mechanics.",
    provenance=FormulaSource(
        authority="Newtonian mechanics",
        reference="Newton's second law",
    ),
)


SPEED = Formula(
    name="Speed",
    symbol="v",
    variables=("v", "d", "t"),
    output="v",
    dimensions={
        "v": Dimension(length=1, time=-1),
        "d": METRE.dimension,
        "t": SECOND.dimension,
    },
    operation=FormulaOperation(
        operation="divide",
        operands=("d", "t"),
    ),
    expression="v = d / t",
    description="Speed equals distance divided by time.",
    source="Classical mechanics; kinematics.",
    provenance=FormulaSource(
        authority="Classical mechanics",
        reference="Kinematics",
    ),
)


AREA = Formula(
    name="Area",
    symbol="A",
    variables=("A", "l"),
    output="A",
    dimensions={
        "A": Dimension(length=2),
        "l": METRE.dimension,
    },
    operation=FormulaOperation(
        operation="power",
        operands=("l",),
        power=2,
    ),
    expression="A = l^2",
    description="Area of a square equals length squared.",
    source="Euclidean geometry.",
    provenance=FormulaSource(
        authority="Euclidean geometry",
        reference="Area of a square",
    ),
)


BASIC_FORMULAS = {
    NEWTON_SECOND_LAW.symbol: NEWTON_SECOND_LAW,
    SPEED.symbol: SPEED,
    AREA.symbol: AREA,
}
