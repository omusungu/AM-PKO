# AM-PKO Authority & Lineage Contract
**Status:** DRAFT
**Version:** 0.1

## 1. Scope

This contract defines the architectural boundary for epistemic authority,
validation-dependent authority state, and historical lineage over authoritative
KnowledgeRecord identities.

It establishes how authority may be computed from knowledge type, lifecycle
state, lineage, validation evidence, integrity, and applicable policy.

It does not redefine the canonical KnowledgeRecord representation, existing
KnowledgeRecord fields, frozen embedding interfaces, retrieval semantics,
Context Assembly semantics, or the existing semantic relationship vocabulary.

## 2. Non-Goals

This contract does not:

- replace the existing KnowledgeRecord representation;
- repurpose KnowledgeRecord `status` as epistemic authority;
- redefine semantic relationships such as `supports`, `contradicts`,
  `derived_from`, or `related_to` as lifecycle lineage;
- create a new Homologue abstraction;
- make retrieval scores authoritative;
- permit Context Assembly to create authority;
- permit Learning to directly mutate authoritative knowledge;
- erase, overwrite, or silently reconcile historical or contradictory records;
- establish a production database, storage technology, or UI;
- authorize a promotion, supersession, or retraction merely by defining the
  corresponding operation.


## 3. Epistemic Authority State

Epistemic authority is represented by a distinct authority lifecycle and is
not equivalent to KnowledgeRecord `status`.

The authority lifecycle is:

DRAFT → STRUCTURED → CONNECTED → VERIFIED

A VERIFIED record may subsequently transition to:

VERIFIED → SUPERSEDED
VERIFIED → RETRACTED

The authority state is a derived epistemic state governed by this contract.
It is not inferred solely from the KnowledgeRecord authoring/corpus status.

### 3.1 State Semantics

- DRAFT: the epistemic record is being formed and is not authoritative.
- STRUCTURED: required structure and knowledge-type classification have been
  established, but authority has not been established.
- CONNECTED: required relationships and lineage references have been
  established and validated sufficiently for the applicable policy, but the
  record is not yet authoritative.
- VERIFIED: the record satisfies the applicable type-specific authority,
  evidence, lineage, integrity, and validation requirements.
- SUPERSEDED: the record was previously authoritative but has been replaced
  by an authorized successor; its historical identity and authority history
  remain preserved.
- RETRACTED: the record was previously authoritative but has been explicitly
  withdrawn by an authorized action with a recorded reason and supporting
  evidence where required.

### 3.2 Terminal and Prohibited Transitions

SUPERSEDED must not silently return to VERIFIED.

RETRACTED must not silently return to VERIFIED.

A previously authoritative record must not be rewritten in place to conceal
the historical transition.

Any later change requiring renewed epistemic evaluation must produce the
appropriate new or derived record and preserve lineage to the prior record.


## 4. Type-Specific Authority Requirements

Authority verification MUST depend on the KnowledgeRecord knowledge type.
No knowledge type may become VERIFIED solely because its structure or
relationships are valid.

### 4.1 FACT

A FACT requires identifiable supporting evidence appropriate to the claim,
together with successful validation of that evidence and the record's
integrity and lineage.

### 4.2 EXPERIENCE

An EXPERIENCE requires evidence establishing that the described experience
occurred. Appropriate evidence may include attestation or other provenance
appropriate to the experience.

Citation is not inherently required when citation would not establish the
occurrence of the experience.

### 4.3 IDEA

An IDEA is not directly eligible for VERIFIED authority.

An IDEA may remain an idea, or it may be transformed through an explicit
derived process into an ANALYSIS or PLAN record subject to that type's
authority requirements.

The transformation MUST preserve lineage to the originating IDEA.

### 4.4 PLAN

A PLAN requires validation appropriate to its intended execution, including
applicable feasibility, constraints, dependencies, resources, and other
requirements defined by the active policy.

A PLAN being well-structured does not establish that it is feasible or
authoritative.

### 4.5 ANALYSIS

An ANALYSIS requires identifiable inputs, reasoning provenance, and validation
appropriate to the claims or conclusions it presents.

The analysis MUST preserve traceability to the knowledge and evidence on
which it depends.

### 4.6 Type Invariant

Knowledge type determines the applicable verification policy; it does not
determine authority by itself.

Therefore:

KnowledgeType(n) ≠ AuthorityState(n)

and:

AuthorityState(n) = VERIFIED

is permitted only when all requirements applicable to the record's knowledge
type have passed.


## 5. Epistemic Lineage

