from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


class EmbeddingDocumentError(Exception):
    """Base error for I-2 embedding-document operations."""


@dataclass(frozen=True)
class EmbeddingDocument:
    """Canonical AM-PKO T-2 EmbeddingDocument."""

    record_id: str
    record_version: str
    embedding_spec_version: str
    document_text: str
    document_hash: str


class EmbeddingDocumentGenerator(ABC):
    """
    AM-PKO I-2 — deterministic EmbeddingDocument generator.

    Implementations transform one canonical KnowledgeRecord into one
    deterministic T-2 EmbeddingDocument according to ER-10.
    """

    @abstractmethod
    def generate(self, record: object) -> EmbeddingDocument:
        """Generate the canonical embedding document."""

    @abstractmethod
    def hash(self, document: EmbeddingDocument) -> str:
        """Return the canonical document hash."""

    @abstractmethod
    def spec_version(self) -> str:
        """Return the exact ER-10 specification version."""
