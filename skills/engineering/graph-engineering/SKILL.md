---
name: graph-engineering
description: Orchestrate complex, cross-layer engineering work by modeling dependencies, batching discovery, tracing impact, and preserving resumable execution artifacts. Use this skill when a task spans multiple components, files, architectural layers, or execution stages and needs a traceable plan or checkpointed handoff. Do not use it for a simple local edit or as a replacement for specialized research, debugging, specification, coding, refactoring, or code-review skills; it coordinates those skills and leaves domain ownership with them.
compatibility: Requires a workspace where Markdown files can be read and written. Uses no external service or framework.
---

# Graph Engineering

Use this skill as a thin orchestration layer for engineering work whose difficulty comes from dependencies, uncertainty, or coordination. The graph is a decision aid and a durable handoff contract: it should make the next useful action obvious without forcing every task into a heavyweight process.

## Role and boundaries

Graph Engineering owns:

- deciding whether graph coordination is warranted;
- defining the work boundary, nodes, edges, phases, and checkpoints;
- batching discovery so the same code, document, or source is not repeatedly traversed;
- recording impact, evidence, decisions, validation results, and unresolved work;
- routing each specialized activity to the skill or workflow that owns it.

It does not become a second research, debugging, specification, implementation, or review skill. It may inspect enough context to build the graph, but it must not repeat a specialist's investigation merely to produce a competing answer. When a specialist is active, treat its output as the authoritative domain result and update the graph around it.

Read only the reference needed for the current stage:

- Planning or scope: `references/graph-planning.md`
- Code structure: `references/code-dependency-graph.md`
- Changed-surface reasoning: `references/impact-analysis.md`
- Sources, claims, and unknowns: `references/evidence-and-references.md`
- Checkpoints and saved work: `references/execution-artifacts.md`
- Handoffs and collision avoidance: `references/interoperability-with-other-skills.md`

## Activation gates

Activate the full workflow when at least one strong signal or two moderate signals are present.

Strong signals:

- The request crosses two or more architectural layers or independently owned components.
- A change, defect, or decision can affect multiple consumers, paths, interfaces, tests, or deployments.
- The user asks for dependency mapping, impact analysis, traceability, staged execution, or resumability.

Moderate signals:

- Discovery is likely to revisit the same files, APIs, documents, or sources.
- The work contains material unknowns, competing hypotheses, or a meaningful unresolved queue.
- Several actions can be safely prepared in parallel but must be merged through validation gates.
- The user may pause and resume the work or hand it to another agent.

Do not activate the full workflow for a single-file/local edit, a direct explanation, a standalone source investigation, a standalone bug diagnosis, a standalone specification, or a standalone review. In those cases, let the specialized workflow own the task. If the boundary is unclear, create only a lightweight one-page graph and stop once routing is clear.

## Fast graph-engineering workflow

1. **Set the boundary.** Write the desired outcome, explicit exclusions, constraints, current mode, and definition of done. Record assumptions instead of hiding them.
2. **Inventory the graph.** Represent relevant files, modules, services, data stores, interfaces, tests, configuration, people/skills, and artifacts as nodes. Add only evidence-backed edges; label inferred edges and confidence.
3. **Find the critical path.** Identify the smallest dependency chain that can prove or disprove the outcome. Separate required work from useful but non-blocking exploration.
4. **Batch discovery.** Group reads and questions by node or concern. Reuse one finding across downstream tasks and avoid asking multiple specialists to answer the same question.
5. **Choose a mode.** Use PLAN, CODE, DEBUG, REFACTOR, or REVIEW below. A task can change modes, but record the transition and its gate.
6. **Delegate by ownership.** Send a bounded request with graph context, relevant nodes, evidence, expected artifact, and stop condition. The receiving skill owns its domain result.
7. **Run validation gates.** Validate graph coverage, evidence, impact, implementation, and review at the appropriate points. Failed gates create explicit queue items rather than silent assumptions.
8. **Checkpoint.** Save the graph delta, decisions, delegated results, validation status, and unresolved queue before a pause or handoff. On resume, load the checkpoint first and revalidate only stale or changed edges.

## Modes

### PLAN

Produce a dependency-aware plan without implementing. Define nodes, edges, critical path, risks, sequence, parallel-safe work, delegation targets, artifacts, and validation gates. Delegate factual discovery or domain specification to the appropriate specialist; do not write a competing research report or spec.

### CODE

