from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Sequence

from embedding.adapters.base import CheckpointEmbeddingAdapter


class LlamaCppEmbeddingAdapter(CheckpointEmbeddingAdapter):
    """
    AM-PKO I-3 adapter for the llama.cpp `llama-embedding` executable.

    One adapter instance represents one pinned embedding checkpoint.
    """

    def __init__(
        self,
        *,
        model_path: str | Path,
        model_id: str,
        model_family: str,
        dimension: int,
        max_input_tokens: int,
        pooling: str | None = "mean",
        normalize: int = 2,
        context_size: int = 512,
        threads: int = 8,
        executable: str = "llama-embedding",
        separator: str = "\x1e",
        query_prefix: str = "",
        document_prefix: str = "",
    ) -> None:
        self._model_path = Path(model_path).expanduser().resolve()
        self._model_id = model_id
        self._model_family = model_family
        self._dimension = dimension
        self._max_input_tokens = max_input_tokens
        self._pooling = pooling
        self._normalize = normalize
        self._context_size = context_size
        self._threads = threads
        self._executable = executable
        self._separator = separator
        self._query_prefix = query_prefix
        self._document_prefix = document_prefix

        if not self._model_path.is_file():
            raise FileNotFoundError(
                f"Embedding checkpoint not found: {self._model_path}"
            )

        if self._dimension <= 0:
            raise ValueError("dimension must be positive")

        if self._max_input_tokens <= 0:
            raise ValueError("max_input_tokens must be positive")

        if self._context_size <= 0:
            raise ValueError("context_size must be positive")

        if self._threads <= 0:
            raise ValueError("threads must be positive")

    def model_id(self) -> str:
        return self._model_id

    def model_family(self) -> str:
        return self._model_family

    def dimension(self) -> int:
        return self._dimension

    def max_input_tokens(self) -> int:
        return self._max_input_tokens

    def _count_tokens(self, text: str) -> int:
        """Return the actual token count produced by the pinned checkpoint tokenizer."""
        command = [
            "llama-tokenize",
            "--model",
            str(self._model_path),
            "--prompt",
            text,
        ]

        completed = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
            env=os.environ.copy(),
        )

        if completed.returncode != 0:
            raise RuntimeError(
                "llama-tokenize failed: "
                + completed.stderr.strip()
            )

        count = 0
        for line in completed.stdout.splitlines():
            if " -> " in line:
                token_id, _ = line.split(" -> ", 1)
                try:
                    int(token_id.strip())
                except ValueError:
                    continue
                count += 1

        if count == 0:
            raise RuntimeError(
                "llama-tokenize returned no parseable tokens"
            )

        return count

    def _embed_text(self, text: str) -> Sequence[float]:
        command = [
            self._executable,
            "--model",
            str(self._model_path),
            "--ctx-size",
            str(self._context_size),
            "--threads",
            str(self._threads),
        ]

        if self._pooling is not None:
            command.extend([
                "--pooling",
                self._pooling,
            ])

        command.extend([
            "--embd-normalize",
            str(self._normalize),
            "--embd-output-format",
            "raw",
            "--embd-separator",
            self._separator,
            "--prompt",
            text,
        ])

        completed = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
            env=os.environ.copy(),
        )

        if completed.returncode != 0:
            raise RuntimeError(
                "llama-embedding failed: "
                + completed.stderr.strip()
            )

        tokens = completed.stdout.split()
        if not tokens:
            raise RuntimeError(
                "llama-embedding returned empty embedding output"
            )

        values = []
        for index, token in enumerate(tokens):
            try:
                values.append(float(token))
            except ValueError as exc:
                raise RuntimeError(
                    "llama-embedding returned unexpected non-numeric "
                    f"stdout token at position {index}: {token!r}"
                ) from exc

        if len(values) != self._dimension:
            raise ValueError(
                "Unexpected embedding dimension: "
                f"expected {self._dimension}, got {len(values)}"
            )

        return values

    def embed_query(self, text: str) -> Sequence[float]:
        return self.embed(self._query_prefix + text)

    def embed_document(self, text: str) -> Sequence[float]:
        return self.embed(self._document_prefix + text)
