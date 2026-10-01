# AM-PKO U-1 — Product Usability & Human-Control Architecture Design

Status: DESIGN
Contract version: 0.1-design

## Purpose

Define the human-facing usability and control boundary for AM-PKO without
coupling the core architecture to a specific interface technology.

U-1 exists to ensure that AM-PKO can be operated, inspected, corrected,
and governed by a human without requiring knowledge of its internal
implementation architecture.

## Core Principle

Hide implementation complexity, not epistemic provenance.

Routine users should not need to understand internal boundaries such as
I-4, VectorStoreMatch, or I-6. When knowledge is used to support an answer,
decision, or action, the relevant provenance and uncertainty must remain
inspectable.

## Primary Human Operations

U-1 covers four primary human operations:

1. CAPTURE
   Express knowledge with minimal interaction and review proposed structure.

2. EXPLORE
   Search, inspect, connect, and understand retrieved knowledge.

3. GOVERN
   Correct, approve, reject, link, contradict, supersede, archive, or
   otherwise control knowledge changes.

4. APPLY
   Use validated knowledge in downstream reasoning or action while preserving
   appropriate human approval boundaries.

## Human-Control Requirements

The interface architecture should support:

- human inspection before consequential mutation;
- explicit correction of machine-generated interpretations;
- visible provenance for grounded knowledge;
- preservation of contradictory knowledge;
- explicit approval for consequential external actions;
- reversible or recoverable user changes where applicable;
- deterministic access to underlying knowledge records;
- separation between system suggestions and authoritative knowledge.

## Progressive Disclosure

U-1 should use progressive disclosure:

Level 0:
Simple result or interaction.

Level 1:
Evidence/provenance indicator.

Level 2:
Relevant record and relationship details.

Level 3:
Full lineage, transformations, evidence, and applicable system state.

The interface should not expose architectural complexity by default.

## Capture Boundary

Capture should initially provide a low-friction human input surface.

The system may propose:

- knowledge type;
- granularity;
- domain;
- project;
- topic;
- relationships;
- relevant metadata.

Proposals are not authoritative until accepted or corrected by the human
or by an explicitly authorized workflow.

Transformation provenance must remain recoverable.

## Exploration Boundary

Exploration should allow a human to:

- search knowledge;
- inspect individual records;
- inspect relationships;
- inspect provenance;
- identify contradictory records;
- understand why records were retrieved;
- distinguish stored knowledge from generated interpretation.

## Context Boundary

When T-8 exists, U-1 should expose an inspectable context boundary before
reasoning where practical.

The context view should be capable of showing:

- query;
- selected records;
- retrieval path;
- relationship expansion;
- contradictions;
- provenance;
- applicable context limits;
- relevant budget information.

U-1 does not define T-8 itself.

## Governance Boundary

Human governance actions should be explicit.

Candidate operations:

- ACCEPT
- CORRECT
- REJECT
- LINK
- CONTRADICT
- SUPERSEDE
- PROMOTE
- ARCHIVE

These operations must not be assumed to exist in the current runtime merely
because they are defined here.

## Interface Independence

U-1 is interface-technology neutral.

Potential interfaces include:

- CLI/terminal;
- web application;
- desktop application;
- note-taking integration;
- future agent interface.

No specific interface technology is selected by this design.

The core AM-PKO contracts remain authoritative beneath all interfaces.

## Initial Interface Strategy

The first usability validation target should be a CLI-native workflow because
it matches the current AM-PKO development environment and provides a
reproducible interaction surface.

Candidate commands are illustrative only:

- ampko capture
- ampko search
- ampko inspect
- ampko context
- ampko explain
- ampko validate
- ampko trace

These commands are not runtime requirements until separately designed and
implemented.

## Usability Measurement

U-1 should eventually be evaluated using measurable workflows.

Initial candidate measures:

- capture completion time;
- search-to-useful-context time;
- provenance inspection effort;
- correction effort;
- recovery/undo effort;
- successful human override;
- accidental mutation rate;
- provenance visibility;
- contradiction discovery before reasoning;
- user ability to distinguish evidence from generated interpretation.

Thresholds must be established from empirical testing rather than frozen
prematurely.

## Architectural Boundaries

U-1 must not:

- modify frozen I-2 through I-6 contracts;
- modify frozen T-5 through T-7 contracts;
- implement T-8;
- implement ReasoningTrace;
- select a production embedding model;
- select a vector database;
- silently mutate KnowledgeRecords;
- replace the Contract Graph;
- become dependent on Obsidian, Logseq, a web framework, or a CLI framework.

## Relationship to Current Architecture

Current conceptual flow:

Capture
  ↓
Structure
  ↓
Connect
  ↓
Embed
  ↓
Retrieve
  ↓
T-8 ContextAssembly
  ↓
Reason
  ↓
Apply

U-1 is a cross-cutting human interaction and governance boundary around
this flow rather than another processing stage.

## Evidence Position

This document is a design proposal.

It does not claim that all described interaction capabilities currently
exist in AM-PKO.

Current implementation maturity must be established separately through
workflow validation.

## Design Status

U-1 is DESIGN only.

It is not frozen.
No runtime implementation is implied.
No existing frozen contract is modified.
No production model or infrastructure decision is made.