Epistemic lineage records historical identity and authority-relevant
derivation between KnowledgeRecord identities.

Lineage is distinct from the semantic relationship layer.

The following lifecycle lineage relations are recognized by this contract:

- supersedes
- split_from
- merged_into

Lineage relations MUST reference stable KnowledgeRecord identities.

### 5.1 Semantic Relationship Separation

A semantic relationship such as `supports`, `depends_on`, `derived_from`,
`part_of`, `related_to`, `caused_by`, `mitigates`, `requires`, or `validates`
MUST NOT be reinterpreted as a lifecycle transition merely because the
relationship connects records.

In particular, `derived_from` identifies derivation and does not by itself
establish `SUPERSEDED` authority state.

Where historical replacement is intended, an explicit `supersedes` lineage
relation is required.

### 5.2 Bidirectional Historical Identity

Where a record supersedes another record, the historical relationship MUST
be explicitly traceable in both directions:

successor → supersedes → predecessor

and, where represented by the authoritative lineage substrate:

predecessor → succeeded_by → successor

The two directions MUST identify the same record pair and MUST NOT contradict
one another.

### 5.3 Preservation

Lineage is append-only.

Creating a successor, split, merge, contradiction, or retraction MUST NOT
erase the identity or historical state of an existing record.

A historical record remains addressable even when it is SUPERSEDED or
RETRACTED.

### 5.4 Branching and Convergence

Lineage MUST permit one-to-many and many-to-one historical evolution.

One record may produce multiple successors through explicit `split_from`
lineage.

Multiple records may converge into a new record through explicit
`merged_into` lineage.

Such structures form a directed lineage graph and MUST preserve every
participating record identity.


## 6. Authority Computation

Authority MUST be computed from the record's applicable epistemic state,
knowledge type, lineage, validation events, evidence, integrity state, and
active authority policy.

Authority MUST NOT be established by a manually asserted authority flag alone.

Conceptually:

Authority(n) =
f(
  Type(n),
  State(n),
  Lineage(n),
  ValidationEvents(n),
  Evidence(n),
  Integrity(n),
  Policy
)

A record is authoritative only when all requirements imposed by the active
authority policy have been satisfied.

These requirements include, where applicable:

- permitted authority state;
- valid knowledge-type classification;
- required evidence;
- successful type-specific validation;
- valid lineage;
- valid content/version integrity;
- valid required ancestor authority;
- absence of a blocking retraction or supersession condition;
- satisfaction of applicable policy constraints.

### 6.1 Fail-Closed Authority

Insufficient, missing, stale, invalid, or internally inconsistent evidence MUST
NOT establish authority.

If the available information is insufficient to establish that all required
authority conditions pass, the authority outcome MUST remain
UNDETERMINED rather than being inferred as VERIFIED.

A broken lineage, invalid integrity state, missing required provenance, or
failed required validation MUST prevent authoritative use according to the
applicable failure policy.

### 6.2 Authority Is Not a Record Field Shortcut

Downstream components MUST consume the computed authority/admissibility
outcome rather than assuming that a KnowledgeRecord's authoring `status`,
retrieval score, embedding similarity, or presence in a corpus establishes
authority.

This preserves the boundary:

Retrieval nominates.
Authority filters.
Context Assembly composes.
Reason consumes.



### 6.3 Authority Outcome Determination

Authority lifecycle state MUST be evaluated separately from the three-valued
admissibility outcome.

For an evaluated record and context, the outcome MUST be determined from the
applicable authority requirements as follows:

- ADMISSIBLE: every required condition is satisfied and no blocking condition
  is present;
- INADMISSIBLE: at least one required condition has definitively failed;
- UNDETERMINED: no required condition has definitively failed, but one or more
  required conditions cannot be established from the available information.

A lifecycle state MUST NOT by itself determine the outcome.

In particular:

- VERIFIED does not guarantee ADMISSIBLE for every context;
- SUPERSEDED and RETRACTED records remain historically addressable but are not
  admissible for current authoritative use unless an applicable policy
  explicitly establishes otherwise;
- DRAFT, STRUCTURED, and CONNECTED states do not establish authoritative use;
- missing, stale, or insufficient evidence produces UNDETERMINED unless the
  applicable requirement is itself definitively failed;
- a definitive failed requirement produces INADMISSIBLE even when other
  requirements pass.

The determination MUST evaluate all applicable requirements without allowing a
later successful condition to override an earlier definitive failure.

Therefore:

AuthorityState(n) != Admissibility(n,R,C)

and:

