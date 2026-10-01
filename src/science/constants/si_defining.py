from science.constants.constant import Constant
from science.units import METRE, SECOND, JOULE, COULOMB, KELVIN, MOLE, HERTZ, LUMEN, WATT, divide_units, multiply_units, power_unit


SPEED_OF_LIGHT = Constant(
    name="speed of light in vacuum",
    symbol="c",
    value=299_792_458.0,
    unit=divide_units(METRE, SECOND),
    description="Speed of light in vacuum.",
    source="BIPM SI defining constant",
)


SI_DEFINING_CONSTANTS = {
    "c": SPEED_OF_LIGHT,
}

PLANCK_CONSTANT = Constant(
    name="Planck constant",
    symbol="h",
    value=6.62607015e-34,
    unit=multiply_units(JOULE, SECOND),
    description="Planck constant.",
    source="BIPM SI defining constant",
)


SI_DEFINING_CONSTANTS["h"] = PLANCK_CONSTANT

ELEMENTARY_CHARGE = Constant(
    name="elementary charge",
    symbol="e",
    value=1.602176634e-19,
    unit=COULOMB,
    description="Elementary charge.",
    source="BIPM SI defining constant",
)


SI_DEFINING_CONSTANTS["e"] = ELEMENTARY_CHARGE

BOLTZMANN_CONSTANT = Constant(
    name="Boltzmann constant",
    symbol="k",
    value=1.380649e-23,
    unit=divide_units(JOULE, KELVIN),
    description="Boltzmann constant.",
    source="BIPM SI defining constant",
)


SI_DEFINING_CONSTANTS["k"] = BOLTZMANN_CONSTANT

AVOGADRO_CONSTANT = Constant(
    name="Avogadro constant",
    symbol="N_A",
    value=6.02214076e23,
    unit=power_unit(MOLE, -1),
    description="Avogadro constant.",
    source="BIPM SI defining constant",
)


SI_DEFINING_CONSTANTS["N_A"] = AVOGADRO_CONSTANT

CESIUM_TRANSITION_FREQUENCY = Constant(
    name="cesium-133 hyperfine transition frequency",
    symbol="Delta_nu_Cs",
    value=9_192_631_770.0,
    unit=HERTZ,
    description="Unperturbed ground-state hyperfine transition frequency of cesium-133.",
    source="BIPM SI defining constant",
)


SI_DEFINING_CONSTANTS["Delta_nu_Cs"] = CESIUM_TRANSITION_FREQUENCY

LUMINOUS_EFFICACY = Constant(
    name="luminous efficacy of monochromatic radiation",
    symbol="K_cd",
    value=683.0,
    unit=divide_units(LUMEN, WATT),
    description="Luminous efficacy of monochromatic radiation of frequency 540 THz.",
    source="BIPM SI defining constant",
)


SI_DEFINING_CONSTANTS["K_cd"] = LUMINOUS_EFFICACY
