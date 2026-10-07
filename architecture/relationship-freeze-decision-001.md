# AM-PKO Relationship Layer — Explicit Freeze Decision

**Status:** DRAFT
**Version:** 0.1
**Decision ID:** RELATIONSHIP_FREEZE_DECISION_001

## 1. Purpose

This document records the explicit review and decision boundary for the AM-PKO
relationship layer.

It does not itself imply that the relationship semantics, substrate,
admissibility design, or Context Assembly contract are frozen.

## 2. Reviewed Artifacts

- `architecture/relationship-semantics-design-001.md`
- `architecture/relationship-semantics-validation-001.json`
- `architecture/relationship-substrate-contract.md`
- `architecture/relationship-substrate-contract-validation-001.json`
- `architecture/relationship-substrate-contract-validation-002.json`
- `architecture/relationship-admissibility-design-001.md`
- `architecture/relationship-admissibility-validation-001.json`
- `architecture/context-assembly-contract.md`

## 3. Validation State

| Area | Validation State | Freeze State | Implementation State |
|---|---|---|---|
| Relationship semantics | VALIDATED_DRAFT | NOT_FROZEN | NOT_AUTHORIZED |
| Relationship substrate | VALIDATED_DRAFT | NOT_FROZEN | NOT_AUTHORIZED |
| Relationship admissibility | VALIDATED_DRAFT | NOT_FROZEN | NOT_AUTHORIZED |
| Context Assembly relationship handling | DRAFT | NOT_FROZEN | NOT_AUTHORIZED |

## 4. Evidence Baseline

The freeze review relies on the following already-produced validation
artifacts. These artifacts establish validation readiness but do not themselves
authorize freeze or runtime implementation.

| Validation Artifact | Status | Freeze | Implementation |
|---|---|---|---|
| `relationship-semantics-validation-001.json` | VALIDATED_DRAFT | NOT_FROZEN | NOT_AUTHORIZED_BY_THIS_ARTIFACT |
| `relationship-substrate-contract-validation-002.json` | VALIDATED_DRAFT | NOT_FROZEN | NOT_AUTHORIZED_BY_THIS_ARTIFACT |
| `relationship-admissibility-validation-001.json` | VALIDATED_DRAFT | NOT_FROZEN | NOT_AUTHORIZED_BY_THIS_ARTIFACT |

Artifact hashes:

- Relationship semantics: `558b81015c2eb6c2a5705cc24138c8c86f6f9e266b02688cb0959e0d3e627624`
- Relationship substrate: `ea06a7077c686aad4ba34afcb291501c0bca5ab2fda66790d2b4a28547634dca`
- Relationship admissibility: `c4caebcdde38a75144d5bae58fa7f91b4dc380b3b48ad5d33fe7e54c7db21204`

The freeze decision MUST NOT be interpreted as retroactively changing the
validation result of any reviewed artifact.

## 5. Decision Questions

### 5.1 Relationship Semantics

**Decision:** [PENDING]

Questions:

- Are the exercised predicate semantics sufficiently validated?
- Are directionality rules sufficiently validated?
- Are neighboring predicate distinctions sufficiently validated?
- Are unexercised predicates explicitly preserved as undefined?
- Are endpoint compatibility requirements sufficiently determined?

### 5.2 Relationship Substrate

**Decision:** [PENDING]

Questions:

- Is the `(source, type, target)` addressability model sufficient?
- Is a standalone RelationshipRecord required?
- Is an independent relationship identifier required?
- Is edge-level provenance required?
- Is edge-level validation state required?
- Are duplicate relationships permitted, rejected, or otherwise governed?
- Are self-links permitted, rejected, or predicate-specific?
- Are inverse relationships materialized, derived, or unnecessary?
- Who governs relationship creation, revision, validation, and retraction?

### 5.3 Relationship Admissibility

**Decision:** [PENDING]

Questions:

- Is the Contract → Constraints → Validation → Admissibility sequence
  sufficiently defined?
- Is fail-closed execution sufficiently explicit?
- Are contextual constraints sufficiently defined?
- Are unexercised predicates correctly prevented from receiving invented
  admissibility rules?

### 5.4 Context Assembly / I-8

**Decision:** [PENDING]

Questions:

- Is relationship traversal sufficiently bounded?
- Is relationship addressability sufficiently defined without requiring an
  independent relationship ID?
