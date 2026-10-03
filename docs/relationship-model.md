# AM-PKO Relationship Model

## Purpose

The AM-PKO relationship layer represents explicit semantic and structural connections between knowledge records.

Relationships are not unrestricted links. Each relationship expresses a defined claim about how two records are connected.

## Relationship Types

The current AM-PKO relationship vocabulary includes:

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

Each relationship type has its own intended meaning and should not be substituted for another merely because the records are related.

## Directionality

Relationships are directional where the semantics require direction.

For example:

```text
K-000001 → K-000002
supports
