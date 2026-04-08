from __future__ import annotations

import argparse
import json
from importlib import metadata

PACKAGE_NAME = "pdf-form-tools"
MODULE_NAME = "pdf_form_tools"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog=PACKAGE_NAME)
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("version", help="Print installed package version")
    subparsers.add_parser("info", help="Print package metadata as JSON")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command in (None, "version"):
        print(metadata.version(PACKAGE_NAME))
        return 0

    if args.command == "info":
        payload = {
            "package": PACKAGE_NAME,
            "version": metadata.version(PACKAGE_NAME),
            "module": MODULE_NAME,
        }
        print(json.dumps(payload, ensure_ascii=True, indent=2))
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
