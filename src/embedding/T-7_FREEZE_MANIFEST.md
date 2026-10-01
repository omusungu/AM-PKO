# AM-PKO T-7 Freeze Manifest

**Status: FROZEN_VALIDATED**

**Contract version: 0.2**

## Contract

T-7 is the canonical `EvaluationRun` representation for one
reproducible retrieval evaluation run.

T-7 belongs to the evaluation boundary and does not participate
in runtime retrieval.

## Canonical fields

The frozen `EvaluationRun` contains exactly:

1. `evaluation_id`
2. `experiment_id`
3. `model_id`
4. `model_family`
5. `judgment_scale`
6. `per_query`
7. `metrics`

## Field provenance

### Directly evidenced

The EXP-4B5-001 evaluation artifacts directly evidence:

- `experiment_id` / equivalent evaluation experiment identity
- `model_id`
- `per_query`
- `metrics`

The M-000001 evaluation artifact additionally directly serializes:

- `model_family`
- complete `judgment_scale`

### Evidence-derived

For evaluation artifacts that omit duplicated metadata:

- `model_family` may be resolved from authoritative `models.json`
- `judgment_scale` may be resolved from the authoritative declared
  evaluation scale evidenced by the M-000001 evaluation artifact

### Reconstructed

`evaluation_id` is a canonical T-7 identity field reconstructed from
the experiment and model identities.

The historical artifacts do not establish that this exact field was
serialized identically in every original artifact.

Canonical reconstruction used:

`experiment_id:model_id`

## Historical schema variation

EXP-4B5-001 contains schema variation across model evaluation files.

M-000001 explicitly contains:

- `experiment_id`
- `model_id`
- `model_family`
- `judgment_scale`
- `per_query`
- `metrics`

M-000002 and M-000003 use an `evaluation` field for experiment
identity and omit `model_family` and `judgment_scale`.

The frozen T-7 contract therefore represents a reconciled canonical
schema and does not claim identical historical serialization.

## Evaluation evidence

Validated historical evaluation artifacts:

- `experiments/embedding/EXP-4B5-001/M-000001_evaluation.json`
- `experiments/embedding/EXP-4B5-001/M-000002_evaluation.json`
- `experiments/embedding/EXP-4B5-001/M-000003_evaluation.json`

The evaluation corpus contains:

- 25 queries
- fixed relevance judgments
- three candidate embedding models
- per-query evaluation results
- aggregate retrieval metrics

Observed aggregate metric family:

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

## Implementation

Canonical implementation:

`src/embedding/evaluation_interface.py`

Implementation requirements:

- frozen dataclass
- exact canonical field order
- immutable instance
- preservation of evaluation identity
- preservation of per-query results
- preservation of aggregate metrics

## Boundary

T-7 does not:

- generate embeddings
- perform vector storage
- perform cosine similarity
- perform runtime retrieval
- perform runtime ranking
- mutate KnowledgeRecords
- traverse the relationship graph
- perform RAG synthesis
- select a production embedding model

## Upstream protection

This freeze does not modify:

- I-2
- I-3
- I-4
- I-5
- I-6

T-7 consumes evaluation evidence at the evaluation boundary and
remains separate from runtime retrieval.

## Production-model status

No production embedding model is selected by T-7.

The existing model-selection decision remains:

`NOT_SELECTED`

## Validation basis

T-7 freeze is based on:

- reconciled design validation
- validation provenance gate
- implementation structural validation
- annotation-origin validation
- real historical artifact evidence validation
- canonical reconstruction validation
- independent pre-freeze contract gate

The independent pre-freeze contract gate passed:

`36/36 checks`

## Freeze condition

This manifest records the intended frozen contract.

Final freeze remains subject to an independent post-manifest
freeze validation gate.

## Status

`FROZEN_VALIDATED`

## Contract version

`0.2`
