# Offline helper scripts

All scripts use only the Python standard library and are written to remain compatible with Python 3.7+.

## inspect_project.py

Discover Native Git collections, requests, definitions, environments, legacy v2.1 files, manifest, and Postman CLI availability.

```bash
python inspect_project.py /path/to/repo
python inspect_project.py /path/to/repo --json
```

## validate_structure.py

Run conservative local checks without PyYAML or network access.

```bash
python validate_structure.py /path/to/repo
python validate_structure.py /path/to/repo --strict
```

## scaffold_request.py

Create a minimal request or clone a known-good sibling.

```bash
python scaffold_request.py --directory postman/collections/API/Users \
  --name "Get User" --method GET --url '{{base_url}}/users/{{user_id}}'
```

## doctor.py

Run inspection + offline validation + Postman CLI lint when installed.

```bash
python doctor.py /path/to/repo
python doctor.py /path/to/repo --no-cli
```
