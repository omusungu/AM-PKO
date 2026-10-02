# AM-PKO EXP-4B6-001 Query Authoring Specification

**Experiment:** EXP-4B6-001  
**Status:** DESIGN  
**Query authoring version:** 0.1-design  
**Corpus dependency:** Frozen EXP-4B6 corpus v0.1

## 1. Purpose

Define controlled rules for authoring the substantive 50-query evaluation set without modifying the frozen corpus or allowing model results to influence query wording.

## 2. Primary Rule

Each query must represent a plausible human knowledge need and must require retrieval from the frozen corpus to identify useful records.

Queries must not simply copy record titles or reproduce record content.

## 3. Query-to-Record Allocation

Each query initially targets one primary corpus record according to the frozen query skeleton.

The primary target is an evaluation reference, not an instruction to the retrieval system.

Additional relevant records may be added when the query genuinely requires multiple records, especially for contradiction, ambiguity, relationship-dependent, and cross-domain cases.

## 4. Direct Queries

Direct queries should seek a clearly identifiable knowledge item.

They should test whether the intended record is retrievable from its meaning rather than from copied title wording.

## 5. Ambiguous Queries

Ambiguous queries must contain genuine contextual or semantic uncertainty.

At least two corpus records should be plausible candidates where appropriate.

The ambiguity must be resolvable through retrieved context, provenance, relationships, or distinctions in meaning.

## 6. Semantic-Overlap Queries

Semantic-overlap queries must distinguish related records whose meanings, purposes, knowledge types, or contexts differ.

Avoid relying solely on identical terminology.

The query should test whether retrieval preserves meaningful distinctions between similar knowledge.

## 7. Contradiction Queries

Contradiction queries must test whether competing propositions remain independently retrievable.

Where the corpus contains a documented contradiction, the relevant set should normally include both competing records when the query calls for comparison.

The query must not resolve the contradiction in advance.

## 8. Relationship-Dependent Queries

Relationship-dependent queries must require the user to connect more than one knowledge record or understand a meaningful dependency, support, derivation, or related relationship.

Do not place the entire relationship chain directly into the query.

## 9. Cross-Domain Queries

Cross-domain queries must connect knowledge across domains while preserving domain-specific meaning.

They must not assume that similar concepts have identical definitions or evidence standards.

## 10. Query Wording

Queries should:

- use natural human language;
- express a genuine information need;
- avoid unnecessary technical jargon;
- avoid candidate model names;
- avoid embedding terminology unless the knowledge need genuinely concerns embeddings;
- avoid metric names unless the query genuinely concerns evaluation;
- avoid artificial keyword stuffing;
- avoid exact copying of corpus titles;
- avoid revealing the intended record ID.

## 11. Rationale

Every query must include a concise rationale explaining why the query represents its assigned query class and why its target record or records are relevant.

The rationale is evaluation metadata and is not submitted as the retrieval query.

## 12. Independence From Evaluation Results

Queries must be authored before embedding-model evaluation.

Query wording must not be changed because a candidate model retrieves an unexpected result.

Judgments must be created independently after substantive query authoring.

Any later query modification requires an explicit revision and validation record.

## 13. Human Utility

Queries should represent situations in which a person would reasonably want to:

- find a known piece of knowledge;
- distinguish between similar knowledge;
- investigate uncertainty;
- compare competing claims;
- follow a relationship between records;
- connect knowledge across domains.

## 14. Provenance and Identity

Queries should sometimes require retrieved records to be distinguished by provenance, knowledge type, context, or identity.

The query itself should not contain information that makes the answer trivial.

## 15. Model Neutrality

No query may:

- name BGE-M3;
- name E5;
- name Qwen;
- request a particular embedding model;
- encode model-specific behavior;
- request a ranking outcome;
- contain evaluation results.

## 16. Corpus Protection

Query authoring must not modify:

- `corpus.json`;
- corpus validation artifacts;
- corpus freeze manifest;
- I-2;
- I-3;
- I-4;
- I-5;
- I-6;
- T-5;
- T-6;
- T-7;
- Contract Graph.

## 17. Judgment Separation

Query authoring determines the information need and candidate relevance targets.

It does not assign relevance grades.

Relevance judgments will be created as a separate artifact after query authoring and validation.

## 18. Lifecycle

The query set follows:

`GENERATED_SKELETON → AUTHORING → GENERATED → VALIDATED → FROZEN`

Only the frozen query set may be used for comparative embedding evaluation.

## 19. Exit Criteria

Query authoring is complete only when:

- all 50 queries contain substantive wording;
- every query has a rationale;
- all six query classes are represented;
- query IDs remain unchanged;
- target IDs reference frozen corpus records;
- no corpus record is modified;
- no model-specific language is present;
- contradiction queries preserve competing propositions;
- ambiguity queries represent genuine ambiguity;
- semantic-overlap queries distinguish related meanings;
- relationship-dependent queries require meaningful relationships;
- cross-domain queries preserve domain distinctions.

**Current state: DESIGN ONLY.**
