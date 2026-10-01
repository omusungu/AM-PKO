# AM-PKO Contract Graph v0.1 — Supporting Node Representation Design

Status: DESIGN
Contract Graph version: 0.1

## Purpose

Define how supporting boundaries may be represented in Contract Graph v0.1
without treating them as additional frozen contracts.

Supporting nodes exist only where repository evidence requires an explicit
boundary to explain contract provenance, dependency, implementation, or
evolution.

## Node Classes

### FROZEN_CONTRACT

Represents one of the eight frozen AM-PKO contracts:

- I-2
- I-3
- I-4
- I-5
- I-6
- T-5
- T-6
- T-7

These remain the authoritative contract nodes.

### SUPPORTING_BOUNDARY

Represents a directly evidenced architectural boundary that is necessary
to explain relationships among frozen contracts but is not itself being
declared a separately frozen contract by Contract Graph v0.1.

Initial candidates:

- T-3 VectorRecord
- T-4 VectorRecord payload
- VectorStoreMatch
- QueryEmbedder

## Supporting Node Fields

Each SUPPORTING_BOUNDARY node should contain:

- node_id
- node_class
- name
- status
- evidence_class
- source_artifacts
- purpose

### node_id

Stable identifier for the supporting boundary.

### node_class

Must equal:

SUPPORTING_BOUNDARY

### name

Canonical boundary name.

### status

Supporting boundaries are not assigned FROZEN_VALIDATED merely because
they are used by frozen contracts.

Permitted status:

DOCUMENTED_SUPPORTING_BOUNDARY

### evidence_class

One of:

- DIRECTLY_EVIDENCED
- EVIDENCE_DERIVED
- RECONSTRUCTED

### source_artifacts

Repository artifacts that directly support the boundary representation.

### purpose

Short description of why the boundary is represented in the graph.

## Authority Rule

Supporting nodes are derived representations of repository evidence.

They do not create new contract authority.

The underlying implementation, interface, design, validation, and freeze
artifacts remain authoritative.

## Scope Protection

Adding a supporting node must not:

- create a new frozen contract;
- alter an existing frozen contract;
- alter a freeze manifest;
- change contract versions;
- imply production selection;
- infer undocumented dependencies.

## Initial Supporting Boundaries

### T-3

Name:

VectorRecord

Purpose:

Canonical vector record consumed and stored by I-4.

Evidence:

- src/embedding/store/interface.py
- src/embedding/store/payload.py
- src/embedding/store/I-4_FREEZE_MANIFEST.md

### T-4

Name:

VectorRecord payload

Purpose:

Canonical metadata payload associated with T-3 and protected from
retrieval-specific score contamination.

Evidence:

- src/embedding/store/payload.py
- src/embedding/store/I-4_FREEZE_MANIFEST.md
- src/embedding/I-4_T-6_SCORE_TRANSPORT_DECISION_001.md

### VectorStoreMatch

Name:

VectorStoreMatch

Purpose:

Transient I-4 retrieval boundary carrying a VectorRecord together with
the retrieval score before I-6 maps the result to T-6.

Evidence:

- src/embedding/store/match.py
- src/embedding/store/interface.py
- src/embedding/I-4_T-6_SCORE_TRANSPORT_DECISION_001.md
- src/embedding/VECTOR_STORE_MATCH_CONTRACT_001.md
- src/embedding/I-6_FREEZE_MANIFEST.md

### QueryEmbedder

Name:

QueryEmbedder

Purpose:

I-6 query-embedding capability boundary that allows retrieval orchestration
to obtain a query vector without modifying the frozen I-3 model interface.

Evidence:

- src/embedding/query_embedder_interface.py
- src/embedding/query_embedder.py
- src/embedding/I-6_QUERY_EMBEDDER_DESIGN_001.md
- src/embedding/I-6_FREEZE_MANIFEST.md

## Design Constraint

Supporting nodes must remain distinguishable from frozen contract nodes.

The Contract Graph must therefore never count SUPPORTING_BOUNDARY nodes as
members of the frozen I-2–T-7 contract family.

## Design Status

This document defines the proposed representation only.

No supporting nodes have yet been added to CONTRACT_GRAPH_V0_1.json.

No frozen contract has been modified.
