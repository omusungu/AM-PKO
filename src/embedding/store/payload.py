from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .interface import VectorRecord


REQUIRED_PAYLOAD_FIELDS = (
    "record_id",
    "knowledge_type",
    "granularity",
    "domain",
    "project",
    "status",
    "topic",
    "skills",
    "source_type",
    "embedding_spec_version",
    "embedding_model_id",
    "record_version",
    "created_at",
)


def validate_vector_record(vector_record: VectorRecord) -> None:
    """Fail closed if a T-3 VectorRecord violates T-4 requirements."""

    if vector_record.dimension <= 0:
        raise ValueError("Vector dimension must be positive")

    if len(vector_record.vector) != vector_record.dimension:
        raise ValueError(
            "Vector length does not match declared dimension"
        )

    if not isinstance(vector_record.payload, Mapping):
        raise TypeError("Vector payload must be a mapping")

    missing = [
        field
        for field in REQUIRED_PAYLOAD_FIELDS
        if field not in vector_record.payload
    ]

    if missing:
        raise ValueError(
            "Vector payload missing required fields: "
            + ", ".join(missing)
        )

    identity = vector_record.identity
    payload = vector_record.payload

    identity_matches = (
        payload["record_id"] == identity.record_id
        and payload["embedding_spec_version"]
        == identity.embedding_spec_version
        and payload["embedding_model_id"]
        == identity.embedding_model_id
        and payload["record_version"]
        == identity.record_version
    )

    if not identity_matches:
        raise ValueError(
            "Vector identity does not match T-4 payload provenance"
        )

    if not isinstance(payload["skills"], (list, tuple)):
        raise TypeError("T-4 skills must be a list or tuple")
