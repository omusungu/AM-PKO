
AM-PKO

Albert Musungu Personal Knowledge Operating System

AM-PKO is an ontology-driven, modular Personal Knowledge Operating System for capturing, structuring, connecting, retrieving, evaluating, reasoning over, and applying knowledge.

It is not merely a document search system or a Retrieval-Augmented Generation (RAG) pipeline. Retrieval is one capability within a broader architecture that connects structured knowledge, relationships, evidence, provenance, modular services, validation, and practical action.

1. Purpose

AM-PKO aims to make personal knowledge:

- Structured: represented through explicit knowledge types and metadata.
- Connected: linked through typed relationships with defined semantics.
- Traceable: supported by sources, evidence, and provenance where available.
- Retrievable: accessible through structured queries and semantic retrieval.
- Evaluable: assessed through explicit contracts, tests, and reproducible experiments.
- Actionable: connected to reasoning, plans, skills, assets, dependencies, and next steps.
- Modular: organized into components whose admissibility depends on explicit contracts, constraints, and validation.

The system should distinguish what is known, what has been done, what remains uncertain, which assets exist, what depends on what, and which actions are justified by the available evidence.

2. Architectural Model

The conceptual organization is:

Albert → Domain → Project → Knowledge Type → Relationship

A more granular knowledge organization is:

Project → Topic → Claim or Experience → Source or Evidence → Skills, Assets, Actions, Relationships, and Metadata

Domains provide organizational context; they are not knowledge types.

The architecture brings together:

1. Knowledge representation and ontology.
2. Typed relationships between knowledge records.
3. Evidence and provenance.
4. Embedding generation and vector storage interfaces.
5. Retrieval and evaluation.
6. Contract-governed modular services.
7. Reasoning, learning, and application.

The architecture is evolving. Conceptual models, draft contracts, validated artifacts, and production decisions must remain distinguishable.

3. Knowledge Ontology

The five core knowledge types are:

| Type | Purpose |
|---|---|
| FACT | Represents a factual assertion. |
| EXPERIENCE | Records an observed or lived experience. |
| IDEA | Captures a proposed concept or possibility. |
| PLAN | Describes intended work or a course of action. |
| ANALYSIS | Records structured interpretation or evaluation |

These categories describe the kind of knowledge being represented, not its subject domain.

The current ontology namespace is:

"https://am-pko.local/ontology#"

The "KnowledgeRecord" identifier convention is:

"K-[0-9]{6}"

Core relationship vocabulary includes:

- "supports"
- "contradicts"
- "depends_on"
- "derived_from"
- "part_of"
- "related_to"
- "caused_by"
- "mitigates"
- "requires"
- "validates"

A vocabulary entry does not, by itself, establish every constraint or governance rule required for its use. Relationship semantics, endpoint compatibility, lifecycle authority, and validation requirements remain separate design concerns.

4. Knowledge Processing Pipeline

The evolving conceptual pipeline is:

Capture → Structure → Connect → Embed → Retrieve → Reason → Learn → Apply

- Capture: collect knowledge and associated source material.
- Structure: classify and normalize knowledge records.
- Connect: represent relationships among records.
- Embed: transform supported content into vector representations.
- Retrieve: locate relevant records through available retrieval mechanisms.
- Reason: evaluate evidence, relationships, dependencies, and uncertainty.
- Learn: incorporate validated findings and evaluation results into future system development.
- Apply: produce justified actions, plans, and operational outputs.

These stages describe architectural capabilities and direction. They do not imply that every stage is fully implemented or production-ready.

5. Embedding and Retrieval Architecture

The documented embedding path is:

"KnowledgeRecord → I-2 EmbeddingDocument → I-3 EmbeddingModel → Vector → I-4 EmbeddingStore → I-6 RetrievalService"

The project has documented and validated components and contracts across this path, including embedding adapters and evaluation artifacts.

The recorded embedding adapter work includes "llama.cpp" with:

- BGE-M3
- Multilingual E5-large
- Qwen3-Embedding-0.6B

The associated work includes fail-closed handling for invalid embeddings and token-related failures, as well as model-specific pooling behavior.

A production vector database remains NOT_SELECTED in the recorded project state. Successful component validation or experiment completion must not be interpreted as production model or infrastructure approval.

6. Modular Architecture and Admissibility

AM-PKO treats modularity as a question of substitutability under explicit contracts and constraints, rather than assuming every component is interchangeable.

The current analytical admissibility predicate is:

"Admissible(M,R,C) = Contract(M,R) ∧ Constraints(M,R,C) ∧ Validation(M,R,C)"

Where:

- "M" is a module.
- "R" is the required role or interface.
- "C" is the applicable context.
- "Contract(M,R)" evaluates contract compatibility.
- "Constraints(M,R,C)" evaluates applicable contextual constraints.
- "Validation(M,R,C)" evaluates validation evidence for the specific module, role, and context.

Validation must apply to the relevant triple and content hash. A result for one module, interface, context, or artifact version must not automatically authorize a different one.

