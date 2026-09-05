# Optional code graph

Do not build a Code Graph by default. Activate this module only when code relationships materially change work ordering, blast radius, ownership, or validation scope.

## Activation signals

Use it when at least one is true:

- a public interface or shared schema has multiple reverse consumers;
- a defect crosses runtime layers and diagnosis needs path context;
- a refactor moves ownership or changes dependency direction;
- configuration, generated code, data flow, or deployment edges are easy to miss;
- a specialist requests a bounded dependency or impact map.

Skip it for a local implementation with obvious callers and focused tests.

## Nodes and edges

Choose stable nodes such as module, API, handler, service, job, schema, table, event, test, configuration key, deployment unit, or external contract. Use edges such as `calls`, `imports`, `reads`, `writes`, `publishes`, `subscribes`, `configured_by`, `generated_from`, `tested_by`, and `deployed_with`.

Record:

```text
source -> target | relationship | observed/inferred | evidence | confidence | stale-after
```

## Bounded traversal

Start from the behavior, contract, failing path, or proposed seam. Traverse direct dependencies, reverse consumers, validators, and operational edges. Stop when the next hop cannot change the planned edit, risk, owner, or check.

Use an existing code-graph/indexing tool when the project already has one. Otherwise inspect the repository with normal code navigation. This skill must not require AST indexing or a graph database.

## Minimal-change decision

Prefer the narrowest stable seam that satisfies the contract. Preserve unrelated behavior, avoid opportunistic cleanup, and add the smallest proof for the changed edge. Broaden validation according to reverse reachability, public-contract sensitivity, uncertainty, and rollback cost.

Return the bounded Code Graph as an input artifact to the appropriate debugging, design, coding, testing, or review owner. The graph manager does not take over that specialist's work.
