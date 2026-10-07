# AM-PKO Relationship Admissibility Design

**Status:** PROPOSED
**Version:** 0.1
**Freeze Status:** NOT_FROZEN
**Implementation Decision:** NOT_AUTHORIZED

## 1. Purpose

This artifact specializes the existing AM-PKO admissibility model for explicit semantic relationships between KnowledgeRecords.

It does not create a new KnowledgeRecord type, relationship runtime type, edge-level provenance schema, edge-level validation schema, authority hierarchy, lifecycle relation, inverse relation, or implementation contract.

## 2. Canonical Binding

Relationship admissibility MUST remain a specialization of the existing AM-PKO admissibility model.

Conceptually:

`RelationshipAdmissible(S, ρ, T, C) ∈ { ADMISSIBLE, INADMISSIBLE, UNDETERMINED }`

where:

- `S` is the source KnowledgeRecord;
- `ρ` is a canonical relationship type;
- `T` is the target KnowledgeRecord;
- `C` is the explicitly evaluated context.

The specialization MUST preserve the canonical three-valued admissibility semantics.

## 3. Evaluation Dimensions

A relationship admissibility evaluation MUST establish, as applicable:

1. relationship semantic contract satisfaction;
2. applicable contextual constraints;
3. required validation evidence.

Conceptually:

`RelationshipAdmissible(S, ρ, T, C)`

is ADMISSIBLE only when all required relationship contract, constraint, and validation conditions positively pass.

A definitive failure of a required condition produces INADMISSIBLE.

Insufficient, missing, stale, unresolved, or otherwise inadequate information produces UNDETERMINED unless a definitive failure establishes INADMISSIBLE.

## 4. Evaluation Order

The relationship specialization follows the existing admissibility sequence:

`RelationshipContract(S, ρ, T) → RelationshipConstraints(S, ρ, T, C) → RelationshipValidation(S, ρ, T, C) → RelationshipAdmissible(S, ρ, T, C)`

These are conceptual design terms only. This artifact does not establish new runtime interfaces or schemas for them.

## 5. Semantic Contract Binding

`RelationshipContract(S, ρ, T)` MUST be evaluated against the separately validated relationship semantics.

It MUST NOT substitute:

- retrieval similarity;
- lexical similarity;
- mere co-occurrence;
- knowledge type alone;
- inverse-edge presence;
- authority state;
- lifecycle state.

The ten canonical relationship types remain the validated vocabulary boundary.

## 6. Endpoint Compatibility

Knowledge type alone MUST NOT determine relationship admissibility.

No normative 5×5 source/target knowledge-type compatibility matrix is established by this artifact.

A relationship type MAY impose additional endpoint constraints only where those constraints are explicitly defined and separately validated.

## 7. Authority Separation

Relationship admissibility MUST NOT be interpreted as epistemic authority.

A relationship MUST NOT by itself establish:

- VERIFIED;
- SUPERSEDED;
- RETRACTED;
- epistemic authority;
- current KnowledgeRecord authority.

Relationship admissibility and KnowledgeRecord authority remain separate evaluated dimensions.

## 8. Lifecycle Separation

Relationship admissibility MUST NOT create or imply lifecycle transitions.

In particular:

- `derived_from` MUST NOT imply `supersedes`;
- `supports` MUST NOT imply a lifecycle transition;
- `contradicts` MUST NOT imply retraction;
- relationship admissibility MUST NOT silently create historical replacement.

## 9. Directionality

The evaluation MUST preserve the authored source → relationship → target direction.

No inverse relationship may be inferred merely because a relationship is admissible.

An independently authored reverse relationship remains independently evaluated.

## 10. Undefined Relationship Semantics

The currently unexercised relationship types:

- `part_of`
- `caused_by`
- `mitigates`
- `validates`

MUST NOT receive invented admissibility rules from this artifact.

Their relationship contracts remain undefined pending explicit semantic validation.

## 11. Fail-Closed Rule

For execution, selection, substitution, traversal, or Context Assembly:

`RelationshipExecutionAdmissible(S, ρ, T, C) ⇔ RelationshipAdmissible(S, ρ, T, C) = ADMISSIBLE`

Therefore:

- `UNDETERMINED` → not executable;
- `INADMISSIBLE` → not executable;
- only `ADMISSIBLE` → eligible for the applicable downstream boundary.

No downstream component may reinterpret `UNDETERMINED` as permission.

## 12. Provenance and Validation Boundary

This artifact does not establish edge-level provenance or validation schemas.

Where required relationship-level provenance or validation is unavailable, the admissibility result MUST reflect that insufficiency rather than fabricate evidence.

The design of relationship-level provenance and validation remains an open architectural question.

## 13. I-8 Boundary

I-8 Context Assembly MAY consume relationships that have passed the applicable admissibility boundary.

I-8 MUST NOT infer relationship edges from retrieval similarity.

Relationship traversal, subgraph construction, provenance expansion, contradiction preservation, and resource-budget enforcement remain implementation concerns of I-8 and are not authorized by this artifact.

## 14. Open Questions Preserved

This artifact does not resolve:

- standalone RelationshipRecord;
- independent relationship ID;
- relationship-level provenance;
- relationship-level validation;
- duplicate relationship policy;
- self-link policy;
- inverse materialization;
- relationship governance authority.

## 15. Decision Boundary

This artifact is a design proposal only.

It does not authorize:

- implementation;
- freezing;
- creation of a standalone RelationshipRecord;
- creation of a relationship-specific runtime interface;
- edge-level provenance;
- edge-level validation;
- inverse materialization;
- normative duplicate/self-link policy.

Any implementation or freeze decision requires explicit subsequent validation and review.

