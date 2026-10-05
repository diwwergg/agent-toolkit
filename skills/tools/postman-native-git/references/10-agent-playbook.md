# Agent playbook

## Add one endpoint

```text
inspect project
  ↓
locate target collection/folder
  ↓
read folder/collection definition
  ↓
read 1-3 sibling requests
  ↓
verify endpoint in code/OpenAPI
  ↓
copy sibling or scaffold minimal request
  ↓
add only required optional fields
  ↓
validate structure
  ↓
Postman CLI lint if available
  ↓
show concise diff summary
```

## Update endpoint

- edit existing request rather than recreating it;
- preserve ordering and resource directories;
- update examples/tests only when the contract changed;
- do not touch unrelated formatting.

## Generate a folder from routes

- group endpoints by existing domain/controller conventions;
- create folder metadata only if sibling folders use it;
- generate one request per endpoint;
- reuse inherited auth and `{{base_url}}`;
- validate after each small batch to localize errors.

## Review a PR

Look for:

- invented/unverified endpoints;
- hardcoded secrets/hosts;
- broken variable names;
- request-level auth duplicated unnecessarily;
- accidental legacy collection JSON;
- unrelated reordering/format churn;
- scripts with side effects or brittle assumptions;
- missing lint evidence when schema-sensitive fields changed.

## Offline escalation rule

Do not search the web unless local evidence cannot resolve the problem. When escalation is required, search only the exact failing rule/field/Postman version, update the relevant local reference note, and return to offline operation.

## Run or debug an endpoint with Postman CLI

```text
inspect project
  ↓
locate collection + request
  ↓
discover environment candidates
  ↓
select explicit/safe environment
  ↓
lint collection + environment when available
  ↓
run target request with -i and -e
  ↓
inspect status/body/tests
  ↓
fix and rerun same request
  ↓
optionally run parent folder / full collection
```

Rules:

- use `-e` / `--environment` for environment path or UID;
- use `-i` for a request/folder name, path, or UID;
- repeat `-i` for ordered dependencies;
- prefer the smallest relevant run scope;
- do not guess between multiple environments;
- never run against production unless the user explicitly requests it;
- treat a non-zero CLI exit code as failure.
