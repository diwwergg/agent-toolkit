---
name: postman-native-git
description: Author, review, scaffold, and validate Postman Native Git Collection Schema 3 YAML projects offline-first. Use for *.request.yaml, .resources/definition.yaml, .postman/resources.yaml, Postman CLI lint/run, migration from collection v2.1 JSON, or when keeping Postman requests in Git alongside application code.
---

# Postman Native Git

Work with Postman Native Git as source code. Prefer local evidence over memory, preserve repository conventions, make minimal diffs, and stay useful when the machine has no internet access.

## Operating mode

Use this precedence order for every change:

1. Existing files in the target collection and nearest sibling request.
2. Local OpenAPI/Swagger/AsyncAPI source of truth if the repo declares one.
3. This skill's `references/` snapshot.
4. Installed Postman CLI lint/run results.
5. Web research only when the local evidence conflicts, the installed CLI rejects a format you cannot explain, or the user explicitly asks for current docs.

Do not browse just to remember syntax that is already covered by this skill.

## Hard rules

- Treat Collection Schema 3 as a multi-file YAML tree; do not emit legacy `*.postman_collection.json` unless migration/export is explicitly requested.
- Author `.yaml`, not `.yml`.
- Preserve the collection's existing folder layout, naming, auth, variables, body style, script style, resource layout, and ordering convention.
- Never invent undocumented endpoints, parameters, request bodies, response fields, auth flows, or secrets.
- Never hardcode tokens, passwords, API keys, production hosts, or personal credentials.
- Do not rewrite an entire collection to normalize style. Modify only the files required for the task.
- Do not use Newman as the runner for Schema 3 Native Git collections. Prefer Postman CLI.
- Do not run cloud sync commands unless the user explicitly asks for sync/push/pull.
- Do not require internet access for ordinary authoring or structural validation.

## Start of task

From the repository root, run:

```bash
python <skill-dir>/scripts/inspect_project.py .
python <skill-dir>/scripts/validate_structure.py .
```

Read the output before editing. If a Postman CLI is installed, prefer an additional authoritative lint after local validation:

```bash
postman workspace lint --fail-severity error
```

If the repo is not a workspace root or only one collection is relevant, lint that collection instead:

```bash
postman collection lint "postman/collections/<Collection Name>"
```

CLI lint is optional for offline authoring; the Python validator must remain usable without it.

## Creating or changing a request

1. Locate the target collection and folder.
2. Read its `.resources/definition.yaml` when present.
3. Read 1-3 nearby `*.request.yaml` files, preferring the same HTTP method and auth pattern.
4. Determine whether auth/variables are inherited from the collection/folder. Do not duplicate them at request level unless siblings do.
5. If an OpenAPI source exists, verify method/path/body/parameters against it.
6. Create the request using one of these strategies:
   - safest: copy the nearest sibling and edit only fields that differ;
   - conservative fallback: use `scripts/scaffold_request.py` to create the minimal request shape.
7. Add scripts/examples only when requirements or nearby conventions justify them.
8. Run `validate_structure.py`.
9. If available, run Postman CLI lint. Fix CLI errors before finishing.
10. Show a small diff summary: files added/changed, auth/variables reused, tests/examples added, validation status.

## Minimal request fallback

When there is no trustworthy sibling, start with the smallest stable shape:

```yaml
$kind: http-request
name: Get User
url: "{{base_url}}/users/{{user_id}}"
method: GET
order: 1000
```

Then add only required headers, body, auth, scripts, or resources. Prefer copying proven local syntax for those optional fields instead of synthesizing a different representation.

## Scaffolding

Create a conservative request:

```bash
python <skill-dir>/scripts/scaffold_request.py \
  --directory "postman/collections/My API/Users" \
  --name "Get User" \
  --method GET \
  --url '{{base_url}}/users/{{user_id}}'
```

Clone a known-good local request and replace only the top-level identity fields:

```bash
python <skill-dir>/scripts/scaffold_request.py \
  --directory "postman/collections/My API/Users" \
  --name "Update User" \
  --method PATCH \
  --url '{{base_url}}/users/{{user_id}}' \
  --template "postman/collections/My API/Users/Get User.request.yaml"
```

After cloning, inspect and remove inherited body, headers, scripts, query parameters, or examples that do not apply.

## Offline validation policy

The bundled validator intentionally checks rules that can be verified safely without a full YAML parser:

- request filename extension and basic naming
- required request top-level fields
- `$kind: http-request`
- supported HTTP method spelling
- case-insensitive duplicate request names/files in a folder
- obvious legacy v2.1 collection JSON mixed into a Native Git collection
- orphan `<request>.resources` directories
- missing collection metadata hints
- likely hardcoded secret keys or bearer/API-key values
- backslash paths and common path-layout mistakes

It does **not** claim to replace Postman's schema linter. If Postman CLI is installed, its lint result is authoritative for format/schema compatibility.

## Local test/run

For a Schema 3 collection, prefer:

```bash
postman collection run "postman/collections/<Collection Name>"
```

Use an environment file when needed:

```bash
postman collection run "postman/collections/<Collection Name>" \
  -e "postman/environments/Local.environment.yaml"
```

Running requests can require network access to the target API even when collection authoring itself is offline.

## Native Git sync

Only when explicitly requested:

```bash
postman workspace lint --fail-severity error
postman workspace prepare
postman workspace push --yes
```

`prepare` is not a replacement for lint. Lint before sync.

## Migration from v2.1 JSON

If the user wants to migrate a legacy collection, prefer the installed CLI rather than hand-converting:

```bash
postman collection migrate path/to/collection.postman_collection.json
```

Then inspect the generated Native Git tree, run local validator + Postman CLI lint, and commit the generated multi-file YAML rather than maintaining two independent sources of truth.

## References to load on demand

- Layout and source-of-truth rules: `references/01-native-git-layout.md`
- Collection Schema 3 authoring: `references/02-collection-v3-authoring.md`
- Request patterns and field strategy: `references/03-request-patterns.md`
- Variables/auth/secrets: `references/04-auth-variables-secrets.md`
- Scripts/tests/examples: `references/05-scripts-tests-examples.md`
- CLI + offline workflow: `references/06-cli-offline-workflow.md`
- Monorepo and `.postman/resources.yaml`: `references/07-monorepo-manifest.md`
- v2.1 migration: `references/08-migration-v21.md`
- Troubleshooting: `references/09-troubleshooting.md`
- Agent checklist: `references/10-agent-playbook.md`
- Source provenance/version snapshot: `references/00-source-index.md`

## Completion checklist

Before reporting success:

- [ ] Endpoint details came from code/spec/user input, not invention.
- [ ] Nearby request conventions were inspected.
- [ ] No secrets or real credentials were added.
- [ ] Only necessary files changed.
- [ ] `validate_structure.py` passes or all warnings are explained.
- [ ] Postman CLI lint passes when the CLI is available.
- [ ] No cloud push occurred unless explicitly requested.
