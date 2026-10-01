from __future__ import annotations

import hashlib
from collections.abc import Mapping, Sequence

from ..document_interface import (
    EmbeddingDocument,
    EmbeddingDocumentGenerator,
)


class ER10EmbeddingDocumentGenerator(EmbeddingDocumentGenerator):
    """
    AM-PKO I-2 implementation of the ER-10 deterministic formatter.

    The generator performs formatting only. It does not semantically
    rewrite, summarize, infer, or enrich KnowledgeRecord content.
    """

    _SPEC_VERSION = "0.1"

    def spec_version(self) -> str:
        return self._SPEC_VERSION

    @staticmethod
    def _text(value: object) -> str:
        if value is None:
            return ""
        return str(value).strip()

    @classmethod
    def _skills(cls, value: object) -> str:
        if value is None:
            return ""

        if not isinstance(value, Sequence) or isinstance(
            value, (str, bytes)
        ):
            raise TypeError("skills must be a sequence")

        return ", ".join(cls._text(item) for item in value)

    @staticmethod
    def _required(record: Mapping[str, object], key: str) -> object:
        if key not in record:
            raise KeyError(f"KnowledgeRecord missing required field: {key}")
        return record[key]

    def _document_text(self, record: Mapping[str, object]) -> str:
        knowledge_type = self._text(
            self._required(record, "knowledge_type")
        )
        granularity = self._text(
            self._required(record, "granularity")
        )

        fields = [
            (
                "Domain",
                self._text(record.get("domain")),
            ),
            (
                "Project",
                self._text(record.get("project")),
            ),
            (
                "Topic",
                self._text(record.get("topic")),
            ),
            (
                "Title",
                self._text(record.get("title")),
            ),
            (
                "Content",
                self._text(record.get("content")),
            ),
            (
                "Skills",
                self._skills(record.get("skills")),
            ),
        ]

        lines = [f"[{knowledge_type} / {granularity}]"]

        for label, value in fields:
            if value:
                lines.append(f"{label}: {value}")
            else:
                lines.append(f"{label}:")

        return "\n".join(lines)

    def hash(self, document: EmbeddingDocument) -> str:
        digest = hashlib.sha256(
            document.document_text.encode("utf-8")
        ).hexdigest()
        return f"sha256:{digest}"

    def generate(self, record: Mapping[str, object]) -> EmbeddingDocument:
        record_id = self._text(self._required(record, "id"))

        metadata = record.get("metadata")
        if not isinstance(metadata, Mapping):
            raise TypeError("KnowledgeRecord metadata must be a mapping")

        record_version = self._text(
            self._required(metadata, "version")
        )

        document_text = self._document_text(record)

        provisional = EmbeddingDocument(
            record_id=record_id,
            record_version=record_version,
            embedding_spec_version=self.spec_version(),
            document_text=document_text,
            document_hash="",
        )

        document_hash = self.hash(provisional)

        return EmbeddingDocument(
            record_id=provisional.record_id,
            record_version=provisional.record_version,
            embedding_spec_version=provisional.embedding_spec_version,
            document_text=provisional.document_text,
            document_hash=document_hash,
        )
