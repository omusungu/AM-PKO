from __future__ import annotations

from typing import Sequence

from .query_embedder_interface import QueryEmbedder
from .retrieval_interface import QueryRequest
from .retrieval_result import RankedResult
from .store.interface import EmbeddingStore
from .store.match import VectorStoreMatch


class RetrievalService:
    """
    AM-PKO I-6 — retrieval orchestration boundary.

    Coordinates T-5 query requests, query embedding, and I-4 vector
    search. It does not implement embedding-model behavior, vector
    similarity, ranking, filtering, evaluation, or RAG synthesis.
    """

    def __init__(
        self,
        query_embedder: QueryEmbedder,
        store: EmbeddingStore,
    ) -> None:
        self._query_embedder = query_embedder
        self._store = store

    def retrieve(self, request: QueryRequest) -> list[RankedResult]:
        if not isinstance(request, QueryRequest):
            raise TypeError("request must be a QueryRequest")

        query_vector: Sequence[float] = (
            self._query_embedder.embed_query(request.query)
        )

        vector_records = self._store.search(
            query_vector,
            k=request.k,
            filters=request.filters,
            include_excluded=request.include_excluded,
        )

        results: list[RankedResult] = []

        for match in vector_records:
            if not isinstance(match, VectorStoreMatch):
                raise TypeError(
                    "I-4 search result must be a VectorStoreMatch"
                )

            results.append(
                RankedResult(
                    record_id=match.record.identity.record_id,
                    score=match.score,
                )
            )

        return results
