#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from repo_metadata import current_branch, current_clone_dir, current_repo_url


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "course.json"
NOTEBOOKS_ROOT = ROOT / "notebooks"


def repo_root_snippet() -> str:
    repo_url = f"{current_repo_url()}.git"
    repo_dir = current_clone_dir()
    repo_branch = current_branch()
    return f"""import os
import subprocess
import sys
from pathlib import Path

REPO_URL = "{repo_url}"
REPO_DIR = "{repo_dir}"
REPO_BRANCH = "{repo_branch}"

if "google.colab" in sys.modules:
    candidate = Path("/content") / REPO_DIR
    if not candidate.exists():
        subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", REPO_BRANCH, REPO_URL, str(candidate)],
            check=True,
        )
    os.chdir(candidate)

root = Path.cwd().resolve()
while not (root / "content" / "course.json").exists():
    if root.parent == root:
        raise RuntimeError("Run this notebook from the repository root.")
    root = root.parent

if str(root) not in sys.path:
    sys.path.insert(0, str(root))
"""


def markdown_cell(text: str) -> dict:
    text = text.strip("\n")
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in text.splitlines()],
    }


def code_cell(code: str) -> dict:
    code = code.strip("\n")
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in code.splitlines()],
    }


def notebook(cells: list[dict]) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.10",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def badge_markdown(language: str, notebook_path: str) -> str:
    slug = current_repo_url().replace("https://github.com/", "")
    colab_url = f"https://colab.research.google.com/github/{slug}/blob/{current_branch()}/{notebook_path}"
    label = "Open in Colab" if language == "en" else "在 Colab 中打开"
    return f"[![{label}](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})"


def setup_code() -> str:
    return f"""{repo_root_snippet()}
import subprocess
import sys

if "google.colab" in sys.modules:
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-q", "torchvision", "torch-lucent", "matplotlib", "numpy", "Pillow"],
        check=True,
    )

from utils.distill_circuits import *

set_seed(0)
describe_runtime()
"""


def intro_markdown(module: dict, language: str, notebook_path: str) -> str:
    title = module["title_en"] if language == "en" else module["title_zh"]
    summary = module["summary_en"] if language == "en" else module["summary_zh"]
    scope = module["notebook_scope_en"] if language == "en" else module["notebook_scope_zh"]
    integrity = module["integrity_note_en"] if language == "en" else module["integrity_note_zh"]
    sections = module["live_sections_en"] if language == "en" else module["live_sections_zh"]
    sections_block = "\n".join(f"- {item}" for item in sections)
    section_header = "## Live Sections" if language == "en" else "## Live 内容"
    integrity_header = "## Integrity Note" if language == "en" else "## 诚实边界"
    scope_header = "## Notebook Scope" if language == "en" else "## Notebook 范围"
    return f"""
{badge_markdown(language, notebook_path)}

# {module['id']} {title}

{summary}

{scope_header}

{scope}

{section_header}

{sections_block}

{integrity_header}

{integrity}
"""


def closing_markdown(module: dict, language: str) -> str:
    title = module["title_en"] if language == "en" else module["title_zh"]
    if language == "en":
        return f"""
## Wrap-up

This notebook keeps **{title}** inside a strict live-only contract: every plot and every measurement comes from runtime execution on public weights, public data, and generated stimuli.
"""
    return f"""
## 小结

这本 notebook 把 **{title}** 保持在严格的 live-only 边界内：所有图和所有测量都来自公开权重、公开数据和运行时生成的刺激。
"""


def article_cells(module: dict, language: str, notebook_path: str) -> list[dict]:
    intro = intro_markdown(module, language, notebook_path)
    cells = [markdown_cell(intro), code_cell(setup_code())]
    article_id = module["id"]

    if article_id == "D01":
        cells.extend(
            [
                code_cell("plot_d01_feature_gallery()"),
                code_cell("plot_d01_real_image_validation()"),
                code_cell("plot_d01_orientation_tuning()"),
                code_cell("plot_d01_small_circuit_trace()"),
            ]
        )
    elif article_id == "D02":
        cells.append(code_cell("plot_d02_early_vision_overview()"))
    elif article_id == "D03":
        cells.extend(
            [
                code_cell("curve_channels = plot_d03_curve_detector_search()\nbest_curve_channel = curve_channels[0]"),
                code_cell("plot_d03_curve_response_comparison(best_curve_channel)"),
                code_cell("plot_d03_real_image_validation(best_curve_channel)"),
            ]
        )
    elif article_id == "D04":
        cells.extend(
            [
                code_cell("equivariance_pair = plot_d04_equivariance_search()"),
                code_cell("plot_d04_equivariance_responses(*equivariance_pair)"),
            ]
        )
    elif article_id == "D05":
        cells.extend(
            [
                code_cell("best_frequency_channel = plot_d05_frequency_detector_search()"),
                code_cell("plot_d05_frequency_tuning(best_frequency_channel)"),
            ]
        )
    elif article_id == "D06":
        cells.append(code_cell("plot_d06_curve_circuit()"))
    elif article_id == "D07":
        cells.append(code_cell("plot_d07_visualizing_weights()"))
    elif article_id == "D08":
        cells.append(code_cell("plot_d08_branch_specialization()"))
    elif article_id == "D09":
        cells.append(code_cell("plot_d09_weight_banding()"))
    else:
        raise ValueError(f"unsupported article ID: {article_id}")

    cells.append(markdown_cell(closing_markdown(module, language)))
    return cells


def notebook_name(module: dict) -> str:
    return f"{module['id'].lower()}_{module['slug'].replace('-', '_')}.ipynb"


def write_notebook(path: Path, cells: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(notebook(cells), indent=2) + "\n")


def remove_old_notebooks() -> None:
    for path in NOTEBOOKS_ROOT.rglob("*.ipynb"):
        path.unlink()


def main() -> None:
    course = json.loads(COURSE_PATH.read_text())
    remove_old_notebooks()

    for language in ("en", "zh"):
        for module in course:
            if not module["notebook_enabled"]:
                continue
            filename = notebook_name(module)
            relative_path = f"notebooks/{language}/{filename}"
            path = NOTEBOOKS_ROOT / language / filename
            cells = article_cells(module, language, relative_path)
            write_notebook(path, cells)


if __name__ == "__main__":
    main()
