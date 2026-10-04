from __future__ import print_function

import argparse
import json
import os
import shutil
import sys

from _common import request_files, read_text, rel, top_level_scalar, iter_files


def main():
    ap = argparse.ArgumentParser(description="Inspect a Postman Native Git repository without network access.")
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    reqs = request_files(root)
    collections = set()
    methods = {}
    kinds = {}

    for p in reqs:
        text = read_text(p)
        method = (top_level_scalar(text, "method") or "?").upper()
        kind = top_level_scalar(text, "$kind") or "?"
        methods[method] = methods.get(method, 0) + 1
        kinds[kind] = kinds.get(kind, 0) + 1
        parts = rel(p, root).split("/")
        if "collections" in parts:
            i = parts.index("collections")
            if i + 1 < len(parts):
                collections.add("/".join(parts[: i + 2]))

    defs = []
    envs = []
    legacy = []
    for p in iter_files(root):
        r = rel(p, root)
        if os.path.basename(p) == "definition.yaml" and ".resources" in r.split("/"):
            defs.append(r)
        if r.endswith(".environment.yaml"):
            envs.append(r)
        if r.endswith(".postman_collection.json"):
            legacy.append(r)

    manifest = os.path.join(root, ".postman", "resources.yaml")
    cli = shutil.which("postman")

    data = {
        "root": root,
        "manifest": rel(manifest, root) if os.path.isfile(manifest) else None,
        "postman_cli": cli,
        "collections": sorted(collections),
        "request_count": len(reqs),
        "request_methods": dict(sorted(methods.items())),
        "request_kinds": dict(sorted(kinds.items())),
        "definition_files": sorted(defs),
        "environment_files": sorted(envs),
        "legacy_v21_collections": sorted(legacy),
    }

    if args.as_json:
        print(json.dumps(data, indent=2, sort_keys=True))
        return 0

    print("Postman Native Git inspection")
    print("root:            %s" % root)
    print("manifest:        %s" % (data["manifest"] or "not found"))
    print("postman CLI:     %s" % (cli or "not found"))
    print("collections:     %d" % len(collections))
    for c in sorted(collections):
        print("  - %s" % c)
    print("requests:        %d" % len(reqs))
    if methods:
        print("methods:         %s" % ", ".join("%s=%d" % item for item in sorted(methods.items())))
    print("definitions:     %d" % len(defs))
    print("environments:    %d" % len(envs))
    print("legacy v2.1:     %d" % len(legacy))

    if not reqs:
        print("\nHint: no *.request.yaml files were found.")
    if legacy and reqs:
        print("\nNote: legacy v2.1 JSON and Native Git v3 files coexist; verify the source of truth.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