- Does I-8 consume only explicit relationships?
- Does I-8 preserve relationship direction and available provenance/validation?
- Does I-8 preserve contradiction edges?
- Are retrieval relevance and epistemic authority kept separate?

## 6. Unexercised Predicate Gate

The following predicates remain undefined:

- `part_of`
- `caused_by`
- `mitigates`
- `validates`

No normative semantics or admissibility rules are established for them by this
document.

Before any such predicate becomes executable, its validation must establish:

1. normative semantic definition;
2. representative repository-native evidence or explicitly validated design
   basis;
3. source/target direction;
4. distinction from neighboring predicates;
5. endpoint compatibility requirements;
6. defensible semantic basis for assertions;
7. separation from epistemic authority;
8. separation from lifecycle lineage;
9. compatibility with I-8's validated-semantics-only boundary.

## 7. Architectural Constraints

The following constraints MUST remain preserved unless explicitly reviewed
and revalidated:

- KnowledgeRecord identity and contract;
- frozen T-5 QueryRequest;
- frozen T-6 RankedResult;
- frozen I-6 RetrievalService;
- validated authority/admissibility semantics;
- lifecycle lineage separation;
- explicit relationship direction;
- no relationship inference from retrieval similarity;
- fail-closed treatment of `UNDETERMINED`;
- no fabricated relationship provenance or validation;
- no silent inverse relationship fabrication.

## 8. Evidence Reviewed

The following evidence is included in the explicit freeze review.

### 8.1 Validation Artifacts

- `RELATIONSHIP_SEMANTICS_VALIDATION_001`
  - artifact: `architecture/relationship-semantics-validation-001.json`
  - status: `VALIDATED_DRAFT`
  - checks: `17/17`
  - freeze: `NOT_FROZEN`
  - implementation: `NOT_AUTHORIZED_BY_THIS_ARTIFACT`
  - next gate: `EXPLICIT_REVIEW_AND_FREEZE_DECISION`

- `architecture/relationship-substrate-contract-validation-002.json`
  - status: `VALIDATED_DRAFT`
  - checks: `27/27`
  - freeze: `DEFERRED`
  - implementation: `NOT_AUTHORIZED`
  - next gate: `EXPLICIT_REVIEW_OF_REMAINING_OPEN_DESIGN_QUESTIONS`

- `RELATIONSHIP_ADMISSIBILITY_VALIDATION_001`
  - artifact: `architecture/relationship-admissibility-validation-001.json`
  - status: `VALIDATED_DRAFT`
  - checks: `9/9`
  - freeze: `NOT_FROZEN`
  - implementation: `NOT_AUTHORIZED_BY_THIS_ARTIFACT`
  - next gate: `EXPLICIT_REVIEW_AND_FREEZE_DECISION`

### 8.2 Reviewed Artifact Hashes

- relationship semantics design:
  `558b81015c2eb6c2a5705cc24138c8c86f6f9e266b02688cb0959e0d3e627624`
- relationship substrate contract:
  `ea06a7077c686aad4ba34afcb291501c0bca5ab2fda66790d2b4a28547634dca`
- relationship admissibility design:
  `c4caebcdde38a75144d5bae58fa7f91b4dc380b3b48ad5d33fe7e54c7db21204`

### 8.3 EXP-4B6 Relationship Corpus Evidence

The reviewed corpus contains:

- 50 KnowledgeRecords;
- 125 explicit relationship edges;
- `supports`: 23;
- `contradicts`: 6;
- `depends_on`: 21;
- `derived_from`: 2;
- `related_to`: 72;
- `requires`: 1;
- unexercised predicates: `part_of`, `caused_by`, `mitigates`, `validates`.

Observed structural properties include:

- 125 unique `(source, type, target)` triples;
- 0 duplicate triples in the reviewed corpus;
- 0 self-links in the reviewed corpus;
- 0 unknown relationship types;
- 0 missing relationship targets;
- 23 reciprocal relationship pairs occur;
- 11 are same-type reciprocal pairs (`related_to`↔`related_to`: 9; `supports`↔`supports`: 2);
- 12 are different-type reciprocal pairs.

These empirical observations describe the reviewed corpus only. They do not establish normative duplicate, self-link, inverse, provenance, validation, or governance policies.

### 8.4 Predicate-Semantics Evidence

The relationship-semantics validation established 17/17 checks, including:

