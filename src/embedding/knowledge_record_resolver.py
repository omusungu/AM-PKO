from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Mapping


class KnowledgeRecordResolver(ABC):
    """
    AM-PKO T-1 resolution boundary.

    Resolves a KnowledgeRecord identity to the authoritative structured
    KnowledgeRecord representation required by downstream components.

    This interface does not define a new KnowledgeRecord type. The
    canonical T-1 representation remains the existing authoritative
    structured record contract.
    """

    @abstractmethod
    def resolve(self, record_id: str) -> Mapping[str, Any]:
        """
        Resolve one KnowledgeRecord identifier.

        Implementations must return the authoritative structured record
        corresponding to record_id.
        """
        raise NotImplementedError
