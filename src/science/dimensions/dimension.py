from dataclasses import dataclass


@dataclass(frozen=True)
class Dimension:
    """
    Represents the dimensional signature of a physical quantity.

    The exponents correspond to the seven SI base dimensions:
    mass, length, time, electric current,
    thermodynamic temperature, amount of substance,
    and luminous intensity.
    """

    mass: int = 0
    length: int = 0
    time: int = 0
    current: int = 0
    temperature: int = 0
    amount: int = 0
    luminous_intensity: int = 0

    def __mul__(self, other: "Dimension") -> "Dimension":
        if not isinstance(other, Dimension):
            return NotImplemented

        return Dimension(
            mass=self.mass + other.mass,
            length=self.length + other.length,
            time=self.time + other.time,
            current=self.current + other.current,
            temperature=self.temperature + other.temperature,
            amount=self.amount + other.amount,
            luminous_intensity=(
                self.luminous_intensity + other.luminous_intensity
            ),
        )

    def __truediv__(self, other: "Dimension") -> "Dimension":
        if not isinstance(other, Dimension):
            return NotImplemented

        return Dimension(
            mass=self.mass - other.mass,
            length=self.length - other.length,
            time=self.time - other.time,
            current=self.current - other.current,
            temperature=self.temperature - other.temperature,
            amount=self.amount - other.amount,
            luminous_intensity=(
                self.luminous_intensity - other.luminous_intensity
            ),
        )

    def __pow__(self, power: int) -> "Dimension":
        if not isinstance(power, int):
            raise TypeError("Dimension powers must be integers.")

        return Dimension(
            mass=self.mass * power,
            length=self.length * power,
            time=self.time * power,
            current=self.current * power,
            temperature=self.temperature * power,
            amount=self.amount * power,
            luminous_intensity=self.luminous_intensity * power,
        )

    def signature(self) -> str:
        """
        Return the canonical dimensional signature.
        """

        symbols = (
            ("M", self.mass),
            ("L", self.length),
            ("T", self.time),
            ("I", self.current),
            ("Θ", self.temperature),
            ("N", self.amount),
            ("J", self.luminous_intensity),
        )

        parts = [
            f"{symbol}^{exponent}"
            for symbol, exponent in symbols
            if exponent != 0
        ]

        return " ".join(parts) if parts else "1"

    def __str__(self) -> str:
        return self.signature()
