#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "course.json"
FOUNDATIONS_PATH = ROOT / "content" / "foundations.json"
REFERENCE_OUTPUTS_PATH = ROOT / "content" / "reference_outputs.json"
EXTENSIONS_PATH = ROOT / "content" / "extensions.json"
REPO_SLUG = "Jonny-English/circuits-zoom-in-fresh-20260325"
README_PATHS = {
    "en": ROOT / "README.md",
    "zh": ROOT / "README_zh.md",
}


def notebook_path(module: dict, language: str) -> str:
    filename = f"{module['id'].lower()}_{module['web_slug'].replace('-', '_')}.ipynb"
    return f"notebooks/{language}/{filename}"


def colab_url(module: dict, language: str) -> str:
    return (
        "https://colab.research.google.com/github/"
        f"{REPO_SLUG}/blob/main/{notebook_path(module, language)}"
    )


def foundation_notebook_path(lab: dict, language: str) -> str:
    filename = f"{lab['id'].lower()}_{lab['web_slug'].replace('-', '_')}.ipynb"
    return f"notebooks/foundations/{language}/{filename}"


def foundation_colab_url(lab: dict, language: str) -> str:
    return (
        "https://colab.research.google.com/github/"
        f"{REPO_SLUG}/blob/main/{foundation_notebook_path(lab, language)}"
    )


def extension_notebook_path(item: dict, language: str) -> str:
    filename = f"{item['id'].lower()}_{item['notebook_slug']}.ipynb"
    return f"notebooks/extensions/{language}/{filename}"


def extension_colab_url(item: dict, language: str) -> str:
    return (
        "https://colab.research.google.com/github/"
        f"{REPO_SLUG}/blob/main/{extension_notebook_path(item, language)}"
    )


def build_table(course: list[dict], language: str) -> str:
    def notebook_cell(module: dict, lang: str) -> str:
        if not module["notebook_enabled"]:
            return "阅读" if lang == "zh" else "Reading"
        return f"[打开]({notebook_path(module, lang)})" if lang == "zh" else f"[Open]({notebook_path(module, lang)})"

    def colab_cell(module: dict, lang: str) -> str:
        if not module["notebook_enabled"]:
            return "-"
        return f"[Colab]({colab_url(module, lang)})"

    if language == "zh":
        header = "| ID | 文章 | 日期 | 状态 | Notebook | Colab | 运行层级 | 你会做什么 |\n|---|---|---|---|---|---|---|---|"
        rows = [
            f"| `{module['id']}` | {module['title_zh']} | `{module['paper_refs'][0]['date']}` | `{module['delivery_mode']}` | {notebook_cell(module, 'zh')} | {colab_cell(module, 'zh')} | `{module['runnable_tier']}` | {module['summary_zh']} |"
            for module in course
        ]
    else:
        header = "| ID | Paper | Date | Status | Notebook | Colab | Runnable tier | What you will do |\n|---|---|---|---|---|---|---|---|"
        rows = [
            f"| `{module['id']}` | {module['title_en']} | `{module['paper_refs'][0]['date']}` | `{module['delivery_mode']}` | {notebook_cell(module, 'en')} | {colab_cell(module, 'en')} | `{module['runnable_tier']}` | {module['summary_en']} |"
            for module in course
        ]
    return "\n".join([header, *rows])


def build_foundation_table(foundations: list[dict], language: str) -> str:
    if language == "zh":
        header = "| ID | 基础 Lab | Notebook | Colab | 运行层级 | 你会补齐什么 |\n|---|---|---|---|---|---|"
        rows = [
            f"| `{lab['id']}` | {lab['title_zh']} | [打开]({foundation_notebook_path(lab, 'zh')}) | [Colab]({foundation_colab_url(lab, 'zh')}) | `{lab['runnable_tier']}` | {lab['summary_zh']} |"
            for lab in foundations
        ]
    else:
        header = "| ID | Foundation Lab | Notebook | Colab | Runnable tier | What it repairs |\n|---|---|---|---|---|---|"
        rows = [
            f"| `{lab['id']}` | {lab['title_en']} | [Open]({foundation_notebook_path(lab, 'en')}) | [Colab]({foundation_colab_url(lab, 'en')}) | `{lab['runnable_tier']}` | {lab['summary_en']} |"
            for lab in foundations
        ]
    return "\n".join([header, *rows])


def build_reference_table(items: list[dict], language: str) -> str:
    if language == "zh":
        header = "| ID | 参考输出 | 文件 | 什么时候用 |\n|---|---|---|---|"
        rows = [
            f"| `{item['id']}` | {item['title_zh']} | [{item['path_zh']}]({item['path_zh']}) | {item['best_for_zh']} |"
            for item in items
        ]
    else:
        header = "| ID | Reference Output | File | When to use it |\n|---|---|---|---|"
        rows = [
            f"| `{item['id']}` | {item['title_en']} | [{item['path_en']}]({item['path_en']}) | {item['best_for_en']} |"
            for item in items
        ]
    return "\n".join([header, *rows])


def build_extension_table(items: list[dict], language: str) -> str:
    if language == "zh":
        header = "| ID | 扩展论文 | 链接 | 状态 | Notebook | Colab | 运行层级 | 为什么现在读 | 你要交什么 |\n|---|---|---|---|---|---|---|---|---|"
        rows = [
            f"| `{item['id']}` | {item['title_zh']} | [原文]({item['source_url']}) | `{item['delivery_mode']}` | [打开]({extension_notebook_path(item, 'zh')}) | [Colab]({extension_colab_url(item, 'zh')}) | `{item['runnable_tier']}` | {item['why_now_zh']} | {item['assignment_zh']} |"
            for item in items
        ]
    else:
        header = "| ID | Extension Paper | Link | Status | Notebook | Colab | Runnable tier | Why now | What to ship |\n|---|---|---|---|---|---|---|---|---|"
        rows = [
            f"| `{item['id']}` | {item['title_en']} | [Source]({item['source_url']}) | `{item['delivery_mode']}` | [Open]({extension_notebook_path(item, 'en')}) | [Colab]({extension_colab_url(item, 'en')}) | `{item['runnable_tier']}` | {item['why_now_en']} | {item['assignment_en']} |"
            for item in items
        ]
    return "\n".join([header, *rows])


def replace_block(text: str, rendered: str, block_name: str) -> str:
    start = f"<!-- {block_name}:START -->"
    end = f"<!-- {block_name}:END -->"
    before, remainder = text.split(start, maxsplit=1)
    _, after = remainder.split(end, maxsplit=1)
    return f"{before}{start}\n{rendered}\n{end}{after}"


def main() -> None:
    course = json.loads(COURSE_PATH.read_text())
    foundations = json.loads(FOUNDATIONS_PATH.read_text())
    reference_outputs = json.loads(REFERENCE_OUTPUTS_PATH.read_text())
    extensions = json.loads(EXTENSIONS_PATH.read_text())
    for language, path in README_PATHS.items():
        updated = path.read_text()
        updated = replace_block(updated, build_foundation_table(foundations, language), "FOUNDATION_TABLE")
        updated = replace_block(updated, build_table(course, language), "COURSE_TABLE")
        updated = replace_block(updated, build_reference_table(reference_outputs, language), "REFERENCE_TABLE")
        updated = replace_block(updated, build_extension_table(extensions, language), "EXTENSION_TABLE")
        path.write_text(updated)
        print(f"updated {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
