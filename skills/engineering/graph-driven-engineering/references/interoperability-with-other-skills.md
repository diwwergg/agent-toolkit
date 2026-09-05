# Interoperability with other skills

The specialist owns domain work; Graph-Driven Engineering owns orchestration state. Use the exact specialist available in the host environment.

## Routing

| Need | Preferred owner | Graph contribution | Returned artifact |
|---|---|---|---|
| Primary-source investigation | Research skill, such as Matt Pocock `research` | Bounded questions, evidence ids, downstream consumers | Findings, sources, limitations |
| Requirements and acceptance criteria | Specification workflow | Goal, affected contracts, unresolved decisions | Authoritative spec or criteria |
| Reproduction and root cause | Debugging skill, such as `diagnosing-bugs` | Symptom node, path context, hypotheses, evidence gaps | Reproduction, root cause, fix boundary |
| Interface or module design | `codebase-design` or architecture workflow | Current/target graph and constraints | Design decision and tradeoffs |
| Terminology or ADR work | `domain-modeling` | Relevant concepts, owners, and decisions | Updated model or ADR |
| Test-first implementation | `tdd` | Change boundary and validation edge | Tests, implementation result, evidence |
| Merge/rebase conflicts | `resolving-merge-conflicts` | Competing graph changes and shared contracts | Resolved state and validation |
| Code review | `code-review` | Changed-surface graph, risks, and tests run | Findings and severity |

## Conflict prevention

- Trigger this skill because coordination is complex, not because a specialist keyword appears.
- Delegate each question once. Use parallel specialists only for explicitly independent or adversarial checks.
- Never ask this skill and a specialist to produce competing research, diagnosis, spec, implementation, or review conclusions.
- Preserve specialist terminology, evidence, uncertainty, and severity in the source of truth.
- Pass a node contract with a stop condition so the specialist does not expand into orchestration.
- If a specialist is already active, attach its result to a node instead of restarting the task.

## Precedence

User instructions and project rules remain authoritative. Within their scope, the specialist's workflow governs how its domain work is performed. Graph-Driven Engineering may sequence, constrain, and verify the returned artifact, but it does not override the specialist's required method.

If no specialist exists, route the node to the narrowest ordinary project workflow and record that fallback as the owner.
