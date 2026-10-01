from __future__ import annotations

from typing import Sequence

from ..document_interface import EmbeddingDocument
from ..model_interface import EmbeddingModel
from ..service_interface import EmbeddingRequest, EmbeddingResponse, EmbeddingService


class ReferenceEmbeddingService(EmbeddingService):
    """Reference I-5 service implementation using dependency injection."""

    def __init__(self, model: EmbeddingModel) -> None:
        self._model = model

    def embed(self, request: EmbeddingRequest) -> EmbeddingResponse:
        document: EmbeddingDocument = request.document
        vector: Sequence[float] = self._model.embed(document.document_text)

        return EmbeddingResponse(
            record_id=document.record_id,
            record_version=document.record_version,
            embedding_spec_version=document.embedding_spec_version,
            model_id=self._model.model_id(),
            dimension=self._model.dimension(),
            vector=vector,
        )

    def health_check(self) -> bool:
        return True
