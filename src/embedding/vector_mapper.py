from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .service_interface import EmbeddingResponse
from .store.interface import VectorIdentity, VectorRecord
from .store.payload import validate_vector_record
from .vector_mapper_interface import VectorRecordMapper


class ReferenceVectorRecordMapper(VectorRecordMapper):
    """Reference mapper from KnowledgeRecord + I-5 response to T-3."""

    @staticmethod
    def _required(record: Mapping[str, Any], key: str) -> Any:
        if key not in record:
            raise KeyError(f"KnowledgeRecord missing required field: {key}")
        return record[key]

    def map(
        self,
        record: Mapping[str, Any],
        embedding: EmbeddingResponse,
    ) -> VectorRecord:
        metadata = self._required(record, "metadata")
        if not isinstance(metadata, Mapping):
            raise TypeError("KnowledgeRecord metadata must be a mapping")

        source = self._required(record, "source")
        if not isinstance(source, Mapping):
            raise TypeError("KnowledgeRecord source must be a mapping")

        record_id = self._required(record, "id")
        record_version = self._required(metadata, "version")
        created_at = self._required(metadata, "created_at")
        source_type = self._required(source, "type")
        skills = self._required(record, "skills")

        if embedding.record_id != record_id:
            raise ValueError("Embedding record_id does not match KnowledgeRecord id")

        if embedding.record_version != record_version:
            raise ValueError(
                "Embedding record_version does not match KnowledgeRecord version"
            )

        identity = VectorIdentity(
            record_id=embedding.record_id,
            embedding_spec_version=embedding.embedding_spec_version,
            embedding_model_id=embedding.model_id,
            record_version=embedding.record_version,
        )

        payload = {
            "record_id": record_id,
            "knowledge_type": self._required(record, "knowledge_type"),
            "granularity": self._required(record, "granularity"),
            "domain": self._required(record, "domain"),
            "project": self._required(record, "project"),
            "status": self._required(record, "status"),
            "topic": self._required(record, "topic"),
            "skills": skills,
            "source_type": source_type,
            "embedding_spec_version": embedding.embedding_spec_version,
            "embedding_model_id": embedding.model_id,
            "record_version": record_version,
            "created_at": created_at,
        }

        vector_record = VectorRecord(
            identity=identity,
            dimension=embedding.dimension,
            vector=embedding.vector,
            payload=payload,
        )

        validate_vector_record(vector_record)
        return vector_record
