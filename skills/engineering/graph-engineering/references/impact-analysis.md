# Impact analysis

Read this reference after a candidate change, diagnosis, or design decision exists and before implementation or sign-off.

## Impact dimensions

Assess impact across:

- direct callers and reverse consumers;
- public contracts, schemas, serialization, and compatibility;
- data ownership, reads/writes, migrations, and backfills;
- configuration, flags, permissions, and environment-specific behavior;
- tests, fixtures, generated artifacts, and documentation;
- runtime, deployment, observability, queues, retries, and failure paths;
- specialist ownership and handoff dependencies.

## Procedure

1. Mark the changed or hypothesized root node.
2. Traverse reverse edges to discover consumers and downstream behavior.
3. Traverse validation edges to find tests, checks, and operational evidence.
4. Classify each reachable node as required, likely, possible, or out of scope.
5. Record blast radius, confidence, and the smallest validation that can reduce uncertainty.
6. Add high-impact unknowns to the unresolved queue with an owner and next action.

## Risk scoring

Use qualitative scoring unless the project already has a quantitative model:

```text
risk = reachability × contract-sensitivity × uncertainty × reversibility-cost
```

High risk commonly means a public contract, shared data, security boundary, deployment path, or many reverse consumers. High uncertainty means an inferred edge, missing test, undocumented behavior, or conflicting specialist result. High reversibility cost means a migration, data rewrite, public release, or difficult rollback.

## Impact matrix

| Surface | Question | Evidence or gate |
|---|---|---|
| Behavior | What user/system behavior changes? | Reproduction, acceptance criterion, or contract |
| Consumers | Who calls, reads, or relies on it? | Reverse dependency traversal |
| Data | What is written, migrated, cached, or serialized? | Schema, query, migration, or runtime evidence |
| Operations | What can fail in production? | Deployment/config/observability checks |
| Verification | What proves safety? | Focused tests plus proportionate broader checks |
| Ownership | Who decides or validates this surface? | Explicit delegation and returned artifact |

## Exit criteria

Impact analysis is sufficient when the changed surface, reverse consumers, major operational paths, validation scope, and remaining uncertainty are explicit. It is not necessary to prove that every file is unaffected; it is necessary to make the risk-bearing edges visible and justified.
