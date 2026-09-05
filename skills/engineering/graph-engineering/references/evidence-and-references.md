# Evidence and references

Read this reference whenever the graph depends on external research, repository facts, test output, specialist results, or claims that may become stale.

## Evidence ledger

Store one record per material claim:

```text
claim:
source/artifact:
location:
observed-at:
fresh-until:
supports:
confidence:
owner:
contradictions:
```

Acceptable evidence includes source material, repository inspection, reproducible commands, test results, runtime observations, explicit user constraints, and a named specialist artifact. Label inference separately from observation. A plan may use a low-confidence claim, but it must show the validation needed before a high-impact action.

## Avoiding repeated discovery

Give each source or node a stable reference id. When a downstream task needs the same fact, pass the id and its relevant excerpt/summary instead of reopening and reinterpreting the entire source. Refresh only when the source is stale, changed, contradicted, or insufficient for the new decision.

## Specialist results

Record the specialist's scope, conclusion, evidence, limitations, and recommended next gate. Do not collapse a specialist result into an unsupported boolean such as `safe: true`; preserve uncertainty and conditions.

## Conflicts and freshness

When evidence conflicts:

1. keep both claims;
2. identify the exact contradiction;
3. prefer the more authoritative and current source for provisional planning;
4. create a resolution item owned by the relevant specialist;
5. block irreversible work if the contradiction changes the risk-bearing path.

When evidence is stale, mark affected edges stale and revalidate only those edges that could change the decision. Dates are useful, but behavior changes and version identifiers are stronger freshness signals.

## Reference hygiene

Use precise paths, symbols, test names, URLs, document sections, commit identifiers, or artifact ids. Never cite a generic “looked at the code” statement as evidence. Keep source material read-only unless the user explicitly asks for an edit.
