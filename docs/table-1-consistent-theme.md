# AM-PKO Table 1 — Consistent Theme

## Substitutability and the Module as a Homologue

Table 1 establishes a central conceptual and architectural theme for AM-PKO:

**Substitutability and the module as a homologue, under heterogeneous modularity.**

The principle is that modules within a system do not have to be identical in order to occupy corresponding roles or satisfy compatible functions.

## Systemic Equivalence

Blair's concept of systemic equivalence provides one way to understand this principle.

Multiple modules may perform approximately the same function within a system even when their internal construction differs.

Therefore, functional correspondence does not necessarily imply material identity.

## Biological Homology

Biological homology provides another useful analogy.

Structures in different organisms can correspond through shared form, developmental origin, or function while remaining materially and operationally different.

A whale's flipper and a human hand, for example, are not identical structures, yet they occupy corresponding biological roles and share evolutionary relationships.

The analogy is useful for AM-PKO because corresponding modules may be heterogeneous while still participating in a common architecture.

## Mathematics as an Extreme Case

Mathematics provides a contrasting extreme.

Repeated modules may be exactly identical because mathematical objects can be defined with exact equality.

Software and knowledge architectures generally do not have this requirement.

Outside such exact systems, modules may differ substantially while remaining compatible at a higher architectural level.

## Heterogeneous Modularity

AM-PKO therefore treats heterogeneity as normal rather than exceptional.

Modules may differ in:

- implementation
- representation
- internal structure
- technology
- scale
- performance
- provenance
- domain

What matters is whether the relevant architectural relationship remains valid.

## Substitutability Is Contextual

Substitutability is not absolute interchangeability.

A module is substitutable only relative to:

- a role
- a function
- an interface
- a contract
- compatibility constraints
- validation requirements
- the context in which it is used

Two modules may therefore be substitutable for one task but not for another.

## Application to AM-PKO

This principle applies across the AM-PKO architecture.

### Knowledge Records

Different knowledge records can have different knowledge types, domains, sources, and granularities while participating in the same KnowledgeRecord structure.

### Relationships

Different relationship types connect records according to different semantic contracts.

A `supports` relationship is not identical to a `depends_on` relationship, even though both participate in the same relationship layer.

### Embedding Models

BGE-M3, multilingual-e5-large, and Qwen3-Embedding are heterogeneous implementations.

They can be treated as candidate substitutes only because AM-PKO places them behind a stable embedding interface.

The architecture does not depend on any one model.

### Storage and Retrieval

Different storage and retrieval implementations can occupy corresponding architectural roles when they satisfy the required interfaces and validation conditions.

## Architectural Consequence

AM-PKO should therefore preserve a distinction between:

**identity → correspondence → compatibility → substitutability**

These are not the same concept.

Two modules may:

1. be identical,
2. be approximately equivalent,
3. occupy homologous roles,
4. be compatible without being equivalent,
5. or be specialized complementary modules that are not substitutes.

The architecture must represent these distinctions rather than collapsing them into a single notion of similarity.

## Core Principle

> **AM-PKO is coherent not because all modules are identical, but because heterogeneous modules can participate in a common architecture through shared roles, interfaces, contracts, relationships, compatibility constraints, and validation.**

This principle connects the conceptual architecture of Table 1 to the practical design of AM-PKO's knowledge records, relationship layer, embedding architecture, retrieval system, and application layer.