Use the graph to constrain implementation to the smallest safe change. Confirm the change surface, contracts, callers, tests, configuration, and rollback boundary before editing. Prefer one coherent change over speculative cleanup. The normal coding workflow or project coding skill owns implementation; Graph Engineering tracks why each touched node is necessary, then routes review and verification to their owners.

Minimal-change strategy:

1. Start from the user-visible behavior or failing contract.
2. Traverse only the affected dependency path and its validation edges.
3. Change the narrowest stable seam that satisfies the contract.
4. Preserve unrelated behavior and avoid opportunistic renames or formatting.
5. Add or adjust the smallest test that proves the changed edge.
6. Recompute reverse impact after the edit and run proportionate validation.

### DEBUG

Freeze the current graph and record the symptom, reproduction, expected behavior, observed behavior, environment, and competing hypotheses. Delegate reproduction, diagnosis, and fix ownership to the debugging skill or workflow. The graph layer maintains hypothesis status, evidence links, affected nodes, and validation checkpoints; it must not invent a root cause from dependency proximity alone.

### REFACTOR

Model the current and target dependency graphs, preserving externally observable contracts. Identify seams, cycles, ownership boundaries, and migration/rollback edges. Delegate design judgment to the codebase-design or coding workflow and verification to tests/review. Require an explicit equivalence or compatibility gate before deleting or redirecting a node.

### REVIEW

Build the changed-surface graph from the diff, then hand the bounded review context to the code-review skill. Include affected nodes, reverse consumers, contracts, risk assumptions, tests run, and unresolved items. The review skill owns findings and severity; Graph Engineering only checks that the review covered the graph's risk-bearing edges and records follow-up work.

## Persistent and resumable execution

Use a project-approved location when one exists. Otherwise save artifacts under `artifacts/graph-engineering/<work-id>/` (or an equivalent user-approved workspace directory). Keep the graph human-readable and append deltas instead of overwriting history. At minimum preserve:

- `00-context.md` — boundary, mode, constraints, and definition of done;
- `01-graph.md` — nodes, edges, confidence, and critical path;
- `02-evidence.md` — claims, references, freshness, and provenance;
- `03-plan.md` — ordered work, delegation, and gates;
- `04-log.md` — chronological actions, results, and mode changes;
- `05-unresolved.md` — unresolved queue with owner, blocker, next action, and expiry/staleness;
- `checkpoint.json` — machine-readable resume pointer and artifact versions.

If the task is too small for the full bundle, use one Markdown status file with the same fields. Never claim resumability when the graph, decisions, and unresolved queue were not saved.

## Unresolved queue

Turn every blocker, unknown, stale edge, failed gate, and deferred risk into a queue item. Each item has: `id`, `question`, `impact`, `owner`, `status`, `evidence-needed`, `next-action`, `blocking`, and `stale-after`. Prioritize items on the critical path or with high blast radius. Close an item only when evidence and the relevant validation gate are recorded.

## Validation gates

Use only gates relevant to the current mode, but make the decision explicit:

- **Boundary gate:** outcome, exclusions, constraints, and done condition are clear.
- **Graph gate:** every planned change has a reason, owner, and known consumers; inferred edges are labeled.
- **Evidence gate:** important claims have a source, artifact, test, or specialist result; freshness is acceptable.
- **Impact gate:** reverse consumers, interfaces, tests, configuration, and operational paths were considered.
- **Implementation gate:** the diff is minimal, contracts are preserved, and targeted tests or checks pass.
- **Handoff gate:** the receiver has context, scope, expected output, stop condition, and unresolved items.
- **Review gate:** the change-bearing graph edges were reviewed by the review owner and findings are dispositioned.

When a gate fails, do not paper over it with a confidence statement. Add or update an unresolved item and choose the smallest action that can satisfy the gate.

## Delegation contract

Every handoff should state:

```text
Objective:
Mode and scope:
Relevant graph nodes/edges:
Known evidence:
Open hypotheses or questions:
Expected output/artifact:
Validation required:
Stop condition:
```

Use explicit ownership boundaries. Research skills own source discovery and synthesis; specification skills own acceptance criteria and formal requirements; debugging skills own reproduction and root-cause diagnosis; coding/refactoring workflows own edits; code-review skills own review findings. Graph Engineering supplies context, prevents duplicate traversal, and records the returned result. See `references/interoperability-with-other-skills.md` for the detailed routing table.

## Completion report

End with a compact status snapshot containing: mode, outcome, graph delta, delegated results, validations passed/failed, remaining unresolved items, saved artifact location, and the next safe action. If work is blocked, name the exact missing input or failed gate and avoid presenting a speculative completion.
