# AM-PKO Relationship Substrate Contract

**Status:** DRAFT
**Contract version:** 0.1-design

## 1. Purpose

Provide an authoritative machine-readable substrate for explicit semantic
relationships between existing KnowledgeRecords.

This contract does not create a new KnowledgeRecord type and does not redefine
epistemic authority, lifecycle lineage, retrieval, or Context Assembly.

## 2. Canonical Relationship Vocabulary

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

A relationship type MUST belong to this vocabulary.

## 3. Minimal Representation

A relationship consists of:

- source: KnowledgeRecord identity
- type: canonical relationship type
- target: KnowledgeRecord identity

The EXP-4B6 corpus establishes the record-local serialization precedent:

```json
{"type":"related_to","target":"K-000105"}

## 4. Identity

For the current design, a relationship is addressable by the tuple:

`(source, type, target)`

No independent relationship identifier is required by this draft.

Whether a standalone relationship identifier is needed remains an open design
question and MUST NOT be assumed by downstream implementation.

## 5. Directionality

Relationship direction MUST be preserved.

For a relationship:

`source -> type -> target`

the source and target MUST NOT be silently exchanged.

A relationship MUST NOT be inferred solely from retrieval similarity.

## 6. Resolution Requirements

A concrete implementation MUST establish, at minimum:

1. source resolves to an existing KnowledgeRecord;
2. target resolves to an existing KnowledgeRecord;
3. relationship type belongs to the canonical vocabulary;
4. relationship direction is preserved.

Failure to establish required identity or type validity MUST NOT be silently
treated as a valid relationship.

## 7. Relationship Semantics

The substrate stores explicit semantic relationships.

It MUST NOT infer a relationship merely because:

- two records are retrieval neighbors;
- two records have similar embeddings;
- two records appear in the same ContextPackage;
- one record is authoritative;
- one record is derived from another.

Explicit semantic relationships remain distinct from retrieval relevance.

The normative semantic definitions for the exercised relationship types are
established by the separately validated artifact:

`architecture/relationship-semantics-design-001.md`

Validation authority:
`architecture/relationship-semantics-validation-001.json`

That semantic artifact establishes validated candidate semantics for the
exercised relationship types and explicitly preserves the unresolved status
of the unexercised types.

The substrate MUST consume relationship semantics only as established by that
validated semantic artifact. It MUST NOT invent additional semantic meanings,
endpoint rules, inverse relationships, or relationship assertions.

This semantic validation does not by itself authorize implementation or freeze
of this substrate contract.

## 8. Contradiction Preservation

`contradicts` is an explicit semantic relationship.

The substrate MUST preserve an explicit contradiction relationship when it is
present and valid.

The substrate MUST NOT:

- remove a contradiction because another record has higher retrieval score;
- convert contradiction into agreement;
- resolve contradiction by selecting one record;
- synthesize consensus.

Contradiction handling during Context Assembly remains governed by the I-8/T-8
contract.

## 9. Authority Separation

Relationships do not create, establish, or promote epistemic authority.

A relationship MUST NOT by itself establish:

- VERIFIED authority;
- SUPERSEDED authority;
- RETRACTED authority;
- ADMISSIBLE status;
- INADMISSIBLE status.

Authority remains governed by the AM-PKO authority and lineage architecture.

## 10. Lifecycle Lineage Separation

Semantic relationships MUST remain distinct from lifecycle lineage.

In particular:

- `derived_from` MUST NOT be interpreted as `supersedes`;
- `supports` MUST NOT be interpreted as a lifecycle transition;
- `contradicts` MUST NOT be interpreted as retraction;
- semantic relationships MUST NOT silently create historical replacement.

Lifecycle lineage remains governed separately by the authority-lineage
contract, including explicit lifecycle relations such as:

- `supersedes`
- `split_from`
- `merged_into`

## 11. KnowledgeRecord Boundary

The relationship substrate MUST NOT modify the frozen KnowledgeRecord contract
merely to provide relationship storage.

The substrate MAY resolve relationships associated with KnowledgeRecords, but
the authoritative KnowledgeRecord identity and contract remain external to
this substrate.

## 12. Provenance and Validation Boundary

This draft does not establish a new edge-level provenance or validation
schema.

Relationship provenance and validation MUST NOT be fabricated merely to
complete the substrate representation.

Whether relationship-level provenance and validation belong inside this
substrate remains an open design question.

## 13. Duplicate and Self-Link Policy

This draft does not establish a normative policy regarding:

- duplicate `(source, type, target)` relationships;
- self-links where `source == target`.

EXP-4B6 empirically contains no duplicate edges and no self-links, but that
observation is not promoted to a normative architectural constraint by this
draft.

Any future restriction MUST be explicitly specified and validated.

## 14. Inverse Relationships

This draft does not require materialized inverse relationships.

Whether inverse relationships are:

- materialized;
- derived at query time; or
- unnecessary

remains an open design question.

No inverse relationship may be silently fabricated unless its semantics are
explicitly established.

## 15. I-8 Relationship

I-8 Context Assembly may consume explicit relationships from this substrate.

I-8 MUST NOT infer relationship edges from retrieval similarity.

I-8 MUST preserve valid explicit relationship identity, direction, type, and
applicable provenance/validation information when those structures are
available.

Relationship traversal and subgraph construction remain implementation
responsibilities of I-8 and are not defined by this substrate contract.

## 16. Frozen Boundary Protection

This contract MUST NOT modify merely to accommodate relationship storage:

- KnowledgeRecord;
- frozen T-5 QueryRequest;
- frozen T-6 RankedResult;
- frozen I-6 RetrievalService;
- frozen T-7 EvaluationRun;
- the authority-lineage contract;
- the production embedding-model selection;
- persistent vector-store selection.

## 17. Architectural Constraints

The relationship substrate MUST NOT:

- perform semantic search;
- calculate embedding similarity;
- rank retrieval results;
- establish epistemic authority;
- perform lifecycle promotion;
- replace lifecycle lineage;
- mutate KnowledgeRecords;
- modify frozen T-5;
- modify frozen T-6;
- modify frozen I-6;
- perform Context Assembly;
- generate natural-language answers;
- perform LLM reasoning;
- silently resolve contradictions.

## 18. Evidence Basis

The current design is grounded in:

1. `docs/relationship-model.md`, which establishes the explicit relationship
   vocabulary and directional relationship concept;
2. `docs/architecture.md`, which establishes relationships as explicit
   structured connections governed by compatibility rules;
3. `docs/table-1-consistent-theme.md`, which establishes that relationship
   types have distinct semantic contracts;
4. EXP-4B6 corpus serialization, which establishes the record-local
   `{type,target}` representation precedent;
5. `architecture/authority-lineage-contract.md`, which separates semantic
   relationships from lifecycle lineage;
6. `architecture/context-assembly-contract.md`, which requires explicit
   relationship preservation and prohibits similarity-derived relationship
   inference.

These sources establish the evidence basis for this draft but do not by
themselves authorize implementation or freezing.

## 19. Open Design Questions

The following remain unresolved:

1. Is a standalone runtime RelationshipRecord type required?
2. Is an independent relationship identifier required?
3. Must relationship provenance be stored at edge level?
4. Must relationship validation state be stored at edge level?
5. Are duplicate `(source,type,target)` edges permitted?
6. Are self-links permitted?
7. Should inverse relationships be materialized or derived?
8. What additional normative endpoint compatibility rules, if any, are required
   beyond the validated semantic definitions?
9. What authority is responsible for creating, revising, validating, and
   retracting relationships?

No implementation decision is authorized by this draft.

## 20. Compatibility Decision

**Status:** VALIDATED_DRAFT

The relationship semantic definitions referenced by §7 have been separately
validated by `RELATIONSHIP_SEMANTICS_VALIDATION_001`.

This does not constitute implementation authorization or freeze authorization
for the relationship substrate.

The remaining open design questions in §19 remain unresolved. In particular,
no standalone RelationshipRecord requirement, independent relationship ID,
edge-level provenance/validation schema, duplicate/self-link policy, inverse
materialization policy, additional endpoint compatibility rules, or
relationship governance authority is established by this contract.

Implementation and freeze decisions require explicit review of the remaining
open design questions and a subsequent validation decision for this contract.
