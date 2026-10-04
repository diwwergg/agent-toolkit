from __future__ import print_function

import argparse
import os
import shutil
import subprocess
import sys


def run(cmd, cwd):
    print("\n$ " + " ".join(cmd))
    try:
        p = subprocess.Popen(cmd, cwd=cwd)
        return p.wait()
    except OSError as e:
        print("failed: %s" % e)
        return 127


def main():
    ap = argparse.ArgumentParser(description="Run offline checks and optional Postman CLI lint.")
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--no-cli", action="store_true", help="Skip Postman CLI even if installed")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    here = os.path.dirname(os.path.abspath(__file__))

    code = run([sys.executable, os.path.join(here, "inspect_project.py"), root], root)
    if code != 0:
        return code

    validate = [sys.executable, os.path.join(here, "validate_structure.py"), root]
    if args.strict:
        validate.append("--strict")
    code = run(validate, root)
    if code != 0:
        return code

    if args.no_cli:
        print("\nPostman CLI lint skipped (--no-cli).")
        return 0

    postman = shutil.which("postman")
    if not postman:
        print("\nPostman CLI not found. Offline structural checks passed; run authoritative lint later when CLI is available.")
        return 0

    manifest = os.path.join(root, ".postman", "resources.yaml")
    if os.path.isfile(manifest):
        return run([postman, "workspace", "lint", "--fail-severity", "error"], root)

    collections = os.path.join(root, "postman", "collections")
    if os.path.isdir(collections):
        return run([postman, "collection", "lint", collections], root)

    print("\nPostman CLI found, but no workspace manifest/default collections directory was detected. Run collection lint manually on the target collection.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
