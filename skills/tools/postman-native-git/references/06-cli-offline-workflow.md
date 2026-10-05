# Postman CLI and offline workflow

## What works offline

Assuming the Postman CLI is already installed, these operations are local in nature and should be preferred before any cloud operation:

```bash
postman --version
postman collection lint "postman/collections/My API"
postman environment lint "postman/environments/Local.environment.yaml"
postman workspace lint --fail-severity error
```

Collection execution can be local as a runner, but the requests still need network access to whatever API URL they target.

## Native Git runner

For Collection Schema 3, use Postman CLI rather than Newman:

```bash
postman collection run "postman/collections/My API"
```

### Environment selection

Postman CLI accepts either a local environment file path or an environment UID:

```bash
postman collection run "postman/collections/My API" \
  -e "postman/environments/Local.environment.yaml"
```

Equivalent long form:

```bash
postman collection run "postman/collections/My API" \
  --environment "postman/environments/Local.environment.yaml"
```

Selection policy for agents:

1. Honor an environment explicitly named by the user.
2. Otherwise reuse an environment already established by repository/task context.
3. A single unambiguous local/dev environment may be selected automatically.
4. If multiple environments are plausible, surface the candidates instead of guessing.
5. Never implicitly select production.

Use `--env-var key=value` for temporary non-secret overrides when changing the environment file is unnecessary. The option may be repeated.

### Run one request or folder

Use `-i` with a request UID, folder UID, request name, folder name, or supported relative folder path:

```bash
postman collection run "postman/collections/My API" \
  -e "postman/environments/Local.environment.yaml" \
  -i "Users/Get User"
```

If names are duplicated, prefer the UID or a folder-qualified path.

### Run multiple items in order

Repeat `-i` to create an explicit run order:

```bash
postman collection run "postman/collections/My API" \
  -e "postman/environments/Local.environment.yaml" \
  -i "Auth/Login" \
  -i "Users/Get User" \
  -i "Users/Update User"
```

This is useful when a target request depends on an authentication/setup request. Do not add prerequisite requests unless the collection's actual flow requires them.

### Scope strategy

Prefer the smallest useful execution scope:

```text
one changed endpoint → one request
related endpoint group → one folder
regression / release confidence → whole collection
```

After a focused run passes, widen the scope only when the task requires regression confidence.

## Migration

Use:

```bash
postman collection migrate legacy.postman_collection.json
```

Prefer CLI migration to handcrafted conversion.

## Init caveat

`postman init` is useful for bootstrapping an AI-ready project and supports `--no-cloud`, `--dry-run`, and `--json`. However, init can also fetch/install Postman-provided agent skills. Therefore this custom skill does not depend on `postman init` for offline day-to-day work.

For an existing Native Git repository, do not rerun init merely to author or run a request.

## Cloud-only / network-dependent actions

Treat these as explicit operations, not routine validation:

- login;
- creating/linking cloud workspaces;
- pulling/pushing workspace content;
- refreshing Postman-provided agent skills;
- cloud mocks/monitors/docs operations.

## Validation and execution order

```text
Bundled Python checks
        ↓
Postman CLI collection/environment/workspace lint (if installed)
        ↓
Select environment
        ↓
Run smallest relevant request/folder
        ↓
Optionally widen to collection regression run
        ↓
Git diff review
        ↓
Cloud sync only when requested
```
