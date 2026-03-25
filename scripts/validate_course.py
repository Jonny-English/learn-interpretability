#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "course.json"
ARTIFACTS_PATH = ROOT / "artifacts" / "manifest.json"
DOCS_ROOT = ROOT / "docs"
NOTEBOOKS_ROOT = ROOT / "notebooks"

REQUIRED_FIELDS = {
    "id",
    "order",
    "title_zh",
    "title_en",
    "summary_zh",
    "summary_en",
    "prereqs",
    "paper_refs",
    "artifact_refs",
    "runnable_tier",
    "web_slug",
}


def fail(message: str) -> None:
    raise SystemExit(message)


def assert_exists(path: Path, message: str) -> None:
    if not path.exists():
        fail(message)


def main() -> None:
    course = json.loads(COURSE_PATH.read_text())
    artifacts = json.loads(ARTIFACTS_PATH.read_text())
    artifact_ids = {artifact["id"] for artifact in artifacts}

    if not isinstance(course, list) or not course:
        fail("content/course.json must be a non-empty list")

    module_ids = []
    orders = []
    for module in course:
        missing = REQUIRED_FIELDS - set(module)
        if missing:
            fail(f"module {module.get('id', '<missing>')} is missing fields: {sorted(missing)}")
        module_ids.append(module["id"])
        orders.append(module["order"])
        for paper in module["paper_refs"]:
            for field in ("title", "url", "date"):
                if field not in paper:
                    fail(f"module {module['id']} paper ref missing {field}")
        for artifact_id in module["artifact_refs"]:
            if artifact_id not in artifact_ids:
                fail(f"module {module['id']} references missing artifact {artifact_id}")

        expected_docs = {
            "zh": DOCS_ROOT / "zh" / "modules" / f"{module['id'].lower()}-{module['web_slug']}.md",
            "en": DOCS_ROOT / "en" / "modules" / f"{module['id'].lower()}-{module['web_slug']}.md",
        }
        expected_notebooks = {
            "zh": NOTEBOOKS_ROOT / "zh" / f"{module['id'].lower()}_{module['web_slug'].replace('-', '_')}.ipynb",
            "en": NOTEBOOKS_ROOT / "en" / f"{module['id'].lower()}_{module['web_slug'].replace('-', '_')}.ipynb",
        }
        for language, path in expected_docs.items():
            assert_exists(path, f"missing {language} doc for {module['id']}: {path}")
        for language, path in expected_notebooks.items():
            assert_exists(path, f"missing {language} notebook for {module['id']}: {path}")

    if len(module_ids) != len(set(module_ids)):
        fail("module IDs must be unique")
    if orders != sorted(orders):
        fail("module order must be sorted")

    for language in ("zh", "en"):
        index_path = DOCS_ROOT / language / "index.md"
        assert_exists(index_path, f"missing docs index for {language}")

    print(f"validated {len(course)} modules and {len(artifacts)} artifacts")


if __name__ == "__main__":
    try:
        main()
    except SystemExit as exc:
        if exc.code not in (None, 0):
            print(exc, file=sys.stderr)
        raise
