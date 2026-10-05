# AM-PKO Architecture

## Overview

AM-PKO (Albert Musungu Personal Knowledge Operating System) is an interconnected personal knowledge architecture designed to move knowledge through:

**Capture → Structure → Connect → Embed → Retrieve → Reason → Apply**

The system is designed as a modular architecture rather than a single monolithic application.

## Core Architecture

The major layers are:

1. **Knowledge Records** — structured representations of personal knowledge.
2. **Relationship Layer** — explicit connections between knowledge records.
3. **Embedding Layer** — transforms canonical knowledge representations into vectors.
4. **Embedding Store** — stores and retrieves vector representations.
5. **Retrieval Engine** — combines similarity retrieval with structured relationships.
6. **Reasoning/Application Layer** — uses retrieved knowledge for reasoning and practical application.

## Modular Principle

AM-PKO follows the principle of heterogeneous modularity.

Modules do not need to be identical to participate in the same architecture. They can be materially different while sharing a role, interface, contract, or functional relationship.

Therefore, substitutability is contextual rather than absolute.

A module is substitutable when it can satisfy the relevant contract for the role in which it is being used.

This principle allows AM-PKO to evolve without coupling the architecture to one implementation.

## Variable Modularity

Variable Modularity is the controlled architectural capacity for heterogeneous module realizations to occupy a stable contract or capability role while satisfying applicable contextual constraints and required validation conditions.

The governing pattern is:

**Stable Contract + Variable Realization + Constraints + Validation**

The stable part of a module role includes:
- architectural role and capability
- semantic contract
- required inputs and outputs
- relationship semantics and system invariants
- validation requirements

The variable part may include:
- implementation and technology
- algorithm and internal structure
- composition and granularity
- optimization and runtime characteristics
- specialization

Variation is therefore bounded rather than arbitrary. A realization is admissible only when it satisfies the relevant contract, contextual constraints, and validation requirements:

**Admissible(M,R,C) ∈ { ADMISSIBLE, INADMISSIBLE, UNDETERMINED }**

Execution admissibility is defined as:

**ExecutionAdmissible(M,R,C) ⇔ Admissible(M,R,C) = ADMISSIBLE**

`UNDETERMINED` fails closed and MUST therefore be treated as `INADMISSIBLE`
for module selection, execution, substitution, or promotion.

The three components remain:

- **Contract(M,R):** static compatibility with the frozen role/interface contract.
- **Constraints(M,R,C):** a typed predicate evaluated against structured context `C`.

For Variable Modularity, `C` is a structured architectural context composed only of
declared constraint dimensions relevant to the role under evaluation. It is not a
runtime interface, module-slot abstraction, or new frozen contract type.

The initial canonical context dimensions are:

- **device:** execution-device or hardware capability constraints.
- **runtime:** execution-runtime and environment constraints.
- **offline_requirement:** whether operation must remain available without network access.
- **latency_budget:** the maximum permitted latency for the relevant operation.

Each context dimension MUST have an explicit value or an explicit unknown state.
Unknown context MUST NOT be silently interpreted as satisfying a constraint.

Additional context dimensions may be introduced only when a concrete architectural
decision requires them and their semantics are explicitly defined.

- **Validation(M,R,C):** evidence bound to the exact module `M`, role `R`, and context `C`, including the content hash of `M`.

A change to module content changes its content hash and therefore makes prior
validation evidence stale unless new validation evidence is established.

The admissibility outcomes are determined as follows:

- **ADMISSIBLE:** `Contract(M,R)`, `Constraints(M,R,C)`, and required
  `Validation(M,R,C)` all positively pass.
- **INADMISSIBLE:** at least one required component positively fails.
- **UNDETERMINED:** the available information or evidence is insufficient to
  establish either a complete pass or a definitive failure.

`UNDETERMINED` MUST NOT be interpreted as compatibility, validation,
substitutability, or permission to execute.

Evaluation proceeds in the following order:

**Contract(M,R) → Constraints(M,R,C) → Validation(M,R,C) → Admissible(M,R,C)**

A failed contract or constraint produces `INADMISSIBLE`. Missing,
incomplete, stale, or otherwise insufficient validation evidence produces
`UNDETERMINED` unless a definitive validation failure establishes
`INADMISSIBLE`.

No later evaluation stage may override a definitive failure established by
an earlier required stage.

Variable Modularity is subordinate to heterogeneous modularity. It describes how heterogeneous realizations may occupy a stable role; it does not by itself establish equivalence or substitutability. Substitutability remains conditional on the applicable role, contract, compatibility constraints, context, and validation evidence.

This is an architectural analysis principle, not a new runtime abstraction. It does not require a separate module-slot class, runtime interface, or implementation mechanism.

