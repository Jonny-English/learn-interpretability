#!/usr/bin/env python3
from __future__ import annotations

import ast
import io
import json
import sys
import tokenize
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "course.json"
EXTENSIONS_PATH = ROOT / "content" / "extensions.json"
NOTEBOOKS_ROOT = ROOT / "notebooks"
ARTIFACT_TOKEN = "artifacts"


def fail(message: str) -> None:
    raise SystemExit(message)


def notebook_cells(path: Path) -> list[tuple[int, str]]:
    payload = json.loads(path.read_text())
    cells = []
    for index, cell in enumerate(payload.get("cells", []), start=1):
        if cell.get("cell_type") == "code":
            cells.append((index, "".join(cell.get("source", []))))
    return cells


def source_mentions_artifacts(source: str) -> bool:
    try:
        tokens = tokenize.generate_tokens(io.StringIO(source).readline)
        for token in tokens:
            if token.type in (tokenize.NAME, tokenize.STRING) and ARTIFACT_TOKEN in token.string.lower():
                return True
    except tokenize.TokenError:
        return ARTIFACT_TOKEN in source.lower()
    return False


def local_imports(source: str) -> set[str]:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return set()
    imports: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module)
    return imports


def resolve_local_import(module_name: str) -> Path | None:
    relative = module_name.replace(".", "/")
    candidates = (
        ROOT / f"{relative}.py",
        ROOT / relative / "__init__.py",
    )
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def audit_source(label: str, source: str, visited: set[Path]) -> None:
    if source_mentions_artifacts(source):
        fail(f"live code references precomputed artifacts: {label}")
    for module_name in local_imports(source):
        local_path = resolve_local_import(module_name)
        if not local_path or local_path in visited:
            continue
        visited.add(local_path)
        audit_source(str(local_path.relative_to(ROOT)), local_path.read_text(), visited)


def assert_live_notebook(path: Path) -> None:
    if not path.exists():
        fail(f"missing live notebook: {path.relative_to(ROOT)}")
    visited: set[Path] = set()
    for cell_number, source in notebook_cells(path):
        audit_source(f"{path.relative_to(ROOT)}::cell{cell_number}", source, visited)


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
