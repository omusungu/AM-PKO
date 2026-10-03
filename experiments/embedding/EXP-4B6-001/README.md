# EXP-4B6-001 — Human Utility & Retrieval Assay

Status: EVALUATED / VALIDATED
Experiment version: 0.1

## Objective

Evaluate whether the frozen AM-PKO retrieval core supports human-usable knowledge work while preserving identity, provenance, semantic discrimination, and contradiction visibility.

## Experimental Scope

This experiment evaluates the existing frozen retrieval pipeline.
It does not modify or refreeze I-2, I-3, I-4, I-5, I-6, T-5, T-6, or T-7.

## Candidate Models

- M-000001 — BGE-M3
- M-000002 — multilingual-e5-large
- M-000003 — Qwen3-Embedding-0.6B

No production model is selected by this experiment.

## Corpus Design

Target corpus size: 50 KnowledgeRecords.

The corpus will contain:
- interconnected records;
- semantically overlapping records;
- intentionally ambiguous records;
- intentionally contradictory records;
- multiple knowledge types;
- multiple domains/projects;
- explicit provenance;
- stable record identities.

## Query Design

Queries will test:
1. direct semantic retrieval;
2. ambiguous concepts;
3. contextually similar but semantically distinct concepts;
4. contradictory knowledge;
5. relationship-dependent knowledge;
6. cross-topic retrieval.

## Evaluation Dimensions

### Retrieval Accuracy
Whether relevant records appear in the retrieved ranking.

### Identity Preservation
Whether retrieved record identity remains traceable to the originating KnowledgeRecord.

### Provenance Preservation
Whether the retrieval path remains traceable through the frozen embedding/retrieval boundaries.

### Semantic Discrimination
Whether closely related but meaningfully different records remain distinguishable.

### Contradiction Visibility
Whether conflicting records can be retrieved together without one being silently discarded or rewritten.

### Human Utility
Whether retrieved results can be inspected and reused by a human without losing their epistemic context.

## Evaluation Metrics
The T-7 evaluation has been completed for all three candidate models using the frozen corpus, queries, and judgments.

Reported metrics:
- Recall@1
- Recall@3
- Recall@5
- MRR
- nDCG@1
- nDCG@3
- nDCG@5
- HighRelevanceRecall@1
- HighRelevanceRecall@3
- HighRelevanceRecall@5

The evaluation validation artifact independently recomputed the metrics with maximum difference `0.0`.

## Experimental Discipline

Inputs and judgments must be frozen before comparative evaluation.

No automatic model winner will be produced.
No production embedding model will be selected automatically.
No frozen AM-PKO contract will be modified by this experiment.

## Artifacts
The experiment currently contains:
- README.md
- corpus.json
- queries.json
- judgments.json
- models.json
- M-000001/2/3 corpus embeddings
- M-000001/2/3 query embeddings
- M-000001/2/3 retrieval outputs
- M-000001/2/3 T-7 evaluation outputs
- corpus, query, judgment, and evaluation validation artifacts
- corpus, query, and judgment freeze manifests
- generation, retrieval, and evaluation scripts

`results.json` and `human_assessment.json` are not currently part of the generated artifact set.

## Current State
The experiment has progressed from design through controlled corpus, query, and judgment freezing to completed T-7 evaluation.

Current lifecycle:
1. Corpus: FROZEN
2. Queries: FROZEN
3. Judgments: FROZEN
4. Candidate embedding generation: COMPLETED
5. Retrieval generation: COMPLETED
6. T-7 evaluation: VALIDATED
7. Production embedding-model selection: FROZEN_NOT_DECIDED

All three candidate-model evaluation artifacts are structurally valid and numerically independently reproducible.

No production embedding model is selected by this experiment. The separate production-selection decision artifact remains intentionally `FROZEN_NOT_DECIDED`.

The experiment does not modify or refreeze the frozen AM-PKO interfaces or types.
