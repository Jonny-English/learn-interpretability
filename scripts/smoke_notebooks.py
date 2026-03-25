#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS_ROOT = ROOT / "notebooks"


def run_notebook(path: Path) -> None:
    payload = json.loads(path.read_text())
    globals_dict = {"__name__": "__main__"}
    exec("import matplotlib; matplotlib.use('Agg')", globals_dict, globals_dict)
    for index, cell in enumerate(payload.get("cells", []), start=1):
        if cell.get("cell_type") != "code":
            continue
        code = "".join(cell.get("source", []))
        if not code.strip():
            continue
        try:
            exec(compile(code, f"{path}:{index}", "exec"), globals_dict, globals_dict)
            exec("import matplotlib.pyplot as plt; plt.close('all')", globals_dict, globals_dict)
        except Exception as exc:  # noqa: BLE001
            raise RuntimeError(f"{path} failed at code cell {index}: {exc}") from exc


def discover_paths(modules: set[str] | None, languages: set[str] | None) -> list[Path]:
    paths = []
    for language in ("en", "zh"):
        if languages and language not in languages:
            continue
        for path in sorted((NOTEBOOKS_ROOT / language).glob("m*.ipynb")):
            if modules and path.stem.split("_", maxsplit=1)[0].upper() not in modules:
                continue
            paths.append(path)
        for path in sorted((NOTEBOOKS_ROOT / "foundations" / language).glob("f*.ipynb")):
            if modules and path.stem.split("_", maxsplit=1)[0].upper() not in modules:
                continue
            paths.append(path)
        for path in sorted((NOTEBOOKS_ROOT / "extensions" / language).glob("x*.ipynb")):
            if modules and path.stem.split("_", maxsplit=1)[0].upper() not in modules:
                continue
            paths.append(path)
    return paths


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", action="append", dest="modules", help="Module ID such as M01, F01, or X01")
    parser.add_argument("--lang", action="append", dest="languages", choices=["en", "zh"])
    args = parser.parse_args()

    modules = {module.upper() for module in args.modules} if args.modules else None
    languages = set(args.languages) if args.languages else None
    paths = discover_paths(modules, languages)
    if not paths:
        raise SystemExit("No notebooks matched the selection.")

    for path in paths:
        print(f"running {path.relative_to(ROOT)}")
        run_notebook(path)
    print(f"smoke-tested {len(paths)} notebooks")


if __name__ == "__main__":
    main()
