# Graph schema

Use this reference to create the smallest graph that controls execution.

## Layers

### Work Graph

A Work Graph node is a bounded unit of work with one owner and one verifiable result. Useful edge types are:

- `depends_on` — target cannot start until source is verified;
- `blocks` — source contains an unresolved condition that prevents target readiness;
- `shares_resource` — nodes may conflict on a file, contract, environment, or external system;
- `requires_approval` — a user or authority gate is needed;
- `validates` — source proves or disproves target completion.

### Artifact Graph

An Artifact Graph connects work to durable outputs:

- `produces` — a node creates or updates an artifact;
- `consumes` — a node requires an artifact as input;
- `supports` — an evidence item supports a claim or edge;
- `supersedes` — a newer artifact replaces a stale version without erasing history.

### Code Graph

Code Graph nodes and edges are optional. Add them only under `optional-code-graph.md`.

## Minimal node record

```text
id | objective | owner | status | inputs | output | evidence | gate | dependencies
```

Use stable short ids such as `N1`, `N2`, and `V1`. Put detail in the node contract rather than encoding prose in the id.

## Legal state transitions

```text
pending -> ready       dependencies and inputs satisfied
ready -> running       owner accepts the node
running -> complete    output exists and verification passes
* -> blocked           missing input, failed gate, or external blocker
blocked -> ready       blocker resolved and readiness rechecked
complete -> invalidated upstream evidence or contract changed
invalidated -> ready   scope and inputs refreshed
```

Attempted work is not completion. A completed node with stale evidence becomes `invalidated` when the staleness can affect downstream decisions.

## Execution waves

Compute waves from verified dependencies:

1. Put all `ready` nodes without shared-resource conflicts in the current wave.
2. Delegate each node once to one owner.
3. Verify returned artifacts independently at the node gate.
4. Resolve conflicts at fan-in.
5. Unlock the next wave only from verified outputs.

If the graph contains a cycle, do not pretend it is a valid schedule. Collapse tightly coupled nodes into one node, identify an interface that can break the cycle, or create a decision node that resolves the dependency.

## Stop rule

Stop graph expansion when the next node or edge cannot change execution order, ownership, artifact flow, risk, or validation. Repository completeness is not the goal; governed execution is.
