# AM-PKO Contract Graph v0.1 — Schema Design

Status: DESIGN
Contract Graph version: 0.1

## Purpose

Contract Graph v0.1 is a machine-readable provenance and dependency graph for AM-PKO frozen contracts.

The graph records:

- authoritative contract identity;
- frozen version and lifecycle state;
- evidence classification;
- authoritative and supporting artifacts;
- implementation artifacts;
- explicit contract dependencies;
- contract evolution;
- validation and compatibility relationships;
- downstream invalidation consequences of contract revision.

The Contract Graph is derived from repository evidence. It does not replace or supersede the underlying contract artifacts.

## Evidence Classes

The graph uses exactly three evidence classes:

- DIRECTLY_EVIDENCED
- EVIDENCE_DERIVED
- RECONSTRUCTED

## Contract Node

Each contract node contains:

- contract_id
- contract_type
- name
- version
- status
- evidence_class
- freeze_artifact
- implementation_artifacts
- evidence_artifacts
- downstream_invalidation

## Relationship

Each relationship contains:

- relationship_id
- source
- relationship_type
- target
- evidence_artifacts

## Relationship Types

The initial vocabulary is:

- DEPENDS_ON
- CONSUMES
- PRODUCES
- IMPLEMENTS
- VALIDATES
- PROTECTS
- EVOLVED_FROM
- COMPATIBLE_WITH
- INVALIDATES

Vague relationship types are intentionally excluded from v0.1.

## Authority Rule

The underlying repository artifacts remain authoritative.

The Contract Graph is a derived machine-readable representation of those artifacts.

A graph entry must not be treated as evidence unless its supporting repository artifact is identified.

## Revision Rule

Revision of a frozen contract must be evaluated against its downstream_invalidation entries.

The graph does not automatically modify, invalidate, or unfreeze contracts.

Any contract revision requires explicit lifecycle handling in the affected contract artifacts.

## Scope

Initial v0.1 scope covers the frozen AM-PKO embedding/retrieval contracts:

- I-2
- I-3
- I-4
- I-5
- I-6
- T-5
- T-6
- T-7

Supporting boundaries and artifacts may be represented where required to explain evidence or dependency relationships.

## Non-Goals

Contract Graph v0.1 does not:

- modify frozen contracts;
- select a production embedding model;
- select a vector database;
- implement T-8;
- perform runtime retrieval;
- replace contract freeze manifests;
- infer undocumented dependencies;
- silently resolve contradictory historical evidence.

## Design Status

This document defines the proposed Contract Graph v0.1 schema.

The graph itself is not yet generated or frozen.
