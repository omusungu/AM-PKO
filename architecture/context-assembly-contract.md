# AM-PKO Context Assembly Contract

**Status:** DRAFT
**Version:** 0.1
**Frontier:** Frontier 1
**Contract Family:** I-8 / T-8

## 1. Functional Boundary

Context Assembly is the deterministic, non-generative compiler between
T-6 RankedResult and T-8 ContextPackage.

It packages authoritative, eligible AM-PKO knowledge and its explicit
relationships into a bounded, machine-interpretable context package.

Context Assembly MUST NOT:

- perform semantic search;
- replace I-6 Retrieval;
- rewrite underlying knowledge content;
- summarize source knowledge;
- generate natural-language answers;
- assign epistemic authority;
- silently resolve contradictions.

## 2. Inputs

Context Assembly consumes:

- T-6 RankedResult candidates;
- the current T-5 QueryRequest design;
- declared graph traversal bounds;
- declared resource constraints;
- the active authority policy/profile;
- authoritative ontological and relationship data required to validate
  candidates.

## 3. Output

Context Assembly produces T-8 ContextPackage containing:

- context_id;
- compiled_records;
- provenance_map;
- active_relationship_subgraph;
- epistemic_validation_summary;
- budget_utilization.

## 4. Authority Boundary

Every candidate record MUST undergo the active authority/admissibility
evaluation before compilation.

ADMISSIBLE candidates may proceed.

INADMISSIBLE candidates MUST NOT enter compiled_records.

UNDETERMINED candidates MUST be treated as INADMISSIBLE for compilation
and MUST NOT enter compiled_records.

Excluded candidates MUST remain observable through the
epistemic_validation_summary.

Context Assembly MUST NOT promote a candidate to authority.

## 5. Contradiction Handling

Context Assembly MUST preserve explicit contradiction relationships.

If candidate records A and B are connected by a frozen `contradicts`
relationship:

- both records MAY remain in compiled_records when independently eligible;
- the contradiction edge MUST remain in active_relationship_subgraph;
- the package MUST expose the contradiction to the Reason layer;
- Context Assembly MUST NOT synthesize or imply consensus.

## 6. Determinism

Given identical:

- T-6 candidates;
- the current T-5 QueryRequest design;
- authority policy;
- graph state;
- resource constraints;
- traversal bounds;
- source content and integrity state;

Context Assembly MUST produce an equivalent T-8 ContextPackage.

## 7. Bounded Execution

Assembly MUST enforce declared:

- token/context budget;
- graph traversal depth;
- latency budget;
- applicable compute/cost constraints.

Budget exhaustion MUST NOT silently expand declared limits.

## 8. Provenance

Every compiled record MUST remain traceable to its source identity,
content/integrity state, lineage, and relevant validation state.

Assembly MUST NOT sever provenance when packaging records.

## 9. Frozen Boundary Protection

I-8/T-8 MUST preserve and consume existing authoritative upstream boundaries rather than redefine them:

- the current T-5 QueryRequest design;
- the current T-6 RankedResult design;
- KnowledgeRecord;
- frozen relationship semantics;
- authority/admissibility semantics.

No existing authoritative or frozen contract may be modified merely to accommodate
Context Assembly.

## 10. Architectural Principle

Retrieval nominates.
Authority filters.
Context Assembly composes.
Reason consumes.
Learning proposes validation or supersession.

## 11. Non-Goals

The I-8/T-8 contract does not define:

- an LLM provider;
- a prompt template;
- a model-specific serialization format;
- a frontend;
- an API transport;
- a vector database;
- autonomous reasoning;
- natural-language generation.

## 12. Retrieval-to-Assembly Ownership Boundary

I-6 RetrievalService remains responsible for retrieval nomination only.

I-6 MUST preserve the T-6 RankedResult identity, score, and ordering
semantics.

I-8 Context Assembly owns the downstream structural composition required
after retrieval nomination, including:

- authority/admissibility filtering;
- bounded relationship traversal;
- relationship-subgraph construction;
- provenance assembly;
- contradiction preservation;
- validation-state exposure;
- resource-budget enforcement;
- deterministic ContextPackage compilation.