For execution or module selection, "UNDETERMINED" is treated as "INADMISSIBLE". Missing evidence is not proof of compatibility.

These rules describe the current architectural direction and review constraints. Their inclusion here does not independently approve a contract, freeze an architecture, or authorize implementation.

7. Relationship-Layer Design Status

The relationship layer is undergoing coordinated design review.

The recorded open-question inventory covers:

1. Q1 — Standalone runtime "RelationshipRecord".
2. Q2 — Independent relationship identifier.
3. Q3 — Relationship-level provenance.
4. Q4 — Relationship-level validation.
5. Q5 — Duplicate relationship assertions.
6. Q6 — Self-link policy.
7. Q7 — Inverse relationship policy.
8. Q8 — Relationship governance and lifecycle authority.
9. Q9 — Relationship endpoint compatibility constraints.

Status: design review; decisions and authorization boundaries remain controlling.

Some questions have draft proposals, supporting tests, or validation artifacts. Such evidence does not automatically constitute an approved architectural decision.

In particular:

- A Q1 or Q2 proposal must not be presented as an authoritative decision unless the governing contract records that decision.
- Q9 predicate-specific constraint analysis remains analytical work unless separately approved through the applicable decision process.
- A successful validation report does not itself authorize a schema change, runtime implementation, or relationship-layer freeze.
- Draft lineage and allocation rules remain distinct from the canonical relationship vocabulary.
- Existing knowledge and relationship data must not be silently reshaped to fit an unapproved proposal.

Consult the relevant architecture documents and their explicit status declarations before treating any proposal as normative.

8. Validation and Experimental Evidence

AM-PKO uses explicit tests and validation artifacts to examine structural consistency, interface behavior, embedding behavior, retrieval quality, and design constraints.

Recorded work includes:

- Knowledge-record and relationship-substrate validation.
- Embedding and retrieval component validation.
- Evaluation experiments with frozen records, queries, and judgments.
- Contract and dashboard consistency checks.
- Relationship-layer design-review evidence.

A validation result applies only to its documented scope, inputs, assumptions, and artifact version. It must not be generalized into a broader approval without evidence and authorization.

Experiment completion, test success, draft validation, architecture approval, and production readiness are different states and must remain distinct.

9. Repository Areas

The repository contains or is intended to organize work across areas such as:

| Area | Purpose |
|---|---|
| "architecture/" | Architecture contracts, design decisions, and review artifacts. |
| "scripts/" | Validation and supporting automation. |
| "dashboard/" | Architecture and knowledge-substrate visualization. |
| Experiment artifacts | Reproducible evaluation inputs, results, and model-related evidence. |

The presence of a file or directory does not establish that its contents are approved, complete, or production-ready. Consult the repository and the relevant artifact status before relying on an implementation claim.

10. Operating and Governance Principles

Development should preserve these principles:

1. Explicit authority: distinguish proposals, decisions, validation, and implementation authorization.
2. Fail-closed behavior: do not treat missing or indeterminate evidence as permission to execute.
3. Traceability: preserve source, provenance, version, and validation context where applicable.
4. Contract-first modularity: evaluate components against explicit roles and constraints.
5. Evidence-scoped conclusions: make claims no broader than the evidence supports.
6. Controlled evolution: preserve compatibility and lineage when changing structures or responsibilities.
7. Reproducibility: retain test inputs, validation results, and relevant artifact versions.
8. Minimal change: avoid unrelated modifications while conducting focused reviews or documentation work.

11. Current Status and Next Steps

AM-PKO is an evolving architecture and implementation project. The recorded work includes structured knowledge records, relationship data, embedding and retrieval components, evaluation experiments, and modular architecture contracts.

The following remain important boundaries:

- The production vector database has not been selected in the recorded state.
- The relationship-layer Q1–Q9 inventory must be resolved through the governing decision process.
- Draft architecture documents are not automatically normative.
- Validation success does not grant implementation or schema-promotion authority.
- Production readiness must be established through explicit, scoped evidence.

Recommended next steps are to:

1. Inspect the current repository and identify authoritative contracts and decisions.
2. Reconcile design-review documents with their governing artifacts without silently promoting drafts.
3. Continue predicate-specific endpoint compatibility analysis for Q9.
4. Resolve outstanding relationship questions through explicit decisions and appropriate validation.
5. Preserve reproducible tests and evidence for each approved change.
6. Select production infrastructure only through a documented evaluation and decision process.

12. Documentation Authority

This README is an orientation document. It summarizes the project and its recorded architectural direction; it does not replace authoritative contracts, decision records, validation artifacts, or implementation specifications.

If this README conflicts with an authoritative project artifact, the applicable governing artifact and its explicit decision status control. Unresolved conflicts must be surfaced rather than silently resolved by documentation.

No architecture freeze, relationship-layer approval, schema promotion, or runtime implementation authorization is conferred by this document.

---

Project: Albert Musungu Personal Knowledge Operating System (AM-PKO)
Document: Root README
Purpose: Project orientation and architecture status
Status: Documentation draft; not an architecture approval
