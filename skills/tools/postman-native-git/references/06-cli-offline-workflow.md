# Postman CLI and offline workflow

## What works offline

Assuming the Postman CLI is already installed, these operations are local in nature and should be preferred before any cloud operation:

```bash
postman --version
postman collection lint "postman/collections/My API"
postman environment lint "postman/environments"
postman workspace lint --fail-severity error
```

Collection execution can be local as a runner, but the requests still need network access to whatever API URL they target.

## Native Git runner

For Collection Schema 3:

```bash
postman collection run "postman/collections/My API"
```

Do not use Newman as the primary runner for Schema 3.

## Migration

Use:

```bash
postman collection migrate legacy.postman_collection.json
```

Prefer CLI migration to handcrafted conversion.

## Init caveat

`postman init` is useful for bootstrapping an AI-ready project and supports `--no-cloud`, `--dry-run`, and `--json`. However, current init behavior also installs/fetches Postman agent skills. Therefore this custom skill does not depend on `postman init` for offline day-to-day work.

For an existing Native Git repository, do not rerun init merely to author a request.

## Cloud-only / network-dependent actions

Treat these as explicit operations, not routine validation:

- login;
- creating/linking cloud workspaces;
- pulling/pushing workspace content;
- refreshing Postman-provided agent skills;
- cloud mocks/monitors/docs operations.

## Validation order

```text
Bundled Python checks
        ↓
Postman CLI collection/workspace lint (if installed)
        ↓
Optional collection run against local/dev API
        ↓
Git diff review
        ↓
Cloud sync only when requested
```