I-8 MUST NOT reinterpret a T-6 retrieval score as an authority score.

Relationship information used by I-8 MUST come from the authoritative
relationship layer and MUST NOT be inferred from semantic similarity.

The retrieval score nominates relevance.

Authority determines eligibility.

Relationship structure determines explicit structural context.

I-8 MUST preserve these distinctions in T-8 ContextPackage.

## 13. T-8 ContextPackage Structural Contract

`ContextPackage` is the canonical, deterministic output of I-8 Context
Assembly.

It is a packaging representation of existing authoritative AM-PKO
structures. It MUST NOT replace or mutate the underlying KnowledgeRecords,
relationships, evidence, lineage, or validation records.

### 13.1 Required Fields

#### `context_id`

A unique execution identifier for the Context Assembly operation.

It identifies the assembled package and MUST NOT be interpreted as a
KnowledgeRecord identity.

#### `compiled_records`

An ordered collection of eligible KnowledgeRecord references and their
canonical record representations.

Every compiled record MUST have passed the applicable authority/admissibility
boundary.

The collection MUST preserve KnowledgeRecord identity.

#### `provenance_map`

A machine-interpretable mapping from every compiled record and included
structural element to its authoritative provenance.

It MUST preserve, where applicable:

- source identity;
- content/integrity identity;
- lifecycle/authority state;
- validation references;
- lineage references;
- relevant timestamps or temporal validity information.

#### `active_relationship_subgraph`

The bounded set of explicit relationship edges included in the assembled
context.

Every edge MUST use an existing AM-PKO relationship type.

Edges MUST preserve:

- relationship identity where available;
- source record identity;
- target record identity;
- relationship type;
- relevant provenance/validation state.

Relationship edges MUST NOT be inferred from retrieval similarity.

#### `epistemic_validation_summary`

A machine-readable diagnostic structure recording the epistemic disposition
of candidates considered during assembly.

It MUST distinguish at minimum:

- included candidates;
- excluded candidates;
- exclusion reason;
- authority/admissibility outcome;
- validation status;
- contradiction presence where applicable.

Excluded candidates MUST remain observable here even though they are absent
from `compiled_records`.

#### `budget_utilization`

A deterministic execution record containing measured resource utilization
against declared assembly limits.

It MUST expose, where applicable:

- token/context allocation;
- token/context utilization;
- traversal bound;
- traversal utilization;
- latency budget;
- measured assembly latency;
- declared compute/cost budget;
- measured compute/cost utilization when available.

### 13.2 Integrity Invariants

A valid T-8 ContextPackage MUST satisfy:

1. Every `compiled_records` entry resolves to an existing KnowledgeRecord.
2. Every compiled record satisfies the active authority/admissibility policy.
3. Every included relationship resolves to existing endpoint records.
4. Every relationship type belongs to the frozen relationship vocabulary.
5. Every compiled record remains provenance-traceable.
6. No excluded candidate appears in `compiled_records`.
7. No retrieval score is represented as an authority decision.
8. Contradictory eligible records and their explicit contradiction edges are
   preserved rather than silently reconciled.
9. Declared resource bounds are never exceeded silently.
10. The package remains deterministic for identical declared inputs and
    authoritative substrate state.

### 13.3 Separation of Representation and Authority

T-8 represents the authority/admissibility outcomes used during compilation; it does not create or establish authority.

A record's inclusion in `compiled_records` means only that it satisfied the
applicable assembly policy at compilation time.

The underlying KnowledgeRecord and authority ledger remain authoritative.

### 13.4 Separation of Retrieval and Epistemic State

T-6 retrieval relevance and epistemic authority are independent dimensions.

A high retrieval score MUST NOT compensate for:

- INADMISSIBLE state;
- UNDETERMINED state;
- failed validation;
- invalid lineage;
- missing required provenance;
- expired or stale validation.

Likewise, an authoritative record MUST NOT be included solely because it is
authoritative if it does not satisfy the active retrieval/task and assembly
constraints.
