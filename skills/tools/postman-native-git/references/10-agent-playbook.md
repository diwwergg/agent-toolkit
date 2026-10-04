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
