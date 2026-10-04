# Migration from Collection v2.1 JSON

## Preferred path

Use the Postman CLI migration command when available:

```bash
postman collection migrate path/to/My.postman_collection.json
```

Then lint the generated collection and inspect the Git diff.

## Why not hand-convert by default

Collection v2.1 stores nested requests, auth, scripts, examples, and variables in one JSON document. Schema 3 distributes them across files/resources. Manual conversion is easy to get subtly wrong and creates noisy diffs.

## Migration checklist

- [ ] Preserve collection/folder/request names.
- [ ] Preserve auth inheritance.
- [ ] Preserve variables without exposing secrets.
- [ ] Preserve request method/path/body/headers.
- [ ] Preserve pre-request and post-response scripts.
- [ ] Preserve documented examples.
- [ ] Check ordering.
- [ ] Run `validate_structure.py`.
- [ ] Run `postman collection lint` when available.
- [ ] Run representative requests/tests.
- [ ] Decide which format is authoritative; avoid maintaining divergent v2.1 and v3 copies.

## Newman

Newman remains useful for exported/legacy v2.1 collections. Do not assume it can execute the Native Git Schema 3 tree directly.