## Embedding Architecture

Candidate embedding models are treated as replaceable implementations behind a stable embedding interface.

The architectural flow is:

**KnowledgeRecord → Canonical EmbeddingDocument → Embedding Interface → Candidate Model → Vector → Retrieval**

Candidate model families include BGE-M3, multilingual-e5-large, and Qwen3-Embedding.

No candidate model is considered the architecture itself. Model selection remains an evaluation question.

## Relationship Architecture

Relationships provide explicit structure between knowledge records.

Examples include:

- `supports`
- `contradicts`
- `depends_on`
- `derived_from`
- `part_of`
- `related_to`
- `caused_by`
- `mitigates`
- `requires`
- `validates`

Relationships are governed by compatibility rules rather than unrestricted linking.

## Knowledge Flow

AM-PKO separates the representation of knowledge from the mechanisms used to retrieve and apply it.

A simplified flow is:

**Capture → Structure → Connect → Embed → Retrieve → Reason → Apply**

This separation allows individual components to evolve while preserving the architectural contracts between them.

## Current Dashboard

The architecture dashboard provides a visual representation of:

- canonical knowledge records
- relationships
- modules
- embedding experiments
- the AM-PKO knowledge pipeline

The dashboard data is stored separately from the presentation layer so that the architecture can evolve toward more sophisticated visualization and interaction.

## Compatibility Matrix

Compatibility is the decision boundary between heterogeneous realization and conditional substitutability. A realization is not admissible merely because it appears to perform the same function or exposes similarly named operations.

The AM-PKO compatibility decision follows:

**Role → Contract → Compatibility Conditions → Validation Evidence → Decision**

| Architectural role | Stable contract | Compatibility conditions | Required validation evidence | Decision |
|---|---|---|---|---|
| I-2 — EmbeddingDocumentGenerator | KnowledgeRecord → canonical EmbeddingDocument | Canonical document structure, required fields, deterministic generation requirements, source integrity | I-2 frozen/validated contract evidence and regression validation | Admit only when the contract and required validation evidence are satisfied |
| I-3 — EmbeddingModel | EmbeddingModel request/response contract | Input handling, output structure, dimensional consistency, pooling/parser/separator behavior, source integrity, runtime-specific constraints | Interface compliance, compatibility checks, regression validation, retrieval evaluation, and applicable operational evidence | Candidate for substitution only when all applicable conditions are satisfied |
| I-4 — EmbeddingStore | Vector storage and retrieval contract | Vector dimensional/specification compatibility, metadata/filtering semantics, exclusion handling, similarity-score semantics, deterministic ordering, top-k behavior | I-4 frozen/validated contract evidence and implementation validation | Admit only when the store satisfies the I-4 contract and applicable compatibility requirements |
| I-5 — EmbeddingService | Canonical EmbeddingDocument → EmbeddingResponse | I-2/I-3 coordination, identity/version preservation, vector dimension and response structure, error behavior | I-5 frozen/validated contract evidence plus regression validation | Admit only when the service preserves the frozen boundary and required behavior |
| I-6 — RetrievalService | QueryRequest → RankedResult[] | Query embedding capability, I-4 retrieval semantics, score transport, identity preservation, deterministic ordering, T-6 output contract | I-6/T-5/T-6 frozen/validated evidence plus retrieval regression validation | Admit only when orchestration preserves the frozen retrieval contract |

### Decision Rule

Compatibility does not establish equivalence or substitutability by itself.

A proposed realization follows the sequence:

1. **Role** — Does the realization occupy the intended architectural role?
2. **Contract** — Does it satisfy the frozen interface and type contract?
3. **Compatibility conditions** — Does it satisfy the contextual, dimensional, semantic, operational, and boundary constraints relevant to that role?
4. **Validation evidence** — Is there sufficient evidence that the realization preserves required behavior?
5. **Decision** — Only then may it be treated as an admissible candidate for conditional substitution.

Therefore:

**compatible ≠ equivalent**

**compatible ≠ automatically substitutable**

**substitutability = compatible realization + required validation in context**

A missing validation condition is not evidence of compatibility. Where required evidence is absent, the architecture must remain undecided rather than infer substitutability from implementation similarity.

This matrix is an architectural decision aid. It does not create a new runtime interface, module-slot abstraction, relationship type, or production-model selection mechanism.

Relationship-type compatibility remains a separate concern of the Relationship Architecture and must not be conflated with module/interface compatibility.
## Architectural Goal

The long-term goal is not merely document search.

AM-PKO is intended to represent what is known, experienced, conceived, planned, analyzed, connected, retrievable, and applicable within Albert Musungu's personal knowledge ecosystem.
