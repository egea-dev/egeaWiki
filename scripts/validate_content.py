#!/usr/bin/env python3
"""Validación estática del Markdown publicado bajo simgest/."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "simgest"
BANNED = ("sandbox:", "/mnt/data", "file://")


def issue(path: Path, line: int, message: str) -> None:
    print(f"{path.relative_to(ROOT)}:{line}: {message}")


def main() -> int:
    errors = 0
    # Wiki.js Git importa el repositorio completo y no admite limitarlo a una
    # subcarpeta. Solo el manual puede conservar extensión Markdown.
    for path in sorted(ROOT.rglob("*.md")):
        if path == ROOT / "PROMPT_CODEX_EGEAWIKI.md" or PAGES in path.parents:
            continue
        issue(path, 1, "Markdown fuera de simgest/ se importaría como página de Wiki.js")
        errors += 1
    for path in sorted(PAGES.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            issue(path, exc.start + 1, "el archivo no es UTF-8")
            errors += 1
            continue
        lines = text.splitlines()
        if len(lines) < 3 or lines[0] != "---" or "---" not in lines[1:]:
            issue(path, 1, "falta front matter YAML")
            errors += 1
        fenced = False
        h1 = 0
        previous_level = 0
        headings: set[str] = set()
        for number, line in enumerate(lines, 1):
            if line.lstrip().startswith("```"):
                fenced = not fenced
            if any(value.lower() in line.lower() for value in BANNED) or re.search(r"[A-Za-z]:\\", line):
                issue(path, number, "ruta temporal o local no permitida")
                errors += 1
            match = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
            if not match or fenced:
                continue
            level, title = len(match.group(1)), match.group(2).casefold()
            if level == 1:
                h1 += 1
            if previous_level and level > previous_level + 1:
                issue(path, number, f"salto de jerarquía de H{previous_level} a H{level}")
                errors += 1
            previous_level = level
            if title in headings:
                issue(path, number, "título duplicado en la misma página")
                errors += 1
            headings.add(title)
        if h1 != 1:
            issue(path, 1, f"debe contener un único H1; se encontraron {h1}")
            errors += 1
        if fenced:
            issue(path, len(lines), "bloque de código sin cerrar")
            errors += 1
    if errors:
        print(f"validate_content: {errors} error(es)")
        return 1
    print("validate_content: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