ExecutionAdmissible(M,R,C) ⇔ Admissible(M,R,C) = ADMISSIBLE


## 7. Validation Binding and Content Integrity

Validation evidence used for authority MUST identify the exact KnowledgeRecord
version to which the evidence applies.

Where content integrity is required by the active policy, validation MUST also
be bound to a canonical content identity for the validated KnowledgeRecord.

A validation result MUST NOT be considered current merely because its
validation identifier exists.

At minimum, validation binding MUST establish:

- KnowledgeRecord identity;
- KnowledgeRecord version;
- validation identity;
- validation scope;
- validation outcome;
- validation time or applicable validity interval;
- evidence or provenance references;
- content integrity identity where required by policy.

### 7.1 Stale Validation

If a KnowledgeRecord changes in a way that changes its validated identity,
previous validation MUST NOT automatically authorize the changed record.

A validation bound to an earlier version or content identity is stale for the
changed record unless the active policy explicitly establishes that the
validation remains applicable.

### 7.2 Integrity Failure

If the integrity identity required by the active policy cannot be established,
does not match the validated record, or cannot be verified, the authority
decision MUST NOT become VERIFIED on the basis of that validation.

The resulting authority outcome MUST be determined according to the
fail-closed rules of this contract.

### 7.3 Evidence Scope

Validation evidence MUST NOT be silently generalized from one KnowledgeRecord
to another record merely because the records are related, semantically
similar, derived from one another, or occupy the same module or role.

Evidence applies only within its declared validation scope.


## 8. Append-Only Authority Event Ledger

Authority-relevant changes MUST be represented as append-only events.

The event history is authoritative evidence of how a KnowledgeRecord reached,
left, or changed authority state.

Recognized authority-relevant event categories include:

- CREATED
- REVISED
- LINKED
- VALIDATED
- SUPERSEDED
- SPLIT
- MERGED
- RETRACTED

An event MUST NOT silently overwrite or delete a prior event.

### 8.1 Event Identity and Binding

Each authority-relevant event MUST be traceable to:

- the affected KnowledgeRecord identity;
- the event type;
- the event actor or authorized source where required by policy;
- the event time;
- the relevant prior state where applicable;
- the resulting state or proposed state where applicable;
- supporting evidence or provenance where required;
- the applicable validation or integrity identity where required.

### 8.2 State Derivation

Authority state MUST be reconstructable from the applicable event history and
validated evidence.

A mutable authority-state value MUST NOT become the sole source of truth when
the underlying event history is unavailable or inconsistent.

If event history required to establish authority is incomplete, corrupted, or
internally inconsistent, the authority outcome MUST fail closed.

### 8.3 Historical Preservation

A new event MUST preserve the existence and historical meaning of earlier
events.

SUPERSEDED and RETRACTED records remain historically addressable.

Contradictory records remain independently addressable and MUST NOT be
silently merged or rewritten as a consequence of recording a contradiction
event or relationship.


### 8.4 Event-to-State Transition Invariant

Authority-relevant events MUST produce only lifecycle transitions permitted by
Section 3 and the applicable authorization policy.

The following transition classes are recognized:

- CREATED MAY establish or record DRAFT;
- REVISED MUST NOT by itself establish VERIFIED and MUST trigger renewed
  evaluation where the revision affects authority-relevant content;
- LINKED MAY support progression toward CONNECTED but MUST NOT by itself
  establish VERIFIED;
- VALIDATED MAY provide evidence required for an authority transition but MUST
  NOT by itself establish authorization;
- SUPERSEDED MAY transition a previously authoritative record to SUPERSEDED
  only through the authorized supersession process;
- SPLIT MUST preserve the source record and establish the resulting lineage;
- MERGED MUST preserve every source record and establish the resulting
  lineage;
- RETRACTED MAY transition a previously authoritative record to RETRACTED
  only through the authorized retraction process.

No event category may silently bypass the authority requirements, authorization
requirements, lineage requirements, or integrity requirements defined elsewhere
in this contract.

A state transition MUST be reconstructable from the recorded event sequence
and the evidence applicable to that transition.

If the event sequence permits multiple incompatible authority states, the
authority state MUST be treated as unresolved and the applicable admissibility
outcome MUST fail closed.


### 8.5 Authorized Lifecycle Progression

Progression through the authority lifecycle MUST occur through explicit,
reconstructable transitions.

The permitted forward progression is:

DRAFT → STRUCTURED → CONNECTED → VERIFIED

A transition from:

