#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "course.json"
DOCS_ROOT = ROOT / "docs"
NOTEBOOKS_ROOT = ROOT / "notebooks"

EXPECTED_IDS = [f"D{index:02d}" for index in range(10)]
REQUIRED_FIELDS = {
    "id",
    "order",
    "slug",
    "title_en",
    "title_zh",
    "summary_en",
    "summary_zh",
    "notebook_scope_en",
    "notebook_scope_zh",
    "live_sections_en",
    "live_sections_zh",
    "prereqs",
    "paper_refs",
    "delivery_mode",
    "notebook_enabled",
    "integrity_note_en",
    "integrity_note_zh",
    "runnable_tier",
}
BANNED_TERMS = [
    "Anthropic",
    "P6-ready",
    "bootcamp",
    "research-ready",
    "foundations",
    "extensions",
    "capability arc",
    "graduation checklist",
]
OBSOLETE_PATHS = [
    ROOT / "content" / "foundations.json",
    ROOT / "content" / "extensions.json",
    ROOT / "content" / "program.json",
    ROOT / "content" / "reference_outputs.json",
    ROOT / "content" / "self_checks.json",
    ROOT / "content" / "glossary.json",
    ROOT / "docs" / "en" / "foundations",
    ROOT / "docs" / "zh" / "foundations",
    ROOT / "docs" / "en" / "extensions",
    ROOT / "docs" / "zh" / "extensions",
    ROOT / "docs" / "en" / "modules",
    ROOT / "docs" / "zh" / "modules",
    ROOT / "docs" / "en" / "program",
    ROOT / "docs" / "zh" / "program",
    ROOT / "notebooks" / "foundations",
    ROOT / "notebooks" / "extensions",
    ROOT / "notebooks" / "circuits_zoom_in_en.ipynb",
    ROOT / "notebooks" / "circuits_zoom_in_zh.ipynb",
    ROOT / "examples",
    ROOT / "templates",
    ROOT / "launch",
    ROOT / "artifacts",
    ROOT / "figures",
    ROOT / "scripts" / "export_figures.py",
    ROOT / "scripts" / "generate_figures.py",
]


def fail(message: str) -> None:
    raise SystemExit(message)


def notebook_name(module: dict) -> str:
    return f"{module['id'].lower()}_{module['slug'].replace('-', '_')}.ipynb"


def article_name(module: dict) -> str:
    return f"{module['id'].lower()}-{module['slug']}.md"


def main() -> None:
    course = json.loads(COURSE_PATH.read_text())
    if not isinstance(course, list) or len(course) != 10:
        fail("content/course.json must contain exactly 10 Distill entries")

    ids = [module["id"] for module in course]
    if ids != EXPECTED_IDS:
        fail(f"expected IDs {EXPECTED_IDS}, got {ids}")

    for expected_order, module in enumerate(course):
        missing = REQUIRED_FIELDS - set(module)
        if missing:
            fail(f"module {module.get('id', '<missing>')} missing fields: {sorted(missing)}")
        if module["order"] != expected_order:
            fail(f"module {module['id']} has wrong order {module['order']}")
        if len(module["paper_refs"]) != 1:
            fail(f"module {module['id']} must have exactly one paper ref")
        if len(module["live_sections_en"]) != len(module["live_sections_zh"]):
            fail(f"module {module['id']} live section counts differ across languages")
        for prereq in module["prereqs"]:
            if prereq not in ids:
                fail(f"module {module['id']} references unknown prerequisite {prereq}")

    if course[0]["id"] != "D00" or course[0]["notebook_enabled"] or course[0]["runnable_tier"] != "reading-only":
        fail("D00 must be reading-only and notebook-disabled")

    for module in course[1:]:
        if not module["notebook_enabled"]:
            fail(f"{module['id']} must be notebook-enabled")
        if module["delivery_mode"] != "live-lab":
            fail(f"{module['id']} must be marked as live-lab")
        if module["runnable_tier"] != "cpu-colab":
            fail(f"{module['id']} must use runnable_tier=cpu-colab")

    for language in ("en", "zh"):
        index_path = DOCS_ROOT / language / "index.md"
        repo_map_path = DOCS_ROOT / language / "repo-map.md"
        articles_index_path = DOCS_ROOT / language / "articles" / "index.md"
        for path in (index_path, repo_map_path, articles_index_path):
            if not path.exists():
                fail(f"missing docs file: {path.relative_to(ROOT)}")
        expected_articles = {article_name(module) for module in course}
        actual_articles = {path.name for path in (DOCS_ROOT / language / "articles").glob("d*.md")}
        if expected_articles != actual_articles:
            fail(f"docs/{language}/articles mismatch: expected {sorted(expected_articles)}, got {sorted(actual_articles)}")
        expected_notebooks = {notebook_name(module) for module in course if module["notebook_enabled"]}
        actual_notebooks = {path.name for path in (NOTEBOOKS_ROOT / language).glob("d*.ipynb")}
        if expected_notebooks != actual_notebooks:
            fail(f"notebooks/{language} mismatch: expected {sorted(expected_notebooks)}, got {sorted(actual_notebooks)}")

    root_docs = [ROOT / "README.md", ROOT / "README_zh.md", ROOT / "CONTRIBUTING.md"]
    for path in root_docs + list(DOCS_ROOT.rglob("*.md")):
        text = path.read_text()
        for term in BANNED_TERMS:
            if term in text:
                fail(f"banned legacy term {term!r} found in {path.relative_to(ROOT)}")

    for path in OBSOLETE_PATHS:
        if path.exists():
            fail(f"obsolete path must be removed: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
