from science.units.prefix import Prefix


QUECTO = Prefix("quecto", "q", 1e-30)
RONTO = Prefix("ronto", "r", 1e-27)
YOCTO = Prefix("yocto", "y", 1e-24)
ZEPTO = Prefix("zepto", "z", 1e-21)
ATTO = Prefix("atto", "a", 1e-18)
FEMTO = Prefix("femto", "f", 1e-15)
PICO = Prefix("pico", "p", 1e-12)
NANO = Prefix("nano", "n", 1e-9)
MICRO = Prefix("micro", "μ", 1e-6)
MILLI = Prefix("milli", "m", 1e-3)
CENTI = Prefix("centi", "c", 1e-2)
DECI = Prefix("deci", "d", 1e-1)

DECA = Prefix("deca", "da", 1e1)
HECTO = Prefix("hecto", "h", 1e2)
KILO = Prefix("kilo", "k", 1e3)
MEGA = Prefix("mega", "M", 1e6)
GIGA = Prefix("giga", "G", 1e9)
TERA = Prefix("tera", "T", 1e12)
PETA = Prefix("peta", "P", 1e15)
EXA = Prefix("exa", "E", 1e18)
ZETTA = Prefix("zetta", "Z", 1e21)
YOTTA = Prefix("yotta", "Y", 1e24)
RONNA = Prefix("ronna", "R", 1e27)
QUETTA = Prefix("quetta", "Q", 1e30)


SI_PREFIXES = {
    prefix.symbol: prefix
    for prefix in (
        QUECTO,
        RONTO,
        YOCTO,
        ZEPTO,
        ATTO,
        FEMTO,
        PICO,
        NANO,
        MICRO,
        MILLI,
        CENTI,
        DECI,
        DECA,
        HECTO,
        KILO,
        MEGA,
        GIGA,
        TERA,
        PETA,
        EXA,
        ZETTA,
        YOTTA,
        RONNA,
        QUETTA,
    )
}
