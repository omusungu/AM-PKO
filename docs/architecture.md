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

## Architectural Goal

The long-term goal is not merely document search.

AM-PKO is intended to represent what is known, experienced, conceived, planned, analyzed, connected, retrievable, and applicable within Albert Musungu's personal knowledge ecosystem.
