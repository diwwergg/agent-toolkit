# Interoperability with other skills

Read this reference before delegating or when another skill appears likely to trigger for the same request.

## Precedence rule

The specialist owns the specialized activity; Graph Engineering owns the coordination state. Do not duplicate the specialist's output, change its conclusion without evidence, or issue a second broad investigation just because the graph is incomplete. Pass context in, receive a bounded artifact out, and update the graph.

## Routing table

| Need | Delegate to | Graph Engineering contributes | Graph Engineering records |
|---|---|---|---|
| Source discovery and synthesis | Research skill | Questions, source boundaries, deduplication ids | Claims, references, freshness, unresolved conflicts |
| Formal requirements or acceptance criteria | Specification skill | Affected nodes, consumers, constraints | Decision, criteria, contract edges |
| Reproduction and root-cause diagnosis | Debugging skill | Symptom graph, hypotheses, impact candidates | Evidence, hypothesis status, fix gate |
| Module/interface design | Codebase-design or architecture workflow | Current/target graph and seams | Design decision, tradeoffs, migration edges |
| Implementation or refactor | Coding/refactoring workflow | Minimal change surface and tests to protect | Changed nodes, diff rationale, validation |
| Review findings | Code-review skill | Changed-surface graph and risk-bearing edges | Findings, dispositions, review gate |

Use the exact skill available in the host environment. If no specialist is available, state the gap and use the narrowest ordinary workflow that can safely produce the needed artifact.

## Collision-avoidance rules

- Trigger Graph Engineering for coordination complexity, not for a keyword such as “research,” “debug,” “spec,” or “review” alone.
- Do not rename or imitate a specialist skill's role in prompts or artifacts.
- Do not ask two specialists to independently solve the same question unless an explicit independent check is the goal.
- Preserve specialist terminology and conclusions; add graph metadata around them.
- Keep handoffs bounded by nodes, questions, artifacts, and stop conditions.
- If a specialist is already active, join its context with a graph checkpoint instead of launching a competing workflow.

## Handoff example

```text
To: debugging skill
Objective: identify why the order endpoint returns stale totals
Mode: DEBUG
Relevant nodes: orders handler -> totals service -> cache key -> integration test
Known evidence: reproduction id R-14; cache key changed in commit X
Open hypotheses: invalidation path, serialization mismatch
Expected output: root-cause note, minimal fix boundary, regression test
Validation: reproduce before and after; run focused integration test
Stop condition: stop after one evidence-backed root cause or report blocked
```

On return, attach the specialist result to the same graph version, mark hypotheses, and move only the requested fix into CODE mode. The debugging skill remains the owner of diagnosis; the coding workflow remains the owner of the edit.
