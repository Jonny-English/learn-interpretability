#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "course.json"
EXTENSIONS_PATH = ROOT / "content" / "extensions.json"
NOTEBOOKS_ROOT = ROOT / "notebooks"
FORBIDDEN_SNIPPETS = (
    'root / "artifacts"',
    "root / 'artifacts'",
    "artifacts/",
)


def fail(message: str) -> None:
    raise SystemExit(message)


def notebook_sources(path: Path) -> str:
    payload = json.loads(path.read_text())
    return "\n".join("".join(cell.get("source", [])) for cell in payload.get("cells", []))


def assert_live_notebook(path: Path) -> None:
    if not path.exists():
        fail(f"missing live notebook: {path.relative_to(ROOT)}")
    source = notebook_sources(path)
    for snippet in FORBIDDEN_SNIPPETS:
        if snippet in source:
            fail(f"live notebook references precomputed artifacts: {path.relative_to(ROOT)}")


def main() -> None:
    course = json.loads(COURSE_PATH.read_text())
    extensions = json.loads(EXTENSIONS_PATH.read_text())

    for module in course:
        filename = f"{module['id'].lower()}_{module['web_slug'].replace('-', '_')}.ipynb"
        for language in ("en", "zh"):
            path = NOTEBOOKS_ROOT / language / filename
            if module["notebook_enabled"]:
                assert_live_notebook(path)
            elif path.exists():
                fail(f"reading-only module still has a generated notebook: {path.relative_to(ROOT)}")

    for extension in extensions:
        filename = f"{extension['id'].lower()}_{extension['notebook_slug']}.ipynb"
        for language in ("en", "zh"):
            path = NOTEBOOKS_ROOT / "extensions" / language / filename
            assert_live_notebook(path)

    print(
        f"audited realtime policy for {sum(1 for module in course if module['notebook_enabled'])} core notebooks "
        f"and {len(extensions)} extension drills"
    )


if __name__ == "__main__":
    try:
        main()
    except SystemExit as exc:
        if exc.code not in (None, 0):
            print(exc, file=sys.stderr)
        raise