- DRAFT to STRUCTURED MUST establish that required structure and
  knowledge-type classification are valid;
- STRUCTURED to CONNECTED MUST establish that required relationships and
  lineage references satisfy the applicable policy;
- CONNECTED to VERIFIED MUST establish all applicable type-specific
  verification, evidence, validation, integrity, lineage, and authorization
  requirements.

No intermediate lifecycle state may be skipped merely because a later
condition appears satisfied.

A transition to VERIFIED MUST satisfy Section 9 promotion requirements.

SUPERSEDED and RETRACTED remain historical terminal states unless an explicit
future contract defines a distinct reinstatement transition. Such a transition
MUST NOT be inferred from ordinary revision, validation, or linking events.

### 8.6 Transition Recording Rule

Lifecycle transitions MUST be represented by the resulting or proposed authority
state recorded on an authority-relevant event; a separate event category is not
required for each lifecycle state.

Accordingly:
- CREATED or REVISED MAY record DRAFT or STRUCTURED where the applicable
  structural requirements are satisfied;
- LINKED or another applicable authority-relevant event MAY record CONNECTED
  where the required relationship and lineage conditions are satisfied;
- VALIDATED MAY record or propose VERIFIED only when all Section 9 promotion
  requirements are satisfied, including required authorization;
- SUPERSEDED and RETRACTED events MUST record their corresponding historical
  terminal state only through their authorized processes.

The event category alone MUST NOT imply the resulting authority state.

Every recorded transition MUST identify the prior state, resulting or proposed
state, applicable evidence, and authorization where required.

## 9. Promotion Authority

Epistemic promotion is an authorized operation, not an automatic consequence
of successful technical validation.

The system MAY determine that a record is eligible for promotion by evaluating
the applicable type, state, evidence, lineage, integrity, and policy
requirements.

Where the active policy requires human or explicitly authorized actor
confirmation, the system MUST NOT promote the record without that
authorization.

### 9.1 Eligibility Versus Promotion

The following are distinct:

- eligibility: the record satisfies the conditions required for a proposed
  authority transition;
- authorization: an actor or policy grants permission for the transition;
- transition: the authoritative event records the resulting state change.

Successful validation establishes evidence for eligibility. It does not, by
itself, establish authorization to promote.

### 9.2 Promotion Invariant

A record MUST NOT enter VERIFIED unless:

1. all applicable verification requirements have passed;
2. required lineage and integrity conditions have passed;
3. required validation evidence is current and correctly bound; and
4. required authorization has been obtained.

If any required condition is missing or unresolved, the record MUST NOT be
promoted to VERIFIED.

### 9.3 Learning Boundary

Learning MUST NOT directly mutate authoritative KnowledgeRecords or directly
promote them.

Learning MAY produce a validation event, validation proposal, or supersession
proposal according to the applicable policy.

Any resulting authority transition MUST pass through the same validation and
authorization boundary as other authority transitions.


## 10. Contradiction and Competing Knowledge

A contradiction is an explicit relationship between independently identifiable
KnowledgeRecords.

Recording a contradiction MUST NOT by itself:

- delete either record;
- merge either record;
- retract either record;
- supersede either record;
- establish either record as authoritative;
- establish either record as inadmissible.

Contradictory records MUST remain independently inspectable and traceable.

### 10.1 Independent Authority Evaluation

Each record participating in a contradiction MUST be evaluated against its
own knowledge type, evidence, lineage, integrity, validation, and applicable
authority policy.

One record's authority outcome MUST NOT be inferred solely from the authority
outcome of the other record.

Therefore, two contradictory records MAY both be authoritative when each
independently satisfies the applicable authority requirements.

### 10.2 No Silent Reconciliation

The authority layer MUST NOT silently reconcile contradictory propositions
into a new conclusion.

Any new conclusion derived from competing records MUST be represented as a
distinct KnowledgeRecord with explicit derivation and provenance.

The originating contradictory records MUST remain preserved and traceable.

### 10.3 Supersession and Contradiction

Contradiction and supersession have different meanings.

A contradiction identifies competing propositions.

A supersession identifies an authorized historical replacement.

A contradiction MUST NOT be interpreted as supersession unless an explicit
authorized supersession transition and corresponding lineage evidence exist.


## 11. Historical Change Operations

Historical change MUST preserve the identity and provenance of every affected
KnowledgeRecord.

### 11.1 Supersession

Supersession represents an authorized historical replacement.

A supersession MUST:

