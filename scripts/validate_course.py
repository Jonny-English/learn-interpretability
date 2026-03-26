#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "course.json"
PROGRAM_PATH = ROOT / "content" / "program.json"
FOUNDATIONS_PATH = ROOT / "content" / "foundations.json"
REFERENCE_OUTPUTS_PATH = ROOT / "content" / "reference_outputs.json"
EXTENSIONS_PATH = ROOT / "content" / "extensions.json"
SELF_CHECKS_PATH = ROOT / "content" / "self_checks.json"
ARTIFACTS_PATH = ROOT / "artifacts" / "manifest.json"
DOCS_ROOT = ROOT / "docs"
NOTEBOOKS_ROOT = ROOT / "notebooks"
TEMPLATES_ROOT = ROOT / "templates"
EXAMPLES_ROOT = ROOT / "examples"

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
    "delivery_mode",
    "notebook_enabled",
    "integrity_note_zh",
    "integrity_note_en",
    "runnable_tier",
    "web_slug",
}

PROGRAM_REQUIRED_FIELDS = {
    "goal_zh",
    "goal_en",
    "program_time_budget_zh",
    "program_time_budget_en",
    "entry_requirements_zh",
    "entry_requirements_en",
    "study_contract_zh",
    "study_contract_en",
    "start_tracks",
    "p6_decision_rule_zh",
    "p6_decision_rule_en",
    "p6_requirements_zh",
    "p6_requirements_en",
    "exit_portfolio_zh",
    "exit_portfolio_en",
    "phases",
    "weeks",
    "independent_sprints",
    "capstones",
    "rubric",
}

EXPECTED_PROGRAM_DOCS = {
    "research-ready.md",
    "first-week-checklist.md",
    "colab-first-path.md",
    "capability-arc.md",
    "p6-graduation-checklist.md",
    "week-by-week.md",
    "research-playbook.md",
    "evaluation-rubric.md",
    "independent-sprints.md",
    "reference-outputs.md",
    "advanced-extensions.md",
}

EXPECTED_TEMPLATE_FILES = {
    "paper_reading_note_en.md",
    "paper_reading_note_zh.md",
    "experiment_log_en.md",
    "experiment_log_zh.md",
    "research_memo_en.md",
    "research_memo_zh.md",
}

FOUNDATION_REQUIRED_FIELDS = {
    "id",
    "order",
    "title_zh",
    "title_en",
    "summary_zh",
    "summary_en",
    "prereqs",
    "skills_zh",
    "skills_en",
    "deliverables_zh",
    "deliverables_en",
    "questions_zh",
    "questions_en",
    "runnable_tier",
    "web_slug",
}

REFERENCE_OUTPUT_REQUIRED_FIELDS = {
    "id",
    "title_zh",
    "title_en",
    "summary_zh",
    "summary_en",
    "path_zh",
    "path_en",
    "best_for_zh",
    "best_for_en",
}

EXTENSION_REQUIRED_FIELDS = {
    "id",
    "order",
    "title_zh",
    "title_en",
    "source_url",
    "summary_zh",
    "summary_en",
    "why_now_zh",
    "why_now_en",
    "assignment_zh",
    "assignment_en",
    "delivery_mode",
    "integrity_note_zh",
    "integrity_note_en",
    "prereqs",
    "notebook_slug",
    "runnable_tier",
    "questions_zh",
    "questions_en",
}


def fail(message: str) -> None:
    raise SystemExit(message)


def assert_exists(path: Path, message: str) -> None:
    if not path.exists():
        fail(message)


def markdown_shape(path: Path) -> list[str]:
    shape = []
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("# "):
            shape.append("h1")
        elif line.startswith("## "):
            shape.append("h2")
        elif line.startswith("- "):
            shape.append("bullet")
        elif len(line) > 3 and line[0].isdigit() and line[1:3] == ". ":
            shape.append("numbered")
        else:
            shape.append("text")
    return shape


