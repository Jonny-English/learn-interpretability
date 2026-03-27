#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from repo_metadata import current_branch, current_repo_slug


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "course.json"
README_PATHS = {
    "en": ROOT / "README.md",
    "zh": ROOT / "README_zh.md",
}
DOCS_ROOT = ROOT / "docs"


def notebook_filename(module: dict) -> str:
    return f"{module['id'].lower()}_{module['slug'].replace('-', '_')}.ipynb"


def article_filename(module: dict) -> str:
    return f"{module['id'].lower()}-{module['slug']}.md"


def colab_url(module: dict, language: str) -> str | None:
    if not module["notebook_enabled"]:
        return None
    slug = current_repo_slug()
    branch = current_branch()
    path = f"notebooks/{language}/{notebook_filename(module)}"
    return f"https://colab.research.google.com/github/{slug}/blob/{branch}/{path}"


def notebook_link(module: dict, language: str, *, from_docs: bool) -> str:
    if not module["notebook_enabled"]:
        return "Reading-only" if language == "en" else "只读"
    prefix = "../../../" if from_docs else ""
    target = f"{prefix}notebooks/{language}/{notebook_filename(module)}"
    label = "Notebook" if language == "en" else "Notebook"
    return f"[{label}]({target})"


def article_link(module: dict, language: str, *, from_docs: bool) -> str:
    filename = article_filename(module)
    target = filename if from_docs else f"docs/{language}/articles/{filename}"
    title = module["title_en"] if language == "en" else module["title_zh"]
    return f"[{module['id']} {title}]({target})"


def root_article_table(course: list[dict], language: str) -> str:
    rows = ["| ID | Article | Paper | Mode | Docs | Colab |", "| --- | --- | --- | --- | --- | --- |"]
    for module in course:
        title = module["title_en"] if language == "en" else module["title_zh"]
        paper = module["paper_refs"][0]
        docs = f"[{module['id']}]({f'docs/{language}/articles/{article_filename(module)}'})"
        mode = "live" if module["notebook_enabled"] else ("reading-only" if language == "en" else "只读")
        colab = (
            f"[Colab]({colab_url(module, language)})"
            if module["notebook_enabled"]
            else ("-" if language == "en" else "-")
        )
        rows.append(
            f"| {module['id']} | {title} | [{paper['title']}]({paper['url']}) | {mode} | {docs} | {colab} |"
        )
    return "\n".join(rows)


def docs_article_table(course: list[dict], language: str, *, article_prefix: str) -> str:
    rows = ["| ID | Article | Paper | Notebook |", "| --- | --- | --- | --- |"]
    for module in course:
        paper = module["paper_refs"][0]
        notebook = (
            f"[Colab]({colab_url(module, language)})"
            if module["notebook_enabled"]
            else ("Reading-only" if language == "en" else "只读")
        )
        rows.append(
            f"| {module['id']} | [{module['id']} {module['title_en'] if language == 'en' else module['title_zh']}]"
            f"({article_prefix}{article_filename(module)}) | "
            f"[Distill]({paper['url']}) | {notebook} |"
        )
    return "\n".join(rows)


