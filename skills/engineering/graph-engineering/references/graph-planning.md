# Graph planning

Read this reference when planning a multi-component task or deciding whether a graph is worth the overhead.

## Planning model

Start with a bounded outcome rather than a list of files. Capture:

- outcome and definition of done;
- inclusions, exclusions, constraints, and compatibility expectations;
- current mode and likely mode transitions;
- known entry points, consumers, environments, and owners;
- assumptions that must be tested.

Represent work as a directed graph:

```text
node = thing that can change, constrain, consume, validate, or own work
edge = relationship that affects order, risk, evidence, or ownership
```

Useful edge labels include `calls`, `imports`, `reads`, `writes`, `configures`, `deploys`, `tests`, `documents`, `blocks`, `owns`, and `validates`. Do not add an edge merely because two nodes look related. Mark `observed`, `inferred`, or `unknown`, with confidence and evidence.

## Planning procedure

1. List the outcome and boundary.
2. Seed nodes from the request, entry point, and likely consumers.
3. Expand only one dependency hop at a time.
4. Mark critical-path nodes, parallel-safe nodes, and risk-bearing nodes.
5. Separate discovery, decision, change, and validation tasks.
6. Assign one owner to each task and one artifact to carry its result.
7. Order tasks by information gain and dependency readiness.
8. Add a gate after each irreversible or high-blast-radius step.

Prefer a shallow, useful graph over exhaustive repository mapping. Stop expansion when additional nodes cannot change the plan, risk assessment, or validation choice.

## Planning table

| Field | Meaning |
|---|---|
| Node | File, module, service, contract, test, artifact, or owner |
| Role | Entry point, dependency, consumer, validator, or constraint |
| Edge | Why this node affects another node |
| Status | Unknown, discovered, planned, changed, validated, or stale |
| Confidence | High, medium, low; include the reason |
| Owner | Specialist or workflow responsible for the next result |
| Gate | Evidence required before advancing |

## Critical-path heuristic

Prioritize a node when it has high downstream reachability, high uncertainty, or sits on an external contract. A low-confidence edge with many consumers is usually more valuable to verify than a high-confidence leaf. Parallelize independent discovery, not changes that touch the same contract or file.

## Exit criteria

A plan is ready when the outcome and boundary are clear, the critical path is evidence-backed enough to act, every planned action has an owner and artifact, and the unresolved queue identifies what could still change the plan.
