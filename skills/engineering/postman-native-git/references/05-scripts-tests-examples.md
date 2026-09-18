# Scripts, tests, and examples

## Principle

Tests and examples are executable/behavioral documentation. Add them when their expected behavior is known from implementation, specification, existing tests, or explicit user requirements.

Do not invent success/error schemas merely to make a collection look complete.

## Post-response tests

Use existing request scripts as the style source. Typical assertions cover:

- expected status code;
- content type;
- required response fields;
- response type/shape;
- business invariant known from the API contract;
- variable capture for a documented workflow.

Keep assertions deterministic. Avoid tests that depend on wall-clock timing or external mutable state unless the API contract requires it.

## Pre-request scripts

Use them for deterministic preparation such as:

- generating unique test data;
- timestamps/nonces required by the API;
- deriving signatures when the collection already uses that approach.

Do not fetch documentation or credentials from the internet in pre-request scripts.

## Examples

Schema 3 can place request-specific examples under the request's `.resources` tree. Follow a sibling example file as the authoritative syntax.

Good examples:

- one normal 2xx response;
- one relevant validation/auth/not-found response when documented;
- sanitized values with no real customer/user data.

## Offline behavior

Creating and validating script/resource structure is offline-capable. Executing a request/test obviously requires the target API to be reachable unless the repo uses a local mock/server.
