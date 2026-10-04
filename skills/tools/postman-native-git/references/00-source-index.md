# Source index and snapshot policy

Snapshot date: **2026-09-18**

This skill is intentionally self-contained for offline use. The files in `references/` paraphrase the stable operational rules needed for day-to-day Native Git authoring. They are not a verbatim mirror of Postman documentation.

## Primary sources used for this snapshot

1. Postman Docs — Collections schemas
   - https://learning.postman.com/docs/use/use-collections/collections-schemas
   - Stable points captured: Collection Schema 3.0.0, multi-file YAML, `*.request.yaml`, request resource directories, `.yaml` authoring, fractional numeric ordering, Postman CLI for v3.

2. Postman Docs — Set up Native Git
   - https://learning.postman.com/docs/use/native-git/setup
   - Stable points captured: `postman/`, `.postman/resources.yaml`, default discovery, monorepo `localResources`, paths relative to `.postman/`, workspace prepare/push behavior.

3. Postman Docs — Develop locally with Native Git
   - https://learning.postman.com/docs/use/native-git/develop-locally
   - Stable points captured: Local View is editable source, Git-first branch workflow, collection v3 YAML committed with code.

4. Postman Docs — Postman CLI collection commands
   - https://learning.postman.com/docs/postman-cli/postman-cli-collections
   - Stable points captured: `collection run`, `collection migrate`, `collection lint`.

5. Postman Docs — Workspace commands
   - https://learning.postman.com/docs/postman-cli/postman-cli-workspace
   - Stable points captured: `workspace lint`, `prepare`, `push` responsibilities.

6. Postman Docs — Init command
   - https://learning.postman.com/latest-v-12/docs/postman-cli/postman-cli-init
   - Stable points captured: `postman init`, `--no-cloud`, `--dry-run`, `--json`, generated Native Git project, agent skill installation behavior.

7. Postman Docs — Environments / variables / collaboration
   - https://learning.postman.com/docs/use/send-requests/variables/managing-environments
   - https://learning.postman.com/docs/use/native-git/collaborate
   - Stable points captured: keep secrets/local values out of Git; shared values are deliberate.

8. Agent Skills specification
   - https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
   - Stable points captured: `SKILL.md` plus optional `scripts/`, `references/`, and `assets/` structure.

## Secondary implementation evidence

Public Native Git repositories and issue reports were used only to understand real generated layouts and known edge cases. They are not treated as normative when they conflict with Postman CLI lint.

Known 2026 edge case captured in this snapshot: a Postman v12.6.2 issue reported a linter conflict around a generated top-level `queryParams` shape. This is why this skill uses the rule **copy a known-good sibling first, then let the installed CLI lint decide** instead of hardcoding every optional field representation.

## When to refresh this snapshot

Refresh web research only if one of these occurs:

- installed Postman CLI rejects a structure that used to lint successfully;
- `postman --version` has moved to a major version whose release notes say the Native Git format changed;
- Postman changes the current collection schema version from 3.0.0;
- a new protocol/resource type is needed and no local sibling demonstrates its format;
- the user explicitly requests current documentation verification.

For ordinary GET/POST/PUT/PATCH/DELETE HTTP authoring in an existing Native Git repository, this local snapshot should be sufficient.
