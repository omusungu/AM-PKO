# AM-PKO EXP-4B6-001 — Record Authoring Specification

**Status:** DESIGN
**Specification version:** 0.1-design

## 1. Purpose

Define controlled authoring rules for the 50 substantive KnowledgeRecords in
EXP-4B6-001 before corpus validation and query construction.

The specification preserves model neutrality, ontological completeness,
provenance, semantic diversity, relationship structure, contradiction
visibility, and reproducibility.

## 2. Authoring Principle

Each record must represent one meaningful unit of personal knowledge.

Records must be authored for knowledge quality, not for optimization toward any
specific embedding model, retrieval algorithm, or expected query result.

## 3. Canonical Record Fields

Every completed record must contain:

- id
- domain
- project
- knowledge_type
- topic
- granularity
- title
- content
- status
- source
- skills
- assets
- actions
- relationships
- metadata

## 4. Substantive Content Rules

### 4.1 Identity

Each record must have a stable unique identifier assigned by the allocation
matrix.

IDs must not be changed during authoring.

### 4.2 Domain and Project

Domain and project must remain consistent with the allocation matrix unless an
explicit design correction is recorded before corpus freeze.

### 4.3 Knowledge Type

The assigned knowledge_type must be preserved.

The content must genuinely reflect its assigned type:

- FACT — asserted knowledge intended as factual.
- EXPERIENCE — knowledge grounded in observed or lived experience.
- IDEA — proposed or exploratory conception.
- PLAN — intended future action or procedure.
- ANALYSIS — reasoned interpretation or finding.

### 4.4 Granularity

The assigned granularity must be preserved.

Content must match the intended granularity rather than merely using its label.

### 4.5 Topic

Topic must be specific enough to distinguish the record from neighboring
records while allowing intentional semantic overlap where assigned.

### 4.6 Title

Titles should be concise and descriptive.

Titles must not contain artificial retrieval keywords, model names, or query
phrases inserted solely to improve retrieval.

### 4.7 Content

Content should contain the actual knowledge claim, experience, idea, plan, or
analysis represented by the record.

Content should be sufficiently specific to stand on its own.

Avoid:

- filler text
- generic statements
- duplicated prose
- artificial keyword stuffing
- embedding-oriented phrasing
- references to this experiment
- references to candidate embedding models
- fabricated precision

Where appropriate, content may contain:

- conditions
- observations
- causes
- consequences
- limitations
- examples
- practical implications
- uncertainty
- competing interpretations

### 4.8 Contradictions

Contradictory records must preserve the disagreement explicitly.

Do not silently reconcile, merge, or rewrite contradictory knowledge into a
single conclusion.

Each contradiction must remain independently inspectable and traceable.

### 4.9 Ambiguity

Ambiguous records must contain genuine contextual ambiguity.

Ambiguity must not be created by making the text vague or meaningless.

The ambiguity should arise from plausible alternative interpretations, related
concepts, overlapping terminology, or insufficient context that a retrieval
system must distinguish.

### 4.10 Semantic Overlap

Semantic-overlap records should share meaningful concepts with other records
while retaining distinct identities, claims, experiences, or implications.

Overlap must be substantive rather than duplicated wording.

## 5. Provenance Rules

Every completed record must contain an explicit source object.

Source type must use an allowed AM-PKO source category.

The source reference must identify the origin sufficiently for human
inspection.

Where the knowledge is reconstructed from personal context, the source must
identify that provenance honestly rather than presenting reconstruction as
external evidence.

No fabricated external citation may be introduced.

## 6. Skills, Assets, and Actions

These fields should describe genuine relationships between the knowledge and
its practical application.

Use empty arrays only when a field is genuinely not applicable.

Do not add items solely to satisfy a count.

## 7. Relationship Rules

Relationships must use canonical AM-PKO relationship types.

Relationship targets must reference stable record IDs.

Relationship semantics must be explicit.

Required relationship roles from the allocation matrix must be implemented
during authoring.

Relationship chains should form meaningful multi-record structures rather than
isolated links.

Cross-domain relationships must represent genuine conceptual or practical
connections.

Historical/superseding relationships must preserve temporal distinction
rather than erasing the earlier record.

## 8. Metadata Rules

Metadata must preserve record version and creation information.

Cluster assignment must remain traceable.

Experiment-specific metadata must not contaminate the substantive knowledge
content.

## 9. Status Lifecycle

During authoring:

RAW → REVIEWED → VALIDATED → FROZEN

Records must not be marked VALIDATED or FROZEN merely because they have been
written.

Validation must occur through explicit corpus gates.

## 10. Model Neutrality

The corpus must not be authored against:

- BGE-M3
- E5
- Qwen3-Embedding
- any other embedding model
- a particular tokenizer
- a particular vector dimension
- a particular retrieval implementation

No candidate model may influence substantive wording.

## 11. Query Independence

Queries must be authored only after the corpus has passed its substantive
validation gate.

Queries must not be derived from model-generated retrieval results.

Judgments must be established independently before comparative model
evaluation.

## 12. Human Utility

Records should be understandable to a knowledgeable human without requiring
knowledge of the experiment implementation.

A human evaluator should be able to determine:

- what the record means
- where it came from
- what type of knowledge it represents
- how it relates to other records
- whether it conflicts with another record
- how it could be applied

## 13. Reproducibility

Authoring must preserve:

- stable IDs
- deterministic field structure
- explicit provenance
- explicit relationships
- controlled allocation
- version information

Substantive changes after validation must be recorded rather than silently
overwriting the validated corpus.

## 14. Freeze Protection

Authoring must not modify:

- frozen AM-PKO core contracts
- I-2
- I-3
- I-4
- I-5
- I-6
- T-5
- T-6
- T-7
- Contract Graph frozen artifacts

EXP-4B6 remains an evaluation corpus and does not redefine the AM-PKO core.

## 15. Authoring Sequence

The corpus shall be authored in controlled batches.

Recommended sequence:

1. Cluster A — Welding/Fabrication
2. Cluster B — Theology/Ministry
3. Cluster C — Technology/AM-PKO
4. Cluster D — Heritage/Storytelling
5. Cluster E — Cross-domain/Contradiction

Each batch must be structurally validated before proceeding.

## 16. Completion Gate

Before corpus freeze, verify:

- 50 records present
- all IDs stable and unique
- allocation matrix preserved
- all required fields populated
- knowledge types preserved
- granularities preserved
- provenance present
- relationships valid
- relationship-chain requirements satisfied
- semantic-overlap requirements satisfied
- ambiguity requirements satisfied
- contradiction requirements satisfied
- historical/superseding requirements satisfied
- cross-domain requirements satisfied
- no model-specific optimization
- no fabricated provenance
- no frozen-core modification

## 17. Current State

This specification defines authoring rules only.

No substantive corpus record is frozen by this document.

No embedding generation is authorized by this document.

No query or judgment construction is authorized until the substantive corpus
passes its dedicated validation gate.
