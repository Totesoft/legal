#!/usr/bin/env python3
"""Fail when draft placeholders or unpublished legal pages remain."""

from __future__ import annotations

import re
import sys
from pathlib import Path

TOKEN = re.compile(r"\{\{[A-Z0-9_]+\}\}")
SKIP_DIRS = {".git", "_site", "vendor", "node_modules"}


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    failures: list[str] = []

    for path in sorted(root.rglob("*")):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in {".md", ".yml", ".yaml", ".html", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        tokens = sorted(set(TOKEN.findall(text)))
        if tokens:
            failures.append(f"{path.relative_to(root)}: placeholders: {', '.join(tokens)}")
        if path.suffix.lower() == ".md" and re.search(r"(?m)^published:\s*false\s*$", text):
            failures.append(f"{path.relative_to(root)}: still contains published: false in front matter")

    if failures:
        print("Legal publication check failed:")
        for item in failures:
            print(f"- {item}")
        return 1

    print("Legal publication check passed: no placeholders or unpublished pages found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
