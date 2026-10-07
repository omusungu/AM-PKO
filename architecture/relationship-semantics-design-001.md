# AM-PKO Relationship Semantics Design

**Status:** PROPOSED
**Version:** 0.1
**Validation Status:** NOT_VALIDATED
**Implementation Status:** NOT_AUTHORIZED

## 1. Purpose

This document proposes semantic definitions for relationship types exercised by the current AM-PKO corpus.

These definitions are design candidates only. They do not modify the canonical relationship vocabulary, authorize implementation, or freeze relationship semantics.

## 2. Evidence Boundary

The proposals are derived from repository-native evidence in:

1. `docs/relationship-model.md`
2. `docs/architecture.md`
3. `docs/table-1-consistent-theme.md`
4. `architecture/authority-lineage-contract.md`
5. `architecture/relationship-substrate-contract.md`
6. `experiments/embedding/EXP-4B6-001/corpus.json`

Currently exercised:
- `supports`
- `contradicts`
- `depends_on`
- `derived_from`
- `related_to`
- `requires`

Currently unexercised:
- `part_of`
- `caused_by`
- `mitigates`
- `validates`

No normative definitions are proposed for the four unexercised types in this version.

## 3. Candidate Semantic Predicates

### 3.1 supports

`supports(S,T)` means the knowledge represented by source `S` provides substantive evidential, explanatory, experiential, or conceptual basis that strengthens or contributes to the credibility, applicability, or understanding of target `T`.

It does not independently establish authority or verification.

### 3.2 contradicts

`contradicts(S,T)` means the knowledge represented by source `S` asserts a proposition, interpretation, condition, or conclusion incompatible with one represented by target `T` under the relevant context.

It does not independently retract, supersede, invalidate, or establish authority for either record.

### 3.3 depends_on

`depends_on(S,T)` means the correctness, interpretation, applicability, construction, or use of source `S` depends materially on knowledge represented by target `T`.

It is not merely a generic association.

### 3.4 derived_from

`derived_from(S,T)` means the knowledge represented by source `S` was developed, produced, or obtained from target `T` as an originating basis.

It does not imply `supersedes(S,T)` or any authority or lifecycle transition.

### 3.5 related_to

`related_to(S,T)` means source `S` has a meaningful semantic association with target `T` without asserting the stronger semantics of support, contradiction, dependency, derivation, or requirement.

It must not be created merely because records were retrieved together or are lexically similar.

### 3.6 requires

`requires(S,T)` means source `S` explicitly declares target `T` as a prerequisite for the intended completion, application, or use represented by `S`.

`requires` is not restricted to physical or operational resources and must not automatically be treated as synonymous with `depends_on`. Whether a `requires` edge also constitutes a `depends_on` edge remains unresolved.

## 4. Directionality

For every candidate predicate:

`S --relationship--> T`

Source and target positions are semantically significant.

Implementations must not reverse or swap them unless an explicit inverse rule is separately validated.

An independently authored reverse edge, where present, is not evidence that the predicate itself is symmetric.

## 5. Non-Implications

No candidate predicate independently establishes:

- authority;
- admissibility;
- verification;
- supersession;
- retraction;
- lifecycle transition;
- contradiction resolution;
- semantic truth.

## 6. Endpoint Compatibility

This version does not define a normative endpoint compatibility matrix.

`knowledge_type` metadata may participate in future validation, but relationship validity must not be determined solely from knowledge type.

The represented knowledge of the source and target remains the primary semantic subject.

## 7. Unresolved Vocabulary

No definitions are proposed here for:

- `part_of`
- `caused_by`
- `mitigates`
- `validates`

These require repository-native evidence or explicitly validated semantic design before implementation.

## 8. Validation Gate

Before these definitions become normative:

1. Each predicate must be reviewed against representative corpus examples.
2. Source/target direction must be validated.
3. Distinctions between neighboring predicates must be validated.
4. Endpoint compatibility requirements must be explicitly determined.
5. Contradiction semantics must remain compatible with the authority-lineage contract.
6. Lifecycle lineage must remain separate from semantic relationships.
7. I-8 traversal must consume only validated semantics.
8. A subsequent validation artifact must authorize implementation and/or freeze.

**Decision:** PROPOSED ONLY. No implementation or freeze authorized.
