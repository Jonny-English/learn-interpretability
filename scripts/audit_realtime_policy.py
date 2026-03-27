#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS_ROOT = ROOT / "notebooks"
BANNED_SNIPPETS = [
    "artifacts/",
    "figures/",
    "circuits_zoom_in_",
    "content/extensions.json",
    "content/foundations.json",
    "content/program.json",
]


def notebook_code(path: Path) -> str:
    payload = json.loads(path.read_text())
    chunks = []
    for cell in payload.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        chunks.append("".join(cell.get("source", [])))
    return "\n".join(chunks)


def main() -> None:
    problems: list[str] = []
    for path in sorted(NOTEBOOKS_ROOT.rglob("d*.ipynb")):
        code = notebook_code(path)
        for snippet in BANNED_SNIPPETS:
            if snippet in code:
                problems.append(f"{path.relative_to(ROOT)} references banned snippet {snippet!r}")
    if problems:
        raise SystemExit("realtime audit failed: " + "; ".join(problems))


if __name__ == "__main__":
    main()