def main() -> None:
    course = json.loads(COURSE_PATH.read_text())
    program = json.loads(PROGRAM_PATH.read_text())
    foundations = json.loads(FOUNDATIONS_PATH.read_text())
    reference_outputs = json.loads(REFERENCE_OUTPUTS_PATH.read_text())
    extensions = json.loads(EXTENSIONS_PATH.read_text())
    self_checks = json.loads(SELF_CHECKS_PATH.read_text())
    artifacts = json.loads(ARTIFACTS_PATH.read_text())

    if not isinstance(course, list) or not course:
        fail("content/course.json must be a non-empty list")

    artifact_ids = [artifact["id"] for artifact in artifacts]
    if len(artifact_ids) != len(set(artifact_ids)):
        fail("artifact IDs must be unique")

    module_ids = [module["id"] for module in course]
    if len(module_ids) != len(set(module_ids)):
        fail("module IDs must be unique")

    orders = [module["order"] for module in course]
    if orders != sorted(orders):
        fail("module order must be sorted")

    artifact_lookup = {artifact["id"]: artifact for artifact in artifacts}
    expected_docs = {"en": set(), "zh": set()}
    expected_notebooks = {"en": set(), "zh": set()}
    expected_foundation_docs = {"en": set(), "zh": set()}
    expected_foundation_notebooks = {"en": set(), "zh": set()}
    expected_extension_docs = {"en": set(), "zh": set()}
    expected_extension_notebooks = {"en": set(), "zh": set()}

    for artifact in artifacts:
        if "path" in artifact:
            assert_exists(ROOT / artifact["path"], f"missing artifact file: {artifact['path']}")

    for module in course:
        missing = REQUIRED_FIELDS - set(module)
        if missing:
            fail(f"module {module.get('id', '<missing>')} is missing fields: {sorted(missing)}")
        if len(module["paper_refs"]) != 1:
            fail(f"module {module['id']} must reference exactly one paper")
        for prereq in module["prereqs"]:
            if prereq not in module_ids:
                fail(f"module {module['id']} references unknown prerequisite {prereq}")
        for paper in module["paper_refs"]:
            for field in ("title", "url", "date"):
                if field not in paper:
                    fail(f"module {module['id']} paper ref missing {field}")
        for artifact_id in module["artifact_refs"]:
            if artifact_id not in artifact_lookup:
                fail(f"module {module['id']} references missing artifact {artifact_id}")
        if module["delivery_mode"] == "reading-only" and module["notebook_enabled"]:
            fail(f"module {module['id']} cannot be reading-only and notebook-enabled at the same time")
        if not module["notebook_enabled"] and module["runnable_tier"] != "reading-only":
            fail(f"module {module['id']} must use runnable_tier=reading-only when notebook_enabled is false")

        doc_name = f"{module['id'].lower()}-{module['web_slug']}.md"
        notebook_name = f"{module['id'].lower()}_{module['web_slug'].replace('-', '_')}.ipynb"
        expected_docs["en"].add(doc_name)
        expected_docs["zh"].add(doc_name)
        if module["notebook_enabled"]:
            expected_notebooks["en"].add(notebook_name)
            expected_notebooks["zh"].add(notebook_name)

    if not isinstance(foundations, list) or not foundations:
        fail("content/foundations.json must be a non-empty list")
    foundation_ids = [foundation["id"] for foundation in foundations]
    if len(foundation_ids) != len(set(foundation_ids)):
        fail("foundation IDs must be unique")

    for foundation in foundations:
        missing = FOUNDATION_REQUIRED_FIELDS - set(foundation)
        if missing:
            fail(f"foundation {foundation.get('id', '<missing>')} is missing fields: {sorted(missing)}")
        for prereq in foundation["prereqs"]:
            if prereq not in foundation_ids:
                fail(f"foundation {foundation['id']} references unknown prerequisite {prereq}")
        for field in ("skills_zh", "skills_en", "deliverables_zh", "deliverables_en", "questions_zh", "questions_en"):
            if len(foundation[field]) < 2:
                fail(f"foundation {foundation['id']} field {field} must contain at least two entries")
        doc_name = f"{foundation['id'].lower()}-{foundation['web_slug']}.md"
        notebook_name = f"{foundation['id'].lower()}_{foundation['web_slug'].replace('-', '_')}.ipynb"
        expected_foundation_docs["en"].add(doc_name)
        expected_foundation_docs["zh"].add(doc_name)
        expected_foundation_notebooks["en"].add(notebook_name)
        expected_foundation_notebooks["zh"].add(notebook_name)

    if not isinstance(reference_outputs, list) or not reference_outputs:
        fail("content/reference_outputs.json must be a non-empty list")
    reference_ids = [entry["id"] for entry in reference_outputs]
    if len(reference_ids) != len(set(reference_ids)):
        fail("reference output IDs must be unique")
    for entry in reference_outputs:
        missing = REFERENCE_OUTPUT_REQUIRED_FIELDS - set(entry)
        if missing:
            fail(f"reference output {entry.get('id', '<missing>')} missing fields: {sorted(missing)}")
        assert_exists(ROOT / entry["path_zh"], f"missing zh reference output file: {entry['path_zh']}")
        assert_exists(ROOT / entry["path_en"], f"missing en reference output file: {entry['path_en']}")

    if not isinstance(extensions, list) or not extensions:
        fail("content/extensions.json must be a non-empty list")
    extension_ids = [entry["id"] for entry in extensions]
    if len(extension_ids) != len(set(extension_ids)):
        fail("extension IDs must be unique")
    extension_orders = [entry["order"] for entry in extensions]
    if extension_orders != sorted(extension_orders):
        fail("extension order must be sorted")
    for entry in extensions:
        missing = EXTENSION_REQUIRED_FIELDS - set(entry)
        if missing:
            fail(f"extension {entry.get('id', '<missing>')} missing fields: {sorted(missing)}")
        if entry["delivery_mode"] != "method-lab":
            fail(f"extension {entry['id']} must currently be labeled method-lab under the strict policy")
        for prereq in entry["prereqs"]:
            if prereq not in module_ids and prereq not in extension_ids:
                fail(f"extension {entry['id']} references unknown prerequisite {prereq}")
        if len(entry["questions_zh"]) < 2 or len(entry["questions_en"]) < 2:
            fail(f"extension {entry['id']} must contain at least two questions per language")
        doc_name = f"{entry['id'].lower()}-{entry['notebook_slug'].replace('_', '-')}.md"
        notebook_name = f"{entry['id'].lower()}_{entry['notebook_slug']}.ipynb"
        expected_extension_docs["en"].add(doc_name)
        expected_extension_docs["zh"].add(doc_name)
        expected_extension_notebooks["en"].add(notebook_name)
        expected_extension_notebooks["zh"].add(notebook_name)

    missing_program = PROGRAM_REQUIRED_FIELDS - set(program)
    if missing_program:
        fail(f"content/program.json is missing fields: {sorted(missing_program)}")
    if not program["phases"] or not program["weeks"] or not program["independent_sprints"] or not program["rubric"]:
        fail("content/program.json must define non-empty phases, weeks, independent_sprints, and rubric")

    phase_ids = [phase["id"] for phase in program["phases"]]
    if len(phase_ids) != len(set(phase_ids)):
        fail("program phase IDs must be unique")
    if not all(phase_id.startswith("S") for phase_id in phase_ids):
        fail("program phase IDs must use the internal Stage naming such as S0")

    week_ids = [week["id"] for week in program["weeks"]]
    if len(week_ids) != len(set(week_ids)):
        fail("program week IDs must be unique")

    for week in program["weeks"]:
        for module_id in week["module_ids"]:
            if module_id not in module_ids:
                fail(f"program week {week['id']} references unknown module {module_id}")

    if not isinstance(self_checks, list) or not self_checks:
        fail("content/self_checks.json must be a non-empty list")
    self_check_ids = [entry["module_id"] for entry in self_checks]
    if len(self_check_ids) != len(set(self_check_ids)):
        fail("self-check module IDs must be unique")
    if set(self_check_ids) != set(module_ids):
        fail(
            f"self-check module set mismatch. expected={sorted(module_ids)}, actual={sorted(self_check_ids)}"
        )
    for entry in self_checks:
        for field in ("module_id", "questions_zh", "questions_en"):
            if field not in entry:
                fail(f"self-check entry missing field: {field}")
        if len(entry["questions_zh"]) < 2 or len(entry["questions_en"]) < 2:
            fail(f"self-check entry {entry['module_id']} must contain at least two questions per language")

    program_doc_sets = {}
    for language in ("zh", "en"):
        program_dir = DOCS_ROOT / language / "program"
        assert_exists(program_dir, f"missing program docs directory for {language}")
        actual_program_docs = {path.name for path in program_dir.glob("*.md")}
        program_doc_sets[language] = actual_program_docs
        if actual_program_docs != EXPECTED_PROGRAM_DOCS:
            fail(
                f"{language} program docs mismatch. expected={sorted(EXPECTED_PROGRAM_DOCS)}, actual={sorted(actual_program_docs)}"
            )

    template_files = {path.name for path in TEMPLATES_ROOT.glob("*.md")}
    if template_files != EXPECTED_TEMPLATE_FILES:
        fail(
            f"template set mismatch. expected={sorted(EXPECTED_TEMPLATE_FILES)}, actual={sorted(template_files)}"
        )

    for language in ("zh", "en"):
        index_path = DOCS_ROOT / language / "index.md"
        assert_exists(index_path, f"missing docs index for {language}")

        docs_dir = DOCS_ROOT / language / "modules"
        actual_docs = {path.name for path in docs_dir.glob("*.md")}
        if actual_docs != expected_docs[language]:
            fail(
                f"{language} docs set mismatch. expected={sorted(expected_docs[language])}, actual={sorted(actual_docs)}"
            )

        notebooks_dir = NOTEBOOKS_ROOT / language
        actual_notebooks = {path.name for path in notebooks_dir.glob("m*.ipynb")}
        if actual_notebooks != expected_notebooks[language]:
            fail(
                f"{language} notebook set mismatch. expected={sorted(expected_notebooks[language])}, actual={sorted(actual_notebooks)}"
            )

        foundations_index = DOCS_ROOT / language / "foundations" / "index.md"
        assert_exists(foundations_index, f"missing foundations index for {language}")
        foundations_dir = DOCS_ROOT / language / "foundations"
        actual_foundation_docs = {path.name for path in foundations_dir.glob("f*.md")}
        if actual_foundation_docs != expected_foundation_docs[language]:
            fail(
                f"{language} foundation docs mismatch. expected={sorted(expected_foundation_docs[language])}, actual={sorted(actual_foundation_docs)}"
            )

        foundation_notebooks_dir = NOTEBOOKS_ROOT / "foundations" / language
        actual_foundation_notebooks = {path.name for path in foundation_notebooks_dir.glob("f*.ipynb")}
        if actual_foundation_notebooks != expected_foundation_notebooks[language]:
            fail(
                f"{language} foundation notebooks mismatch. expected={sorted(expected_foundation_notebooks[language])}, actual={sorted(actual_foundation_notebooks)}"
            )

        extensions_index = DOCS_ROOT / language / "extensions" / "index.md"
        assert_exists(extensions_index, f"missing extensions index for {language}")
        extensions_dir = DOCS_ROOT / language / "extensions"
        actual_extension_docs = {path.name for path in extensions_dir.glob("x*.md")}
        if actual_extension_docs != expected_extension_docs[language]:
            fail(
                f"{language} extension docs mismatch. expected={sorted(expected_extension_docs[language])}, actual={sorted(actual_extension_docs)}"
            )

        extension_notebooks_dir = NOTEBOOKS_ROOT / "extensions" / language
        actual_extension_notebooks = {path.name for path in extension_notebooks_dir.glob("x*.ipynb")}
        if actual_extension_notebooks != expected_extension_notebooks[language]:
            fail(
                f"{language} extension notebooks mismatch. expected={sorted(expected_extension_notebooks[language])}, actual={sorted(actual_extension_notebooks)}"
            )

    for module in course:
        zh_path = DOCS_ROOT / "zh" / "modules" / f"{module['id'].lower()}-{module['web_slug']}.md"
        en_path = DOCS_ROOT / "en" / "modules" / f"{module['id'].lower()}-{module['web_slug']}.md"
        if markdown_shape(zh_path) != markdown_shape(en_path):
            fail(f"module markdown structure mismatch for {module['id']}")

    for foundation in foundations:
        zh_path = DOCS_ROOT / "zh" / "foundations" / f"{foundation['id'].lower()}-{foundation['web_slug']}.md"
        en_path = DOCS_ROOT / "en" / "foundations" / f"{foundation['id'].lower()}-{foundation['web_slug']}.md"
        if markdown_shape(zh_path) != markdown_shape(en_path):
            fail(f"foundation markdown structure mismatch for {foundation['id']}")

    for entry in extensions:
        doc_name = f"{entry['id'].lower()}-{entry['notebook_slug'].replace('_', '-')}.md"
        zh_path = DOCS_ROOT / "zh" / "extensions" / doc_name
        en_path = DOCS_ROOT / "en" / "extensions" / doc_name
        if markdown_shape(zh_path) != markdown_shape(en_path):
            fail(f"extension markdown structure mismatch for {entry['id']}")

    for entry in reference_outputs:
        zh_path = ROOT / entry["path_zh"]
        en_path = ROOT / entry["path_en"]
        if markdown_shape(zh_path) != markdown_shape(en_path):
            fail(f"reference output markdown structure mismatch for {entry['id']}")

    live_article_count = sum(1 for module in course if module["notebook_enabled"])
    print(
        f"validated {len(course)} article entries with {live_article_count} live article notebooks, "
        f"{len(foundations)} foundation labs, {len(reference_outputs)} reference outputs, "
        f"{len(extensions)} extension papers, {len(artifacts)} artifacts, and "
        f"{len(program['weeks'])} research-ready weeks"
    )


if __name__ == "__main__":
    try:
        main()
    except SystemExit as exc:
        if exc.code not in (None, 0):
            print(exc, file=sys.stderr)
        raise
