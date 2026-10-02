# AM-PKO EXP-4B6-001 — Corpus Schema & Allocation Plan

**Status: DESIGN**
**Corpus schema plan version: 0.1-design**

## 1. Purpose

Define the exact structural allocation of the 50-record evaluation corpus before
the records themselves are authored.

This plan controls corpus composition, identifier allocation, knowledge-type
coverage, granularity diversity, relationship density, ambiguity, contradiction,
historical/superseding knowledge, cross-domain links, and provenance.

The plan is model-neutral and must be completed before corpus generation.

## 2. Canonical Record Structure

Every record will conform to the AM-PKO KnowledgeRecord structure:

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

Required identity rule:

`id` must be unique and stable within EXP-4B6-001.

Record IDs will use:

`K-000101` through `K-000150`

## 3. Cluster Allocation

| Cluster | Domain | Record IDs | Count |
|---|---|---:|---:|
| A | Welding/Fabrication | K-000101–K-000110 | 10 |
| B | Theology/Ministry | K-000111–K-000120 | 10 |
| C | Technology/AM-PKO | K-000121–K-000130 | 10 |
| D | Heritage/Storytelling | K-000131–K-000140 | 10 |
| E | Cross-domain / Contradiction | K-000141–K-000150 | 10 |

Total: 50 records.

## 4. Knowledge-Type Allocation

Each of the five canonical knowledge types must occur throughout the corpus:

- FACT
- EXPERIENCE
- IDEA
- PLAN
- ANALYSIS

Target distribution:

| Knowledge Type | Target Count |
|---|---:|
| FACT | 10 |
| EXPERIENCE | 10 |
| IDEA | 10 |
| PLAN | 10 |
| ANALYSIS | 10 |

No cluster is required to contain exactly two of each type; allocation should
support realistic semantic variation and the relationship requirements.

## 5. Granularity Allocation

The corpus must collectively contain all of the following canonical granularities:

- Claim
- Observation
- Heuristic
- Procedure
- Hypothesis
- Finding
- Principle
- Pattern
- PlanItem
- Recommendation

Target: at least 4 records representing each granularity, with additional
records allocated according to domain realism.

## 6. Required Special-Property Allocation

The generated corpus must contain at least:

- 10 explicit relationship chains
- 8 semantic-overlap records
- 5 ambiguity records
- 4 explicit contradictory relationships
- 2 historical/superseding relationships
- 6 cross-domain relationships

Special properties may overlap on the same records.

## 7. Relationship Allocation

Relationships must use only canonical AM-PKO relationship types:

- supports
- contradicts
- depends_on
- derived_from
- part_of
- related_to
- caused_by
- mitigates
- requires
- validates

At least 10 relationships must form explicit multi-record chains.

Relationships must be represented by stable record IDs.

No relationship may be invented merely to satisfy a numerical target; each must
have a defensible semantic basis.

## 8. Contradiction Allocation

At least four contradiction relationships must be explicit.

Contradictions must preserve both records as independent knowledge.

A contradiction must not be resolved automatically during corpus construction.

Where appropriate, contradictory records may differ by:

- context
- experience
- interpretation
- time
- evidence
- methodological assumption

## 9. Historical / Superseding Allocation

At least two relationships must represent historical change or supersession.

Historical records remain preserved.

A newer record must not silently overwrite an earlier record.

Temporal metadata must distinguish the records where applicable.

## 10. Semantic-Overlap Allocation

At least eight records must intentionally contain meaningful semantic overlap.

Overlap should include cases where records share concepts but differ in:

- purpose
- domain
- knowledge type
- granularity
- evidence
- conclusion
- context

The overlap must be substantive rather than simple keyword duplication.

## 11. Ambiguity Allocation

At least five records must participate in ambiguity scenarios.

Ambiguity should include concepts whose interpretation depends on context,
domain, relationship structure, or surrounding knowledge.

Ambiguous records must remain independently identifiable.

## 12. Cross-Domain Allocation

At least six explicit cross-domain relationships must connect records across
the five clusters.

Cross-domain links should represent genuine conceptual relationships rather
than artificial numerical padding.

## 13. Provenance Allocation

Every record must contain explicit source/evidence information.

Sources may use the AM-PKO source types appropriate to the record, including:

- conversation
- document
- field_note
- technical_reference
- inspection_report
- checklist
- drawing
- standard
- interview
- observation
- dataset
- brainstorm

Provenance must remain attached to the record throughout evaluation.

## 14. Model-Neutrality Rule

Corpus construction must occur independently of:

- embedding model scores
- retrieval rankings
- candidate-model performance
- production-model selection
- vector-database behavior

No generated retrieval result may be used to rewrite the corpus before the
evaluation inputs are frozen.

## 15. Query Independence

The corpus must be completed and validated before queries are authored.

Queries must not be constructed to favor:

- BGE-M3
- multilingual-e5-large
- Qwen3-Embedding
- any other embedding model

## 16. Judgment Independence

Relevance judgments must be frozen after query construction and before
comparative embedding evaluation.

Judgments must be based on the intended human-use semantics of the corpus,
not on observed model rankings.

## 17. Generation Lifecycle

The controlled lifecycle is:

`DESIGN → GENERATED → VALIDATED → FROZEN`

The schema/allocation plan is currently:

`DESIGN`

The actual 50 records must not be generated until this plan passes validation.

## 18. Architectural Protection

This experiment must not:

- modify frozen I-2
- modify frozen I-3
- modify frozen I-4
- modify frozen I-5
- modify frozen I-6
- modify frozen T-5
- modify frozen T-6
- modify frozen T-7
- freeze T-8
- select a production embedding model
- select a vector database
- replace the Contract Graph
- introduce silent ontology mutation

## 19. Validation Requirement

Before corpus generation, validate:

1. ID allocation
2. cluster allocation
3. knowledge-type coverage
4. granularity coverage
5. relationship requirements
6. contradiction requirements
7. historical/superseding requirements
8. semantic-overlap requirements
9. ambiguity requirements
10. cross-domain requirements
11. provenance requirements
12. model-neutrality requirements
13. query-independence requirements
14. judgment-independence requirements
15. lifecycle controls
16. architectural protection

Only a passing schema/allocation gate authorizes corpus generation.
