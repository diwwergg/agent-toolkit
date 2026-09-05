# Code dependency graph

Read this reference for code changes, refactors, architecture work, or reviews where repository structure matters.

## Node types

Use the smallest useful stable unit:

- repository/package and build target;
- file, module, class, function, route, handler, job, or schema;
- public interface, event, database table, cache key, feature flag, or configuration key;
- unit, integration, contract, end-to-end, or monitoring check;
- deployment, runtime, queue, or external service boundary.

Avoid making every local variable a node. A symbol becomes a node when it is an entry point, contract, shared dependency, risk-bearing branch, or validation target.

## Edge types

Record direct edges such as `imports`, `calls`, `constructs`, `implements`, `reads`, `writes`, `publishes`, `subscribes`, `routes-to`, `configured-by`, `generated-from`, `tested-by`, and `deployed-with`. Record indirect edges only when an artifact or specialist result supports them.

For each edge capture:

```text
source -> target | relationship | observed/inferred/unknown | confidence | evidence | stale-after
```

## Traversal strategy

Begin at the changed behavior, failing test, public contract, or requested entry point. Traverse outward to direct dependencies and reverse consumers. Then inspect validation and operational edges. Stop when the next hop cannot alter the change, risk, test scope, or owner.

For a proposed edit, answer:

1. Which behavior or contract changes?
2. Which callers, consumers, writers, readers, and serializers depend on it?
3. Which tests and configurations encode the old behavior?
4. Which runtime or deployment paths can expose the change?
5. Which edges are inferred and therefore need validation?

## Graph quality checks

- Every changed node has at least one reason and one validation edge.
- Public or shared nodes have reverse-consumer coverage.
- Generated files point to their source of truth.
- Configuration and feature flags are included when behavior depends on them.
- Test coverage is not treated as proof of absence of operational impact.
- Stale or inferred edges are visible rather than silently promoted to facts.

## Minimal-change rule

Prefer changing a narrow stable seam with a focused test over reshaping the graph. Do not use the graph as a reason to perform unrelated cleanup. If a broader refactor is justified, model current and target graphs separately and add a compatibility or migration gate.