def render_readme(course: list[dict], language: str) -> str:
    if language == "en":
        return f"""# Learn Interpretability: Distill Circuits

A bilingual, Colab-first repository for working through the entire [Distill 2020 Circuits thread](https://distill.pub/2020/circuits/) with strict live-only notebooks.

This repository now does one thing only:

- map the Distill Circuits thread into a single `D00-D09` sequence
- keep mirrored English and Chinese notes
- generate live notebooks for `D01-D09`
- refuse pre-rendered `figures/`, precomputed `artifacts/`, and slideshow-style walkthroughs

## Start Here

- Read the thread entry: [D00 Thread: Circuits](docs/en/articles/{article_filename(course[0])})
- Open the first live notebook: [D01 in Colab]({colab_url(course[1], 'en')})
- Browse the docs index: [docs/en/index.md](docs/en/index.md)

## Why This Repo Exists

The Distill Circuits thread is still one of the clearest public introductions to neural circuits. The problem is that many readers meet it as a sequence of beautiful static pages. This repository rebuilds the thread as a runnable study path: each live notebook has to earn its claims with public weights, public data, and runtime-generated analysis.

## Distill Sequence

{root_article_table(course, language)}

## Repo Shape

- `content/course.json`: the single source of truth for `D00-D09`
- `docs/en` and `docs/zh`: mirrored article notes and navigation pages
- `notebooks/en` and `notebooks/zh`: mirrored live notebooks for `D01-D09`
- `utils/distill_circuits.py`: shared runtime helpers for InceptionV1, stimuli, searches, and weight analysis
- `scripts/`: notebook generation, README/docs rendering, validation, link checks, audit, and smoke tests

## Regenerate And Verify

```bash
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py
python3 scripts/validate_course.py
python3 scripts/audit_realtime_policy.py
python3 scripts/check_links.py
python3 scripts/smoke_notebooks.py
```
"""

    return f"""# Learn Interpretability: Distill Circuits

一个双语、Colab 优先、严格 live-only 的仓库，专门服务 [Distill 2020 Circuits 线程](https://distill.pub/2020/circuits/)。

这个仓库现在只做一件事：

- 把 Distill Circuits 线程收口成一条 `D00-D09` 学习线
- 维护中英双语镜像讲义
- 为 `D01-D09` 生成 live notebooks
- 明确拒绝预渲染 `figures/`、预计算 `artifacts/` 和幻灯片式讲解

## 从这里开始

- 先读线程入口：[D00 Circuits 线程总览](docs/zh/articles/{article_filename(course[0])})
- 直接打开第一本 live notebook：[D01 Colab]({colab_url(course[1], 'zh')})
- 浏览中文文档首页：[docs/zh/index.md](docs/zh/index.md)

## 为什么要做这个仓库

Distill 的 Circuits 线程依然是公开世界里最清晰的神经电路入门材料之一。问题在于，很多读者接触到它时，看到的是一串漂亮的静态页面。这个仓库把它改造成一条可运行的学习路径：每一本 live notebook 都必须用公开权重、公开数据和运行时生成的分析来为自己的说法负责。

## Distill 顺序

{root_article_table(course, language)}

## 仓库结构

- `content/course.json`：`D00-D09` 的唯一真相源
- `docs/en` 与 `docs/zh`：双语镜像讲义与导航页
- `notebooks/en` 与 `notebooks/zh`：`D01-D09` 的双语 live notebooks
- `utils/distill_circuits.py`：InceptionV1、刺激生成、搜索和权重分析的共享运行时工具
- `scripts/`：README/docs 渲染、notebook 生成、校验、审计、链接检查和 smoke 测试

## 重新生成与校验

```bash
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py
python3 scripts/validate_course.py
python3 scripts/audit_realtime_policy.py
python3 scripts/check_links.py
python3 scripts/smoke_notebooks.py
```
"""


def render_docs_index(course: list[dict], language: str) -> str:
    if language == "en":
        return f"""# Distill Circuits Index

This repository tracks the Distill Circuits thread as one mirrored bilingual sequence.

- Repo root: [README.md](../../README.md)
- Repo map: [repo-map.md](repo-map.md)
- Article list: [articles/index.md](articles/index.md)

## Sequence

{docs_article_table(course, language, article_prefix='articles/')}
"""
    return f"""# Distill Circuits 索引

这个仓库把 Distill Circuits 线程维护成一条中英镜像学习线。

- 仓库首页：[README_zh.md](../../README_zh.md)
- 仓库地图：[repo-map.md](repo-map.md)
- 文章列表：[articles/index.md](articles/index.md)

## 顺序

{docs_article_table(course, language, article_prefix='articles/')}
"""


