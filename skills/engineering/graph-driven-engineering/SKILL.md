---
name: graph-driven-engineering
description: Coordinate dependency-heavy, multi-stage engineering work with a work graph, explicit node contracts, artifact provenance, parallel execution waves, verification gates, and resumable checkpoints. Use when a task has several interdependent work items, crosses components or specialist skills, needs safe fan-out/fan-in, or must survive handoffs and later sessions. Do not use for a simple local change or one standalone research, specification, debugging, implementation, refactoring, testing, or code-review task; those specialist skills retain ownership. Build a code dependency graph only when it materially changes ordering, blast-radius analysis, or validation.
compatibility: Works with Markdown-capable coding agents and existing specialist skills. No external graph database, AST indexer, or service is required.
---

# Graph-Driven Engineering

Act as the thin manager of complex engineering work. Turn the goal into a governed graph, route each node to its rightful owner, require evidence at fan-in, and keep a small source of truth that another agent can resume. Do not absorb the specialist work into this skill.

## Core responsibility

Own only four things:

1. Convert the goal into a dependency-aware work graph.
2. Identify safe execution waves and shared-resource constraints.
3. Define the artifact and evidence each node must return.
4. Verify completed nodes and fan them into the next wave or final result.

Research, specification, diagnosis, design, coding, testing, security, documentation, and review remain owned by the relevant skill or project workflow.

## Activation gate

Use the full workflow when the task has at least three meaningful work nodes and one of these is true:

- execution order or parallelism affects correctness;
- multiple components, owners, or specialist skills must coordinate;
- outputs must share evidence or converge through a verification gate;
- the work must be resumable across agents or sessions;
- a change has a non-obvious blast radius.

Use a lightweight single-page graph for two-node, high-risk work. Do not activate for a self-contained specialist task or a straightforward local edit. A keyword such as “research”, “debug”, “review”, “plan”, or “graph” is not sufficient by itself.

## Three-layer model

| Layer | Default | Purpose |
|---|---|---|
| Work Graph | Always | Goal, work nodes, dependencies, waves, owners, and gates |
| Artifact Graph | Always | Which node produces or consumes each artifact and evidence item |
| Code Graph | Optional | Code-level dependency and blast-radius context when it changes execution decisions |

Read `references/graph-schema.md` when constructing the graph. Read `references/optional-code-graph.md` only after the activation rule in that file is met.

## Fast workflow

1. **Resume or initialize.** Load the existing source of truth and checkpoint. If none exists, create them from the templates.
2. **Bound the goal.** Record outcome, exclusions, constraints, definition of done, and current mode.
3. **Build the Work Graph.** Create the smallest set of nodes that changes execution. Give each node the contract in `references/node-contract.md`.
4. **Build the Artifact Graph.** Connect node outputs to downstream inputs. Reuse evidence instead of rediscovering it.
5. **Schedule waves.** Run only `ready` nodes. Parallelize nodes with satisfied dependencies and no shared-resource conflict.
6. **Delegate.** Give the specialist a bounded node contract. The specialist owns the domain result; this skill owns routing and state.
7. **Verify and fan in.** Check the node's output and evidence against its gate before unlocking dependents.
8. **Checkpoint.** Update the source of truth, evidence ledger, unresolved queue, graph state, and next safe action.

Prefer a shallow graph. Stop expanding when another node cannot change ownership, ordering, risk, or validation.

## Routing modes

Modes change graph context, not specialist ownership.

| Mode | Graph responsibility | Specialist owner |
|---|---|---|
| PLAN | Scope nodes, dependencies, waves, artifacts, and gates | Research/specification/design workflows own their conclusions |
| CODE | Bound the change surface and validation edges | Coding workflow owns edits; testing workflow owns test strategy when specialized |
| DEBUG | Track symptom, hypotheses, evidence, and impacted paths | Debugging skill owns reproduction and root cause |
| REFACTOR | Compare current/target graphs and migration gates | Codebase-design and coding workflows own design and implementation |
| REVIEW | Supply the changed-surface graph and risk-bearing edges | Code-review skill owns findings and severity |

For Matt Pocock skills and other specialist workflows, follow `references/interoperability-with-other-skills.md`.

## Node lifecycle and validation

Use these states: `pending -> ready -> running -> complete`. A node may move to `blocked` from any active state, or to `invalidated` when upstream evidence changes. Do not unlock downstream nodes merely because work was attempted.

Apply five gates:

- **Start:** outcome, boundary, and graph scope are clear.
- **Ready:** dependencies are complete, required inputs exist, and the owner is assigned.
- **Node complete:** expected artifact exists and its evidence satisfies the node's verification rule.
- **Fan-in:** outputs agree on shared contracts; conflicts are resolved or queued as blocking.
- **Finish:** definition of done is met, required nodes are verified, and unresolved non-blockers are disclosed.

## Persistent and resumable artifacts

Use the project's approved artifact location. Otherwise use `artifacts/graph-driven-engineering/<work-id>/` with:

- `plan.md` — goal, Work Graph, waves, node contracts, and gates;
- `source-of-truth.md` — current graph state, decisions, completed outputs, mode, and next action;
- `evidence.md` — provenance, claim-to-source links, verification results, and contradictions;
- `checkpoint.json` — compact machine-readable resume pointer.

Initialize the Markdown files from `templates/`. Keep them concise and update existing records rather than creating parallel truth files. See `references/artifact-contract.md` for checkpoint and staleness rules.

## Unresolved queue

Record each unknown, conflict, failed gate, or deferred risk with `id`, `question`, `impact`, `owner`, `blocking`, `evidence-needed`, `next-action`, and `stale-after`. Prioritize critical-path and high-blast-radius items. A blocking item prevents the dependent node from becoming `ready`.

## Minimal-change strategy

In CODE or REFACTOR mode, begin from the behavior or contract that must change. Traverse only the dependency path needed to identify the narrowest stable seam and its validators. Avoid opportunistic cleanup. Require a focused proof for the changed edge, then run broader validation only in proportion to reverse reachability and contract risk.

## Delegation and fan-in contract

Every delegated node includes its objective, inputs, relevant edges, owner, expected artifact, evidence rule, stop condition, and unresolved questions. On return, verify the artifact; do not rewrite the specialist's conclusion into a competing result. If two outputs conflict, create a resolution node rather than choosing silently.

## Completion report

Report the outcome, graph delta, completed and blocked nodes, specialist results, gates passed or failed, unresolved queue, artifact location, and next safe action. Do not claim completion while a required node or fan-in gate is unresolved.
