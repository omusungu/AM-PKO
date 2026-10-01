# AM-PKO T-7 — EvaluationRun Design

Status: DESIGN_RECONCILED
Contract version: 0.2-design

## Purpose

T-7 represents one reproducible evaluation run over retrieval results.

It belongs to the evaluation boundary and does not participate in runtime retrieval.

## Evidence recovered

Existing EXP-4B5 evaluation artifacts establish these evaluation dimensions:

- experiment identity
- model identity
- relevance judgments
- per-query evaluation
- aggregate retrieval metrics

Observed aggregate metrics include:

- Recall@1
- Recall@3
- Recall@5
- HighRelevanceRecall@1
- HighRelevanceRecall@3
- HighRelevanceRecall@5
- nDCG@1
- nDCG@3
- nDCG@5
- MRR

## Reconstructed fields

### evaluation_id

Identifier for the evaluation run.

Type:
`str`

### experiment_id

Identifier of the experiment being evaluated.

Type:
`str`

### model_id

Identifier of the embedding model evaluated.

Type:
`str`

### model_family

Human-readable model-family identifier.

Type:
`str`

### judgment_scale

Definition of relevance levels used by the evaluation.

Type:
`Mapping`

### per_query

Per-query evaluation results.

Type:
`Sequence[Mapping]`

### metrics

Aggregate evaluation metrics.

Type:
`Mapping[str, float]`

## Boundary

T-7 does not:

- generate query embeddings
- generate document embeddings
- perform vector storage
- perform cosine similarity
- perform runtime ranking
- mutate KnowledgeRecords
- perform graph traversal
- perform RAG synthesis
- select a production embedding model

## Relationship to T-5 and T-6

T-5 represents the retrieval request.

T-6 represents individual ranked retrieval matches.

T-7 evaluates retrieval behavior using experiment inputs, relevance judgments, and measured results.

T-7 therefore does not become part of the runtime retrieval path.

## Evidence reconciliation

The reconstructed T-7 field set has been reconciled against the
EXP-4B5-001 evaluation artifacts.

### Directly evidenced fields

The following fields are directly represented in the historical
evaluation artifacts:

- `experiment_id`
- `model_id`
- `per_query`
- `metrics`

### Evidence-derived fields

The following fields are recoverable from the frozen experiment inputs
but are not represented uniformly in every historical evaluation file:

- `model_family` — derived by joining `model_id` against `models.json`.
- `judgment_scale` — derived from the relevance scale represented in
  `judgments.json`.

### Canonical reconstructed identity

`evaluation_id` is retained as a canonical T-7 identity field.

It is not claimed to have existed as an explicit field in every
historical evaluation artifact.

### Historical schema variation

The three historical model evaluation artifacts are not schema-identical.

- M-000001 explicitly contains `experiment_id`, `model_id`,
  `model_family`, and `judgment_scale`.
- M-000002 and M-000003 use `evaluation` for the experiment identifier
  and omit `model_family` and `judgment_scale` from the evaluation file.

Therefore the canonical T-7 contract represents a reconciled schema and
does not claim that all seven fields were historically serialized in
identical form.

### Reconciliation principle

Historical evidence is preserved as observed.

Canonical T-7 fields may be constructed from authoritative experiment
inputs where the historical evaluation artifact omitted duplicated
metadata. Such reconstruction must remain explicitly distinguishable
from direct historical serialization.

## Reconstruction status

The design is evidence-reconciled but remains a non-frozen contract.

The exact historical Python interface and complete original validation
rules were not recoverable.

No frozen I-2, I-3, I-4, or I-5 contract is modified by this design.