def render_repo_map(language: str) -> str:
    if language == "en":
        return """# Repo Map

## Top Level

- [`content/`](../../content): course metadata and only the Distill article manifest
- [`docs/`](../../docs): mirrored English and Chinese notes
- [`notebooks/`](../../notebooks): generated live notebooks
- [`utils/`](../../utils): shared Distill runtime helpers
- [`scripts/`](../../scripts): generators, validation, audit, smoke tests, and link checks

## Maintenance Commands

```bash
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py
python3 scripts/validate_course.py
python3 scripts/audit_realtime_policy.py
python3 scripts/check_links.py
python3 scripts/smoke_notebooks.py
```
"""
    return """# 仓库地图

## 顶层结构

- [`content/`](../../content)：课程元数据和 Distill 文章清单
- [`docs/`](../../docs)：中英镜像讲义
- [`notebooks/`](../../notebooks)：生成出来的 live notebooks
- [`utils/`](../../utils)：共享 Distill runtime 工具
- [`scripts/`](../../scripts)：README/docs 渲染、生成、校验、审计、smoke 和链接检查

## 维护命令

```bash
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py
python3 scripts/validate_course.py
python3 scripts/audit_realtime_policy.py
python3 scripts/check_links.py
python3 scripts/smoke_notebooks.py
```
"""


def render_articles_index(course: list[dict], language: str) -> str:
    if language == "en":
        header = "# Distill Circuits Articles"
        lead = "Each entry below links to the article note and, when available, its live notebook."
    else:
        header = "# Distill Circuits 文章列表"
        lead = "下面每一项都链接到对应讲义；如果有 live notebook，也会一起给出。"
    return f"""{header}

{lead}

{docs_article_table(course, language, article_prefix='')}
"""


def render_article(module: dict, course: list[dict], language: str) -> str:
    title = module["title_en"] if language == "en" else module["title_zh"]
    summary = module["summary_en"] if language == "en" else module["summary_zh"]
    scope = module["notebook_scope_en"] if language == "en" else module["notebook_scope_zh"]
    integrity = module["integrity_note_en"] if language == "en" else module["integrity_note_zh"]
    live_sections = module["live_sections_en"] if language == "en" else module["live_sections_zh"]
    prereq_links = []
    for prereq in module["prereqs"]:
        target = next(item for item in course if item["id"] == prereq)
        prereq_links.append(article_link(target, language, from_docs=True))
    prereq_block = ", ".join(prereq_links) if prereq_links else ("None" if language == "en" else "无")
    paper = module["paper_refs"][0]
    notebook_block = (
        f"- Notebook: {notebook_link(module, language, from_docs=True)}\n- Colab: [Colab]({colab_url(module, language)})"
        if module["notebook_enabled"]
        else ("- Notebook: reading-only" if language == "en" else "- Notebook：只读")
    )
    live_block = "\n".join(f"- {item}" for item in live_sections) or ("- Reading-only thread entry" if language == "en" else "- 线程入口页，仅阅读")
    counterpart = f"../../{'zh' if language == 'en' else 'en'}/articles/{article_filename(module)}"
    counterpart_label = "Chinese" if language == "en" else "English"
    if language == "en":
        return f"""# {module['id']} {title}

- Distill article: [{paper['title']}]({paper['url']})
- Date: {paper['date']}
- Prerequisites: {prereq_block}
- Mirror: [{counterpart_label}]({counterpart})
{notebook_block}

## Summary

{summary}

## Notebook Scope

{scope}

## Live Coverage

{live_block}

## Integrity Note

{integrity}
"""
    return f"""# {module['id']} {title}

- Distill 原文：[{paper['title']}]({paper['url']})
- 日期：{paper['date']}
- 前置：{prereq_block}
- 镜像：[{counterpart_label}]({counterpart})
{notebook_block}

## 摘要

{summary}

## Notebook 范围

{scope}

## Live 覆盖

{live_block}

## 诚实边界

{integrity}
"""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n")


def main() -> None:
    course = json.loads(COURSE_PATH.read_text())
    for language in ("en", "zh"):
        write(README_PATHS[language], render_readme(course, language))
        write(DOCS_ROOT / language / "index.md", render_docs_index(course, language))
        write(DOCS_ROOT / language / "repo-map.md", render_repo_map(language))
        write(DOCS_ROOT / language / "articles" / "index.md", render_articles_index(course, language))
        for module in course:
            write(
                DOCS_ROOT / language / "articles" / article_filename(module),
                render_article(module, course, language),
            )


if __name__ == "__main__":
    main()
