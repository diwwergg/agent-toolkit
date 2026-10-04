# Monorepos and `.postman/resources.yaml`

## Default discovery

Postman discovers elements under the repository's default `postman/` directories. `.postman/resources.yaml` also connects local paths to workspace/cloud metadata.

## Monorepo pattern

For a repository with multiple services, keep one top-level manifest and register service-specific Postman elements through `localResources`.

Conceptual layout:

```text
repo/
├── .postman/
│   └── resources.yaml
└── services/
    ├── service-a/
    │   └── postman/
    │       ├── collections/
    │       └── environments/
    └── service-b/
        └── postman/
            ├── collections/
            └── environments/
```

Representative manifest fragment:

```yaml
localResources:
  collections:
    - ../services/service-a/postman/collections/Service A API
    - ../services/service-b/postman/collections/Service B API
  environments:
    - ../services/service-a/postman/environments/Service A Staging.environment.yaml
```

Paths are relative to the `.postman/` directory.

## Safety

Do not invent `workspace.id` or `cloudResources` IDs. Those values tie local elements to cloud entities and should come from Postman setup/pull/prepare workflows.

Do not delete manifest entries because a service is absent from the current task; force-sync semantics can make absence meaningful.

## Agent rule

Before editing a monorepo, run `inspect_project.py` from the repository root so the agent sees all collection roots and the manifest location before selecting the target service.
