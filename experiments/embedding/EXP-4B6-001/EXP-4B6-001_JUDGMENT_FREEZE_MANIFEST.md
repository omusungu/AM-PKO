# AM-PKO EXP-4B6-001 Judgment Freeze Manifest

Experiment: EXP-4B6-001
Judgment artifact: judgments.json
Frozen judgment version: 0.1
Status: FROZEN
Freeze status: FROZEN
Frozen at: 2026-10-02T04:49:24.797379+00:00

## Freeze Basis

- Frozen corpus dependency: PASS
- Frozen query dependency: PASS
- Judgment authoring completeness: PASS
- Judgment validation gate: PASS
- Judgment entries: 50
- Relevance assignments: 102
- Judgment grades: 1 = partially relevant; 2 = highly relevant
- Grade distribution: 1 = 22; 2 = 80
- Model-dependent ranking evidence used for authoring: NONE

## Independence

Judgments were authored as a separate artifact from query construction and are not derived from observed embedding-model rankings.

The judgment artifact remains model-independent.

## Lifecycle Transition

AUTHORING / VALIDATED → 0.1 / FROZEN

The substantive relevance judgments were not modified by this lifecycle transition.

## Freeze Protection

The frozen corpus and frozen query set remain authoritative inputs.

No embedding model was selected by this freeze.

No retrieval ranking was used to alter the judgments.

## Downstream Authorization

Embedding evaluation: AUTHORIZED

## Authority

judgments.json at frozen judgment version 0.1 is authoritative.

Validation artifact:
EXP-4B6-001_JUDGMENT_VALIDATION_001.json

Freeze manifest:
EXP-4B6-001_JUDGMENT_FREEZE_MANIFEST.md