- exercised predicates have corpus evidence;
- unexercised predicates remain undefined;
- neighboring predicate distinctions are preserved;
- relationship direction is preserved;
- retrieval similarity is not treated as `related_to`;
- authority is not created by a relationship;
- lifecycle lineage is separated from semantic relationships;
- relationship assertions require a defensible semantic basis;
- I-8 must consume only validated relationship semantics.

### 8.5 Endpoint-Compatibility Evidence

Corpus evidence demonstrates predicate-specific endpoint usage across the five KnowledgeRecord types.

The review does not establish a universal 5x5 knowledge-type compatibility matrix. Endpoint compatibility therefore remains contextual and predicate-specific unless separately defined and validated.

### 8.6 Repository-Native Examples

The reviewed repository contains concrete relationship evidence, including:

- `requires(K-000124, K-000123)` as an explicit prerequisite relationship;
- `supports`, `depends_on`, `derived_from`, `contradicts`, `related_to`, and `requires` examples in the EXP-4B6 corpus;
- relationship objects currently represented with `{type, target}` under a source KnowledgeRecord.

No repository-native precedent was identified that establishes a standalone semantic `RelationshipRecord`, independent relationship identifier, edge-level provenance schema, or edge-level validation schema.

### 8.7 Context Assembly Evidence

The I-8 Context Assembly contract explicitly defines relationship addressability through:

`(source, type, target)`

I-8 is required to preserve source, target, type, and direction, while not requiring or synthesizing an independent relationship identifier where none is provided by the authoritative substrate.

I-8 traversal is restricted to explicit relationships in the authoritative relationship substrate. Retrieval similarity, embedding proximity, lexical similarity, co-occurrence, and ContextPackage membership cannot create traversal edges.

### 8.8 Architectural Constraint Evidence

The review preserves the existing boundaries:

- frozen KnowledgeRecord and retrieval contracts remain unchanged;
- authority/admissibility remains separate from relationship semantics;
- lifecycle lineage remains separate from semantic relationships;
- `UNDETERMINED` remains fail-closed;
- retrieval relevance is not authority;
- relationship direction is preserved;
- contradiction edges are preserved;
- relationship provenance or validation must not be fabricated;
- unexercised predicate semantics and admissibility rules must not be invented;
- no runtime implementation is authorized by the reviewed validation artifacts.

### 8.9 Remaining Design Questions

The evidence does not yet resolve:

1. standalone runtime `RelationshipRecord`;
2. independent relationship identifier;
3. relationship-level provenance;
4. relationship-level validation state;
5. duplicate assertion policy;
6. self-link policy;
7. inverse relationship policy;
8. relationship governance authority;
9. additional endpoint-compatibility constraints.

These questions remain subject to explicit decision and subsequent validation before any corresponding rule becomes normative or implementation-authorizing.

## 9. Open Questions

The following relationship-layer questions remain explicitly open unless and
until a final decision records otherwise:

1. Is a standalone runtime `RelationshipRecord` required?
2. Is an independent relationship identifier required?
3. Is relationship-level provenance required?
4. Is relationship-level validation state required?
5. What is the normative policy for duplicate `(source, type, target)` assertions?
6. What is the normative policy for self-links?
7. Are inverse relationships materialized, derived at query time, or unnecessary?
8. What authority governs relationship creation, revision, validation, and retraction?
9. Are additional endpoint-compatibility constraints required beyond the
   validated predicate semantics?

No open question may be treated as resolved merely because empirical corpus
evidence currently contains no counterexample.

Any resolution MUST be explicit, evidence-backed, and validated before it
becomes normative or implementation-authorizing.

## 10. Decision

**Validation Result:** VALIDATED_DRAFT
**Freeze Decision:** DEFERRED
**Implementation Decision:** NOT_AUTHORIZED_BY_THIS_ARTIFACT

**Reason:** The reviewed relationship-layer evidence passes the defined validation gates and establishes contract readiness only. The remaining explicit design questions are not resolved by the current evidence; therefore formal freeze, runtime implementation, and relationship-promotion authority remain separate lifecycle decisions.

## 11. Authorization Boundary

No runtime implementation, schema promotion, relationship lifecycle
mechanism, independent relationship identifier, edge-level provenance model,
edge-level validation model, duplicate policy, self-link policy, inverse
materialization policy, or governance mechanism is authorized merely by this
template.

A final decision requires explicit review, completed evidence references, and
a subsequent validation/authorization decision where applicable.
