from __future__ import annotations


class EmbeddingStoreError(Exception):
    """Base error for I-4 EmbeddingStore operations."""


class VectorNotFound(EmbeddingStoreError):
    """Requested vector identity does not exist."""


class VectorAlreadyExists(EmbeddingStoreError):
    """Vector identity already exists and cannot be silently replaced."""


class InvalidVector(EmbeddingStoreError):
    """VectorRecord violates the I-4/T-4 contract."""


class InvalidSearch(EmbeddingStoreError):
    """Search request violates I-4 requirements."""


class StoreUnavailable(EmbeddingStoreError):
    """Storage backend is unavailable or unhealthy."""
