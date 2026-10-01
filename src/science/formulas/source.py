from dataclasses import dataclass


@dataclass(frozen=True)
class FormulaSource:
    """
    Structured provenance for a scientific formula.
    """

    authority: str
    reference: str = ""
    note: str = ""

    def __post_init__(self) -> None:
        if not self.authority:
            raise ValueError("Formula source authority cannot be empty.")

    def __str__(self) -> str:
        if self.reference:
            return f"{self.authority}: {self.reference}"
        return self.authority
