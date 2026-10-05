# postman-native-git

Offline-first Agent Skill for Postman Native Git / Collection Schema 3 YAML repositories.

## Install manually

Copy this directory to your agent's skill directory, for example:

```text
.agents/skills/postman-native-git/
```

The skill itself is tool-agnostic and follows the Agent Skills directory convention (`SKILL.md`, `references/`, `scripts/`, `assets/`).

## Design goals

- Git-friendly, minimal diffs
- Native Git Schema 3 first
- Works offline for authoring/structure checks
- No PyYAML or pip dependencies
- Python 3.7+ helper scripts
- Existing repository conventions override generic examples
- Postman CLI lint is authoritative when available
- Postman CLI request/folder execution with `-i`
- Selectable local/cloud environments with `-e` / `--environment`
- Safe execution policy: smallest relevant scope, never implicit production
- Web research is a last resort, not a routine dependency

Run a quick health check:

```bash
python scripts/doctor.py /path/to/repo --no-cli
```
