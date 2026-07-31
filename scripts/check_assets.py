#!/usr/bin/env python3
"""Comprueba assets referenciados, huérfanos y coincidencia exacta de rutas."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
IMAGE = re.compile(r"!\[[^\]]*\]\((/assets/[^)\s]+)|<img\s+[^>]*src=[\"'](/assets/[^\"']+)", re.I)


def main() -> int:
    available = {item.relative_to(ROOT).as_posix() for item in ASSETS.rglob("*") if item.is_file()}
    used: set[str] = set()
    errors = 0
    pages = [ROOT / "simgest.md", *sorted((ROOT / "simgest").rglob("*.md"))]
    for path in pages:
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for match in IMAGE.findall(line):
                target = next(value for value in match if value)
                key = target.lstrip("/").split("?", 1)[0].split("#", 1)[0]
                if key not in available:
                    print(f"{path.relative_to(ROOT)}:{number}: imagen inexistente o con mayúsculas incorrectas: {target}")
                    errors += 1
                else:
                    used.add(key)
    for orphan in sorted(available - used):
        print(f"{orphan}: asset huérfano")
        errors += 1
    print("check_assets: " + ("OK" if not errors else f"{errors} error(es)"))
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())
