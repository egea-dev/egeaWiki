#!/usr/bin/env python3
"""Comprueba enlaces Markdown internos y muestra archivo y línea."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")


def route_exists(route: str) -> bool:
    route = route.split("#", 1)[0].split("?", 1)[0]
    if not route:
        return True
    if route.startswith("/assets/"):
        return (ROOT / route.lstrip("/")).is_file()
    if not route.startswith("/simgest"):
        return False
    relative = route.lstrip("/")
    candidates = (ROOT / f"{relative}.md", ROOT / relative / "index.md")
    if route == "/simgest":
        candidates = (ROOT / "simgest" / "index.md",)
    return any(candidate.is_file() for candidate in candidates)


def main() -> int:
    errors = 0
    for path in sorted((ROOT / "simgest").rglob("*.md")):
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for target in LINK.findall(line):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                if target.startswith("/") and not route_exists(target):
                    print(f"{path.relative_to(ROOT)}:{number}: enlace interno inexistente: {target}")
                    errors += 1
                elif not target.startswith("/"):
                    print(f"{path.relative_to(ROOT)}:{number}: enlace relativo ambiguo: {target}")
                    errors += 1
    print("check_links: " + ("OK" if not errors else f"{errors} error(es)"))
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())
