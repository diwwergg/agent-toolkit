from __future__ import print_function

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE = os.path.join(ROOT, "tests", "fixtures", "basic")


def run(script, *args):
    cmd = [sys.executable, os.path.join(ROOT, "scripts", script)] + list(args)
    print("$ " + " ".join(cmd))
    return subprocess.call(cmd)


if __name__ == "__main__":
    if run("inspect_project.py", FIXTURE) != 0:
        sys.exit(1)
    if run("validate_structure.py", FIXTURE, "--strict") != 0:
        sys.exit(2)
    print("selftest: OK")
