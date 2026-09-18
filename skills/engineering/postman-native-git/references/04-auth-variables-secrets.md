# Auth, variables, and secrets

## Security rule

Git should contain variable references and non-sensitive shared defaults, not real secrets.

Examples of safe references:

```text
{{base_url}}
{{access_token}}
{{api_key}}
{{user_id}}
```

Examples that should trigger review:

- long bearer token literals;
- JWT-looking values;
- API keys embedded in headers/query parameters;
- passwords/client secrets in YAML;
- production hostnames copied as permanent defaults when an environment variable already exists.

## Inheritance first

Before adding request-level auth:

1. inspect collection metadata;
2. inspect folder metadata;
3. inspect two sibling requests;
4. add explicit request auth only when this endpoint differs.

This reduces duplication and prevents credential drift.

## Environment values

Postman supports local and shared variable behavior. For Git workflows:

- store reusable non-secret names/defaults in committed files as appropriate;
- keep sensitive local values private;
- use vault/secret mechanisms where the team's Postman setup supports them;
- never convert a private/local credential into a shared Git value automatically.

## Validator behavior

`validate_structure.py` performs heuristic secret scanning. It is intentionally conservative and can produce warnings. A warning means inspect the value; it does not prove credential leakage.
