# Collection Schema 3 authoring

## Stable facts

- Current Postman collections use schema 3.0.0.
- Schema 3 is a directory tree rather than one monolithic collection JSON file.
- The format is designed for source control, human review, automation, and AI editing.
- Requests are separate YAML files.
- Examples and scripts can live as request resources.
- Folder/collection metadata can be represented with `definition.yaml` files.
- Numeric order values control display/run ordering.

## Authoring principle

Schema 3 intentionally makes small edits cheap. Use that property:

- one endpoint change should normally touch one request file and perhaps its own resources;
- one folder description change should touch only that folder metadata;
- adding tests should not cause unrelated request rewrites;
- preserve stable key ordering already used by nearby files to keep Git diffs small.

## Conservative minimum request

```yaml
$kind: http-request
name: Get User
url: "{{base_url}}/users/{{user_id}}"
method: GET
order: 1000
```

This is the safest fallback when there is no sibling request to copy.

## Optional fields are convention-sensitive

Headers, query parameters, bodies, auth, scripts, examples, and newer protocol-specific properties can have representation details that evolve. Before writing them:

1. find a local request using the same feature;
2. copy its representation;
3. change only values relevant to the endpoint;
4. run CLI lint if available.

This avoids teaching the agent a stale optional-field grammar.

## Legacy coexistence

A repository can contain old v2.1 JSON during migration, but do not silently maintain both v2.1 and v3 as equal sources. Choose one source of truth and document the conversion direction.
