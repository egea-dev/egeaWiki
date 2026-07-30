#!/usr/bin/env python3
"""Regenera MANIFEST_WIKIJS.json a partir de las páginas publicadas."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORDER = [
    "/simgest", "/simgest/migracion", *[f"/simgest/migracion/{n:02d}-{slug}" for n, slug in [
        (1, "cuentas-contables"), (2, "mapeo-formas-pago"), (3, "mapeo-localidades"), (4, "crear-localidad"),
        (5, "localidad-desconocida"), (6, "revision-post-migracion"), (7, "notas-advertencias")]],
    "/simgest/operativa", *[f"/simgest/operativa/{n:02d}-{slug}" for n, slug in [
        (1, "introduccion"), (2, "presupuestos"), (3, "formas-de-pago"), (4, "revision-presupuesto"),
        (5, "generar-pdf"), (6, "articulos-variantes-escandallos"), (7, "ficha-articulo-escandallo"),
        (8, "tarifas-proveedor"), (9, "pedidos-proveedor"), (10, "recepcion-mercancia"), (11, "pedidos-cliente"),
        (12, "columnas-visibles"), (13, "gestion-carga"), (14, "checklists"), (15, "errores-habituales")]],
]
TITLE = re.compile(r"^title:\s*(.+?)\s*$", re.M)
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)")


def source_for(route: str) -> Path:
    relative = route.lstrip("/")
    return ROOT / relative / "index.md" if route in {"/simgest", "/simgest/migracion", "/simgest/operativa"} else ROOT / f"{relative}.md"


def main() -> None:
    pages = []
    for position, route in enumerate(ORDER, 1):
        source = source_for(route)
        text = source.read_text(encoding="utf-8")
        title = TITLE.search(text).group(1).strip()
        if title.startswith('"') and title.endswith('"'):
            title = title[1:-1]
        targets = LINK.findall(text)
        pages.append({
            "route": route,
            "title": title,
            "source": source.relative_to(ROOT).as_posix(),
            "assets": sorted({target for target in targets if target.startswith("/assets/")}),
            "outgoing_links": sorted({target for target in targets if target.startswith("/simgest")}),
            "navigation_order": position,
        })
    (ROOT / "MANIFEST_WIKIJS.json").write_text(
        json.dumps({"format": "Wiki.js 2.x Git content manifest", "pages": pages}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