1. identify the predecessor record;
2. identify the successor record;
3. preserve both record identities;
4. establish explicit lifecycle lineage between them;
5. preserve the predecessor's historical authority state;
6. record the authorization and supporting evidence required by policy.

Supersession MUST NOT be implemented by overwriting the predecessor's
KnowledgeRecord content.

The successor MUST undergo its own applicable authority evaluation.

### 11.2 Split

A split represents the decomposition of one historical record into multiple
distinct records.

A split MUST:

- preserve the source record;
- create independently identifiable resulting records;
- establish explicit `split_from` lineage;
- preserve provenance to the source record;
- evaluate each resulting record independently for authority.

A split MUST NOT erase the source record merely because its knowledge has been
decomposed.

### 11.3 Merge

A merge represents the authorized convergence of multiple historical records
into a new record.

A merge MUST:

- preserve every source record;
- create an independently identifiable resulting record;
- establish explicit `merged_into` lineage for each source;
- preserve provenance from every source;
- evaluate the resulting record independently for authority.

A merge MUST NOT retroactively rewrite the historical meaning of its source
records.

### 11.4 Historical Conservation Invariant

For every supersession, split, or merge:

Record identities MUST be conserved.

Historical events MUST be conserved.

Lineage MUST remain traceable.

Provenance MUST remain traceable.

No operation may silently delete, overwrite, or collapse an existing
historical record.


## 12. Three-Valued Authority Outcome

Authority evaluation MUST produce an explicit epistemic outcome:

ADMISSIBLE
INADMISSIBLE
UNDETERMINED

These outcomes are distinct from the authority lifecycle states defined in
Section 3.

### 12.1 ADMISSIBLE

ADMISSIBLE means the record satisfies all applicable authority and
admissibility requirements for the evaluated context.

Only ADMISSIBLE records may proceed to an execution or compilation boundary
that requires authoritative knowledge.

### 12.2 INADMISSIBLE

INADMISSIBLE means at least one required condition has definitively failed.

A definitive failure MUST NOT be converted into UNDETERMINED merely because
other conditions pass.

### 12.3 UNDETERMINED

UNDETERMINED means the available information is insufficient to establish
ADMISSIBLE or a definitive INADMISSIBLE result.

Examples include:

- missing required evidence;
- unresolved lineage;
- unavailable validation;
- insufficient integrity information;
- incomplete policy inputs;
- unresolved required context.

UNDETERMINED MUST remain explicitly observable as an epistemic outcome.

### 12.4 Fail-Closed Execution Rule

For execution, selection, substitution, and Context Assembly:

ExecutionAdmissible(M,R,C) ⇔ Admissible(M,R,C) = ADMISSIBLE

Therefore:

UNDETERMINED → not executable
INADMISSIBLE → not executable
Only ADMISSIBLE → eligible to proceed to the applicable execution or compilation boundary

For epistemic promotion, ADMISSIBLE is necessary but is not by itself
sufficient authorization. Promotion MUST additionally satisfy the
authorization and transition requirements defined in Section 9.

No downstream component may reinterpret UNDETERMINED as permission to proceed.
### 12.5 Separation From Lifecycle State

Authority lifecycle state and admissibility outcome answer different questions.

Authority state describes the epistemic lifecycle of a KnowledgeRecord.

Admissibility describes whether the record satisfies the applicable
requirements for a particular evaluated use.

Therefore a lifecycle state MUST NOT be treated as a direct substitute for an
admissibility outcome.

### 12.6 Lifecycle-to-Admissibility Invariant

Authority lifecycle state and admissibility outcome MUST be evaluated as
separate dimensions.

The following invariant applies:

- VERIFIED is a necessary lifecycle condition for current authoritative use
  only where the active policy requires authoritative knowledge;
- VERIFIED alone MUST NOT establish ADMISSIBLE;
- SUPERSEDED and RETRACTED records MUST NOT be treated as currently
  authoritative by default;
- DRAFT, STRUCTURED, and CONNECTED records MUST NOT be treated as currently
  authoritative;
- any lifecycle state may still produce an explicitly evaluated
  INADMISSIBLE or UNDETERMINED outcome according to the applicable policy and
  context;
- historical addressability MUST NOT be confused with current admissibility.

Therefore, lifecycle state constrains admissibility evaluation, but does not
replace it.

The admissibility evaluator MUST preserve both dimensions in its observable
result:

AuthorityState(n)

and

Admissible(n,R,C) ∈ {ADMISSIBLE, INADMISSIBLE, UNDETERMINED}

A downstream component MUST NOT infer one dimension solely from the other
when the applicable policy requires explicit evaluation.
