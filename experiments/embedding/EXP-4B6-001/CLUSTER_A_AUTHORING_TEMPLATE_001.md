# AM-PKO EXP-4B6-001 — Cluster A Authoring Template

**Cluster:** A
**Domain:** Welding/Fabrication
**Records:** K-000101–K-000110
**Status:** DESIGN
**Template version:** 0.1-design

## Purpose

Define the substantive authoring structure for Cluster A before records are
written into corpus.json.

## Records

### K-000101
- Knowledge Type: FACT
- Granularity: Claim
- Topic: Heat Distortion
- Special Role: semantic_overlap

### K-000102
- Knowledge Type: EXPERIENCE
- Granularity: Observation
- Topic: Structural Fit-up
- Special Role: ambiguity

### K-000103
- Knowledge Type: IDEA
- Granularity: Heuristic
- Topic: Weld Porosity
- Special Role: relationship_chain

### K-000104
- Knowledge Type: PLAN
- Granularity: Procedure
- Topic: Root Passes
- Special Roles: semantic_overlap, cross_domain

### K-000105
- Knowledge Type: ANALYSIS
- Granularity: Hypothesis
- Topic: Tack Sequence
- Special Role: contradiction

### K-000106
- Knowledge Type: FACT
- Granularity: Finding
- Topic: Interpass Temperature
- Special Role: historical_superseding

### K-000107
- Knowledge Type: EXPERIENCE
- Granularity: Principle
- Topic: Material Preparation
- Special Roles: relationship_chain, semantic_overlap

### K-000108
- Knowledge Type: IDEA
- Granularity: Pattern
- Topic: Jigs and Fixtures
- Special Roles: ambiguity, cross_domain

### K-000109
- Knowledge Type: PLAN
- Granularity: PlanItem
- Topic: Site Troubleshooting
- Special Role: relationship_chain

### K-000110
- Knowledge Type: ANALYSIS
- Granularity: Recommendation
- Topic: Fabrication Planning
- Special Role: semantic_overlap

## Required Authoring Fields

Each record must define:

1. title
2. content
3. source.type
4. source.reference
5. skills
6. assets
7. actions
8. relationships
9. metadata.version
10. metadata.created_at
11. metadata.cluster

## Authoring Constraints

- Preserve the allocated knowledge type.
- Preserve the allocated granularity.
- Preserve the allocated topic.
- Implement the assigned special role.
- Use genuine welding/fabrication knowledge.
- Preserve provenance honestly.
- Do not fabricate external citations.
- Do not optimize wording for any embedding model.
- Do not create queries yet.
- Do not generate embeddings yet.
- Do not modify the allocation matrix.
- Do not modify frozen AM-PKO contracts.

## Review Gate

Before insertion into corpus.json, verify every record for:

- semantic correctness
- knowledge-type correctness
- granularity correctness
- provenance correctness
- relationship correctness
- special-role correctness
- human interpretability
- model neutrality
