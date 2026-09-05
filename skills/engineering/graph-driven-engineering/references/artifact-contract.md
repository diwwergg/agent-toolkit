# Artifact contract

Artifacts make the graph observable, testable, and recoverable without forcing a graph database or proprietary runtime.

## Required files

Use the templates in `../templates/`.

### plan.md

Holds the stable goal, scope, Work Graph, execution waves, node contracts, and validation gates. Change it when the plan changes, not after every observation.

### source-of-truth.md

Holds current state: active mode, graph version, node status, decisions, artifact index, unresolved queue, last verified gate, and next safe action. This is the first file read on resume.

### evidence.md

Holds material claims and verification results. Each record links a claim or edge to a source, test, repository location, specialist result, or runtime observation. Label observation, inference, contradiction, confidence, and freshness.

### checkpoint.json

Use this compact shape:

```json
{
  "work_id": "stable-id",
  "graph_version": "v1",
  "mode": "PLAN",
  "status": "active",
  "last_verified_gate": "start",
  "ready_nodes": [],
  "running_nodes": [],
  "blocked_nodes": [],
  "unresolved_ids": [],
  "stale_evidence_ids": [],
  "next_safe_action": "...",
  "updated_at": "ISO-8601"
}
```

## Provenance rules

- Give artifacts and material evidence stable ids.
- Record who or which skill produced the result and under what scope.
- Link downstream claims to evidence ids instead of duplicating source interpretation.
- Mark inferred edges and stale evidence explicitly.
- Preserve conflicting results until a specialist-owned resolution node closes them.
- Do not copy secrets or unnecessary private source content into coordination artifacts.

## Resume procedure

1. Read `checkpoint.json` and `source-of-truth.md`.
2. Confirm referenced inputs and shared contracts have not changed.
3. Revalidate only stale evidence and the edges it can affect.
4. Resume from `ready_nodes` or the recorded next safe action.
5. Update the checkpoint after a node gate, fan-in, mode change, or pause.

Do not replay completed discovery merely to rebuild context. If the source of truth and actual workspace disagree, mark affected nodes `invalidated` before continuing.
