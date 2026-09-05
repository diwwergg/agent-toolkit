# Execution artifacts

Read this reference when work spans turns, agents, modes, or checkpoints.

## Recommended bundle

```text
artifacts/graph-engineering/<work-id>/
├── 00-context.md
├── 01-graph.md
├── 02-evidence.md
├── 03-plan.md
├── 04-log.md
├── 05-unresolved.md
├── handoffs/
│   └── <handoff-id>.md
└── checkpoint.json
```

Use the project's established artifact directory when one exists. Keep these files out of production source unless the user asks to commit them. Do not put secrets, credentials, or private source contents into a shared artifact merely to improve traceability.

## Checkpoint contents

```json
{
  "work_id": "stable-human-readable-id",
  "mode": "PLAN|CODE|DEBUG|REFACTOR|REVIEW",
  "status": "active|blocked|complete|needs-review",
  "last_completed_gate": "boundary|graph|evidence|impact|implementation|handoff|review",
  "current_frontier": ["node-or-task-id"],
  "graph_version": "vN",
  "artifact_paths": [],
  "unresolved_ids": [],
  "stale_edges": [],
  "next_safe_action": "...",
  "updated_at": "ISO-8601 timestamp"
}
```

The checkpoint is a resume pointer, not a substitute for the Markdown records. Update it after a meaningful gate, mode transition, specialist return, or pause.

## Handoff artifact

Each handoff should link to the graph version and contain the delegation contract from `SKILL.md`, the exact scope, prior evidence ids, expected output, validation requested, stop condition, and returned result. A handoff is complete only when the result is written back to the graph and unresolved queue.

## Resume procedure

1. Load the checkpoint and read the referenced context, graph, log, and unresolved queue.
2. Confirm the workspace and relevant sources have not changed.
3. Revalidate stale or high-impact edges only.
4. Resume at the current frontier; do not replay completed discovery.
5. Update the checkpoint before handing off again.

## Completion and archival

Mark status complete only after the required gate passes and the next action is either unnecessary or explicitly handed off. Preserve the final graph and evidence for the user's requested retention period, then archive or remove artifacts only under the user's project conventions.
