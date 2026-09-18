from __future__ import print_function

import argparse
import os
import sys

from _common import VALID_METHODS, read_text, replace_top_level_scalar, slug_filename, write_text


def main():
    ap = argparse.ArgumentParser(description="Create a conservative Postman Native Git HTTP request without external dependencies.")
    ap.add_argument("--directory", required=True, help="Target collection/folder directory")
    ap.add_argument("--name", required=True)
    ap.add_argument("--method", required=True)
    ap.add_argument("--url", required=True)
    ap.add_argument("--order", default="1000")
    ap.add_argument("--template", help="Optional known-good sibling *.request.yaml to clone")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    method = args.method.upper()
    if method not in VALID_METHODS:
        print("error: unsupported HTTP method %s" % args.method, file=sys.stderr)
        return 2

    target_dir = os.path.abspath(args.directory)
    filename = slug_filename(args.name) + ".request.yaml"
    target = os.path.join(target_dir, filename)

    if os.path.exists(target) and not args.force:
        print("error: target exists: %s (use --force to overwrite)" % target, file=sys.stderr)
        return 3

    if args.template:
        text = read_text(args.template)
        text = replace_top_level_scalar(text, "$kind", "http-request")
        text = replace_top_level_scalar(text, "name", args.name)
        text = replace_top_level_scalar(text, "url", args.url, quote=True)
        text = replace_top_level_scalar(text, "method", method)
        if args.order:
            text = replace_top_level_scalar(text, "order", str(args.order))
    else:
        text = (
            "$kind: http-request\n"
            "name: %s\n"
            "url: \"%s\"\n"
            "method: %s\n"
            "order: %s\n"
        ) % (args.name, args.url.replace('"', '\\"'), method, args.order)

    write_text(target, text)
    print(target)
    if args.template:
        print("note: cloned a sibling template; inspect and remove inherited fields/resources that do not apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
