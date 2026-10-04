from __future__ import print_function

import argparse
import os
import re
import sys

from _common import VALID_METHODS, iter_files, read_text, rel, request_files, top_level_scalar

SECRET_KEY_RE = re.compile(r"(?i)(authorization|api[-_ ]?key|access[-_ ]?token|client[-_ ]?secret|password)\s*:")
JWT_RE = re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b")
BEARER_LITERAL_RE = re.compile(r"(?i)bearer\s+[A-Za-z0-9._~+/-]{16,}")
VAR_RE = re.compile(r"{{[^{}]+}}")


def issue(level, code, path, message):
    return (level, code, path, message)


def main():
    ap = argparse.ArgumentParser(description="Offline structural validator for Postman Native Git projects.")
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--strict", action="store_true", help="Treat warnings as failure.")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    issues = []
    reqs = request_files(root)

    # Case-insensitive collisions in each directory.
    by_dir = {}
    for p in reqs:
        by_dir.setdefault(os.path.dirname(p), []).append(p)
    for d, files in by_dir.items():
        seen = {}
        for p in files:
            key = os.path.basename(p).lower()
            if key in seen:
                issues.append(issue("ERROR", "NAME001", rel(p, root), "case-insensitive duplicate of %s" % rel(seen[key], root)))
            else:
                seen[key] = p

    for p in reqs:
        r = rel(p, root)
        text = read_text(p)
        kind = top_level_scalar(text, "$kind")
        name = top_level_scalar(text, "name")
        url = top_level_scalar(text, "url")
        method = top_level_scalar(text, "method")

        if kind != "http-request":
            issues.append(issue("ERROR", "REQ001", r, "expected top-level '$kind: http-request'"))
        if not name:
            issues.append(issue("ERROR", "REQ002", r, "missing top-level name"))
        if not url:
            issues.append(issue("ERROR", "REQ003", r, "missing top-level url"))
        if not method:
            issues.append(issue("ERROR", "REQ004", r, "missing top-level method"))
        elif method.upper() not in VALID_METHODS:
            issues.append(issue("ERROR", "REQ005", r, "unsupported/unknown HTTP method '%s'" % method))
        elif method != method.upper():
            issues.append(issue("WARN", "REQ006", r, "HTTP method should match local uppercase convention"))

        if "\\" in text:
            issues.append(issue("WARN", "PATH001", r, "contains backslashes; Native Git paths should use forward slashes"))

        # Heuristic secret detection, ignoring variable references.
        scrubbed = VAR_RE.sub("{{VAR}}", text)
        if JWT_RE.search(scrubbed):
            issues.append(issue("WARN", "SEC001", r, "contains a JWT-looking literal; verify no real token is committed"))
        if BEARER_LITERAL_RE.search(scrubbed):
            issues.append(issue("WARN", "SEC002", r, "contains a bearer-token-looking literal; prefer a variable"))
        if SECRET_KEY_RE.search(scrubbed):
            for line in scrubbed.splitlines():
                if SECRET_KEY_RE.search(line):
                    value = line.split(":", 1)[1].strip() if ":" in line else ""
                    if value and value not in ("", "null", "~", "{{VAR}}") and len(value) >= 12:
                        issues.append(issue("WARN", "SEC003", r, "possible credential literal near '%s'" % line[:80].strip()))
                        break

    # Orphan request resource directories.
    for base, dirs, files in os.walk(root):
        for d in list(dirs):
            if d.endswith(".resources") and d != ".resources":
                stem = d[:-len(".resources")]
                sibling = os.path.join(base, stem + ".request.yaml")
                if not os.path.isfile(sibling):
                    issues.append(issue("WARN", "RES001", rel(os.path.join(base, d), root), "request resource directory has no sibling %s.request.yaml" % stem))

    # Legacy collection JSON mixed with v3 tree.
    legacy = []
    yml_authoring = []
    for p in iter_files(root):
        r = rel(p, root)
        if r.endswith(".postman_collection.json"):
            legacy.append(r)
        if r.endswith(".request.yml") or r.endswith(".environment.yml"):
            yml_authoring.append(r)
    if legacy and reqs:
        for r in legacy:
            issues.append(issue("WARN", "MIG001", r, "legacy v2.1 collection JSON coexists with Native Git request files; verify one source of truth"))
    for r in yml_authoring:
        issues.append(issue("WARN", "FMT001", r, "author new Native Git files with .yaml rather than .yml"))

    # Collection metadata hint: only warn when a top-level collection root can be inferred.
    collection_roots = set()
    for p in reqs:
        parts = rel(p, root).split("/")
        if "collections" in parts:
            i = parts.index("collections")
            if i + 1 < len(parts):
                collection_roots.add(os.path.join(root, *parts[: i + 2]))
    for croot in sorted(collection_roots):
        definition = os.path.join(croot, ".resources", "definition.yaml")
        if not os.path.isfile(definition):
            issues.append(issue("WARN", "COL001", rel(croot, root), "no .resources/definition.yaml found; compare with a working collection generated by your Postman version"))

    errors = [x for x in issues if x[0] == "ERROR"]
    warnings = [x for x in issues if x[0] == "WARN"]

    if not issues:
        print("OK: no structural issues found (%d request files checked)." % len(reqs))
        return 0

    for level, code, path, message in issues:
        print("%s %-7s %s: %s" % (level, code, path, message))
    print("\nSummary: %d error(s), %d warning(s), %d request(s) checked." % (len(errors), len(warnings), len(reqs)))
    print("Note: this is an offline structural check, not a replacement for `postman collection lint`/`postman workspace lint`.")

    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
