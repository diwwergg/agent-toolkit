from __future__ import print_function

import os
import re

REQUEST_SUFFIX = ".request.yaml"
VALID_METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"}


def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_text(path, content):
    parent = os.path.dirname(path)
    if parent and not os.path.isdir(parent):
        os.makedirs(parent)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def iter_files(root):
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules", ".venv", "venv", "dist", "build", "__pycache__"}]
        for name in files:
            yield os.path.join(base, name)


def request_files(root):
    return [p for p in iter_files(root) if p.endswith(REQUEST_SUFFIX)]


def top_level_scalar(text, key):
    pattern = re.compile(r"^" + re.escape(key) + r"\s*:\s*(.*?)\s*$", re.MULTILINE)
    m = pattern.search(text)
    if not m:
        return None
    value = m.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("\"", "'"):
        value = value[1:-1]
    return value


def replace_top_level_scalar(text, key, value, quote=False):
    rendered = ('"' + value.replace('"', '\\"') + '"') if quote else value
    pattern = re.compile(r"^(" + re.escape(key) + r"\s*:\s*).*$", re.MULTILINE)
    if pattern.search(text):
        return pattern.sub(lambda m: m.group(1) + rendered, text, count=1)
    if not text.endswith("\n"):
        text += "\n"
    return text + key + ": " + rendered + "\n"


def slug_filename(name):
    # Preserve human-readable Native Git filenames while removing path-invalid chars.
    safe = re.sub(r"[\\/:*?\"<>|]+", "-", name).strip().rstrip(".")
    safe = re.sub(r"\s+", " ", safe)
    return safe or "Request"


def rel(path, root):
    return os.path.relpath(path, root).replace(os.sep, "/")
