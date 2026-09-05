# Node contract

Use one contract per work node. It is both a delegation prompt and a verification boundary.

## Contract

```yaml
id: N1
objective: One observable result
mode: PLAN | CODE | DEBUG | REFACTOR | REVIEW
owner: Specialist skill or project workflow
status: pending | ready | running | blocked | complete | invalidated
inputs:
  - Artifact or evidence id
relevant_edges:
  - Upstream/downstream relationship needed for this node
constraints:
  - Scope, compatibility, safety, or shared-resource limit
expected_output:
  artifact: Path or result type
  contents: Required fields or conclusions
evidence_rule: What proves the result is trustworthy
verification: Check to run before marking complete
stop_condition: Point where the owner must return rather than expand scope
unresolved:
  - Question or blocker id
```

## Ownership rules

- Assign one accountable owner. Collaborators may contribute evidence but do not create a second authoritative result.
- Keep the objective narrow enough that one specialist can finish and verify it.
- Pass existing artifact and evidence ids so the owner does not rediscover context.
- Require the owner to return limitations and unresolved questions with the artifact.
- If the requested work crosses specialties, split it into nodes joined by an artifact edge.

## Delegation message

```text
Objective:
Mode and scope:
Inputs and evidence ids:
Relevant graph edges:
Expected artifact:
Verification rule:
Stop condition:
Open questions:
```

The graph manager may reject an incomplete return at the node gate, but must not replace the specialist's domain judgment with its own. Create a follow-up node for missing work.

## Parallel safety

Two nodes may run together only when their dependencies are verified and they do not write the same source, mutate the same environment, redefine the same contract, or require contradictory assumptions. Parallel reading is usually safe; parallel editing of overlapping contracts is not.

## Fan-in

At fan-in, check artifact presence, evidence quality, shared-contract consistency, and unresolved blockers. When outputs conflict, preserve both and create a bounded resolution node owned by the relevant specialist.
