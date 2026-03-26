#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from repo_metadata import current_branch, current_clone_dir, current_repo_url


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "course.json"
FOUNDATIONS_PATH = ROOT / "content" / "foundations.json"
EXTENSIONS_PATH = ROOT / "content" / "extensions.json"
SELF_CHECKS_PATH = ROOT / "content" / "self_checks.json"
OUTPUT_ROOT = ROOT / "notebooks"


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
                "version": "3.9",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


WORKSHEETS = {
    "M00": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Name the three terms you want to leave with: feature, circuit, intervention.",
            "Predict which live section will change your intuition most: feature visualization, CIFAR validation, orientation tuning, or circuit tracing.",
            "Open the paper-reading-note template before you run the notebook.",
        ],
        "before_zh": [
            "先写下你这篇要带走的 3 个词：feature、circuit、intervention。",
            "先预测哪一段 live 实验最会改变你的直觉：feature visualization、CIFAR 验证、方向调谐还是 circuit tracing。",
            "运行前先打开 paper-reading-note 模板。",
        ],
        "after_en": [
            "Write one paragraph on which output was actually measured live and which claims still rely on interpretation.",
            "List the first ambiguity that appears when you try to generalize this visual result to language models.",
        ],
        "after_zh": [
            "写一段话说明这次 notebook 里哪些结果是实时测出来的，哪些结论仍然带有解释成分。",
            "列出当你把这套视觉结果推广到语言模型时，最先出现的一个歧义点。",
        ],
        "ship_en": [
            "One reading note with a mentor/peer-summary paragraph.",
            "One experiment log covering at least one measured activation sweep.",
            "One glossary list of unclear terms.",
            "One next-question list for M01.",
        ],
        "ship_zh": [
            "1 份带导师/同伴摘要的 reading note。",
            "1 份至少覆盖一次激活测量的 experiment log。",
            "1 份不懂术语清单。",
            "1 份通往 M01 的 next-question list。",
        ],
    },
    "M01": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Choose one variable family to change: hidden dimension, sparsity, or loss weight.",
            "Predict how the geometry should change before you run the sweep.",
            "Write the baseline settings into the experiment-log template.",
        ],
        "before_zh": [
            "先选一个变量家族：hidden dimension、sparsity 或 loss weight。",
            "在做 sweep 之前，先预测几何图像会怎么变。",
            "先把 baseline 设置写进 experiment-log 模板。",
        ],
        "after_en": [
            "State the geometric reason overlap appears in your run.",
            "Separate what the plot shows directly from the story you tell about neurons.",
        ],
        "after_zh": [
            "写清这次 run 里概念重叠出现的几何原因。",
            "把图直接展示的东西和你对 neuron 的解释分开写。",
        ],
        "ship_en": [
            "One experiment log with baseline and one sweep.",
            "One annotated plot of the hidden geometry.",
            "One 100-200 word memo on why neuron semantics break.",
        ],
        "ship_zh": [
            "1 份带 baseline 和 sweep 的 experiment log。",
            "1 张带注释的隐藏空间图。",
            "1 份 100-200 字的 memo，说明为什么 neuron semantics 会失效。",
        ],
    },
    "M02": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Choose one axis to sweep: sparsity coefficient, feature count, or noise level.",
            "Write down what 'better feature recovery' means before you look at the result.",
            "Decide which failure pattern would make you distrust the recovered features.",
        ],
        "before_zh": [
            "先选一个要扫的轴：稀疏系数、feature 数量或噪声水平。",
            "在看结果前，先定义“更好的 feature recovery”是什么意思。",
            "先写下哪种失败模式会让你不信任这些恢复出来的 feature。",
        ],
        "after_en": [
            "Compare the recovered directions to the planted dictionary and name one mismatch.",
            "Write down the boundary where monosemanticity starts to degrade in your setup.",
        ],
        "after_zh": [
            "把恢复出来的方向和真实字典对比，并指出一个不匹配点。",
            "写清在你的设定里，monosemanticity 从哪里开始变差。",
        ],
        "ship_en": [
            "One experiment log with a sweep.",
            "One short note on failure boundaries.",
            "One next experiment that would test whether the degradation is about capacity or regularization.",
        ],
        "ship_zh": [
            "1 份带 sweep 的 experiment log。",
            "1 份失败边界短说明。",
            "1 个下一步实验，用来区分问题更像是 capacity 还是 regularization。",
        ],
    },
    "M03": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Decide how you want to group the catalog: by domain, usefulness, or ambiguity.",
            "Pick one feature you expect to be easy to recover and one you expect to be missing.",
            "Open the paper-reading-note template and write the question in one sentence.",
        ],
        "before_zh": [
            "先决定你要怎么给 catalog 分组：按领域、用途还是歧义程度。",
            "提前选一个你觉得容易恢复的 feature，再选一个你觉得可能缺失的 feature。",
            "先打开 paper-reading-note 模板，用一句话写下这篇的核心问题。",
        ],
        "after_en": [
            "Write one paragraph on why a catalog changes the research style from anecdotes to cartography.",
            "Name one missing-feature question that would be worth chasing next.",
        ],
        "after_zh": [
            "写一段话说明为什么 catalog 会把研究风格从轶事变成制图。",
            "提出一个值得继续追的缺失 feature 问题。",
        ],
        "ship_en": [
            "One taxonomy note.",
            "One missing-feature question.",
            "One short memo explaining how you would prioritize the next cataloging pass.",
        ],
        "ship_zh": [
            "1 份 taxonomy note。",
            "1 个缺失 feature 问题。",
            "1 份短 memo，说明下一轮 cataloging 你会优先找什么。",
        ],
    },
    "M04": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Pick one baseline and one possible confounder before you fit the probe.",
            "Write down what high accuracy would and would not prove.",
            "Decide which feature weight you expect to dominate.",
        ],
        "before_zh": [
            "在训练 probe 之前，先定一个 baseline 和一个潜在 confounder。",
            "先写清高 accuracy 能证明什么、不能证明什么。",
            "提前判断哪个 feature 权重会占主导。",
        ],
        "after_en": [
            "Explain why the strongest probe weight might still be misleading.",
            "List three confounders or alternative explanations for the result.",
        ],
        "after_zh": [
            "解释为什么最大的 probe 权重仍然可能误导你。",
            "列出 3 个 confounders 或替代解释。",
        ],
        "ship_en": [
            "One probe memo with baseline and confounders.",
            "One figure of feature weights.",
            "One proposed follow-up label or task.",
        ],
        "ship_zh": [
            "1 份包含 baseline 和 confounders 的 probe memo。",
            "1 张 feature 权重图。",
            "1 个后续标签或任务建议。",
        ],
    },
    "M05": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Define the target metric and one off-target metric before you run the sweep.",
            "Predict roughly where the sweet spot should appear.",
            "Write the stop condition for a bad steering direction.",
        ],
        "before_zh": [
            "在跑 sweep 之前，先定义 target metric 和一个 off-target metric。",
            "提前预测 sweet spot 大概会落在哪一段。",
            "先写下一个坏 steering 方向的 stop condition。",
        ],
        "after_en": [
            "Identify where benefit and collateral cost stop moving together.",
            "State the smallest steering strength you would ship and why.",
        ],
        "after_zh": [
            "指出收益和副作用开始不再同步变化的位置。",
            "写下如果要上线，你会选择的最小 steering strength 以及理由。",
        ],
        "ship_en": [
            "One steering evaluation memo.",
            "One explicit off-target metric.",
            "One failure-analysis paragraph on where the sweep becomes untrustworthy.",
        ],
        "ship_zh": [
            "1 份 steering evaluation memo。",
            "1 个明确写出的 off-target metric。",
            "1 段 failure analysis，说明从哪里开始这个 sweep 不再可信。",
        ],
    },
    "M06": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Choose one path or subgraph you plan to explain in detail.",
            "Write down what a faithful slice of computation means in this context.",
            "Open the memo template and reserve a section called 'what the graph does not prove'.",
        ],
        "before_zh": [
            "先挑一条你准备详细解释的路径或子图。",
            "先写下在这个语境里，什么叫 faithful slice of computation。",
            "打开 memo 模板，预留一段“这张图还不能证明什么”。",
        ],
        "after_en": [
            "Explain three high-contribution edges in plain language.",
            "Mark one ambiguity that would require a follow-up experiment.",
        ],
        "after_zh": [
            "用自己的话解释 3 条高贡献边。",
            "标出一个必须靠后续实验才能消除的歧义。",
        ],
        "ship_en": [
            "One graph walkthrough.",
            "One ambiguity note.",
            "One next experiment that would reduce uncertainty about the graph.",
        ],
        "ship_zh": [
            "1 份 graph walkthrough。",
            "1 份 ambiguity note。",
            "1 个能降低这张图不确定性的下一步实验。",
        ],
    },
    "M07": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Write the workflow stages you expect before loading the artifact.",
            "Pick one point in the pipeline where cost or latency might dominate.",
            "Decide what output a research engineer would actually need from the tool.",
        ],
        "before_zh": [
            "在加载 artifact 之前，先写下你预期的 workflow 阶段。",
            "提前挑一个你觉得成本或延迟会占主导的位置。",
            "先想清楚研究工程师真正需要工具输出什么。",
        ],
        "after_en": [
            "Point to the bottleneck that most shapes what research can be asked.",
            "Write one concrete tooling improvement request.",
        ],
        "after_zh": [
            "指出最会改变研究问题形状的那个 bottleneck。",
            "写一个具体的工具改进请求。",
        ],
        "ship_en": [
            "One workflow diagram.",
            "One bottleneck analysis.",
            "One tooling-needs note that could be handed to an engineer.",
        ],
        "ship_zh": [
            "1 张 workflow 图。",
            "1 份 bottleneck analysis。",
            "1 份可以直接交给工程师的 tooling-needs note。",
        ],
    },
    "M08": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Pick one trait you care about before looking at the artifact.",
            "Predict whether vector similarity should line up with behavioral similarity.",
            "Write one risk of controlling character through a direction.",
        ],
        "before_zh": [
            "在看 artifact 前，先选一个你最关心的 trait。",
            "预测向量相似度是否应该和行为相似度对齐。",
            "先写一条通过方向控制 character 的风险。",
        ],
        "after_en": [
            "Compare before/after trait shifts and say which one looks most controllable.",
            "State one reason persona control might drift or destabilize.",
        ],
        "after_zh": [
            "比较前后 trait 变化，并说哪个 trait 看起来最可控。",
            "写出 persona control 可能漂移或失稳的一个原因。",
        ],
        "ship_en": [
            "One short memo on what persona vectors make legible.",
            "One risk paragraph.",
            "One follow-up question about stability.",
        ],
        "ship_zh": [
            "1 份短 memo，说明 persona vectors 让什么变得可读。",
            "1 段风险说明。",
            "1 个关于稳定性的后续问题。",
        ],
    },
    "M09": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Predict where self-report and behavior should diverge most strongly.",
            "Write one warning against over-interpreting introspection-like signals.",
            "Decide which mismatch would be most interesting if it appeared.",
        ],
        "before_zh": [
            "先预测 self-report 和 behavior 最可能在哪些地方明显分叉。",
            "先写一条不要过度解释 introspection-like signals 的提醒。",
            "提前决定哪一种 mismatch 最值得研究。",
        ],
        "after_en": [
            "Rank the mismatch cases and explain why the top case matters.",
            "Write what evidence would be needed before making a stronger introspection claim.",
        ],
        "after_zh": [
            "给 mismatch 案例排个序，并解释为什么排第一的最重要。",
            "写出如果要提出更强的 introspection claim，还需要哪些证据。",
        ],
        "ship_en": [
            "One critique separating self-report from internal-state claims.",
            "One follow-up experiment idea.",
            "One short memo on the strongest mismatch.",
        ],
        "ship_zh": [
            "1 份 critique，把 self-report 和内部状态 claim 分开。",
            "1 个 follow-up experiment 想法。",
            "1 份关于最强 mismatch 的短 memo。",
        ],
    },
    "M10": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Predict how axis position should relate to helpfulness, safety, and warmth.",
            "Choose one failure mode of trying to stabilize assistant character.",
            "Write down one reason a single axis might be too simple.",
        ],
        "before_zh": [
            "先预测轴位置和 helpfulness、safety、warmth 之间会是什么关系。",
            "先挑一个稳定 assistant character 时可能出现的 failure mode。",
            "先写下一条“单一轴可能太简单”的理由。",
        ],
        "after_en": [
            "Explain what moves smoothly along the axis and what does not.",
            "State one reason character control may require a manifold rather than a single direction.",
        ],
        "after_zh": [
            "解释哪些属性会沿着这条轴平滑变化，哪些不会。",
            "写出为什么 character control 可能需要一个流形，而不是单一方向。",
        ],
        "ship_en": [
            "One short memo on what the axis captures.",
            "One failure-mode note.",
            "One two-week proposal idea for character stabilization.",
        ],
        "ship_zh": [
            "1 份短 memo，说明这条轴到底捕捉了什么。",
            "1 份 failure-mode note。",
            "1 个关于 character stabilization 的两周提案想法。",
        ],
    },
}

SELF_CHECKS = {
    entry["module_id"]: entry
    for entry in json.loads(SELF_CHECKS_PATH.read_text())
}
FOUNDATIONS = json.loads(FOUNDATIONS_PATH.read_text())
FOUNDATION_LOOKUP = {entry["id"]: entry for entry in FOUNDATIONS}
EXTENSIONS = json.loads(EXTENSIONS_PATH.read_text())
EXTENSION_LOOKUP = {entry["id"]: entry for entry in EXTENSIONS}


def bullet_block(heading: str, items: list[str]) -> str:
    return "\n".join([heading, "", *[f"- {item}" for item in items]])


def research_cells(module_id: str, language: str) -> list[dict]:
    worksheet = WORKSHEETS[module_id]
    title = worksheet["title_en"] if language == "en" else worksheet["title_zh"]
    before = worksheet["before_en"] if language == "en" else worksheet["before_zh"]
    after = worksheet["after_en"] if language == "en" else worksheet["after_zh"]
    ship = worksheet["ship_en"] if language == "en" else worksheet["ship_zh"]
    headings = {
        "en": ("## Turn this notebook into research output", "### Before you run", "### After you run", "### Ship these artifacts"),
        "zh": ("## 把这本 notebook 变成研究产出", "### 运行前", "### 运行后", "### 最后交付这些产物"),
    }
    intro_heading, before_heading, after_heading, ship_heading = headings[language]
    intro = (
        f"{intro_heading}\n\n"
        f"{title} means this notebook is not complete when the cells finish. "
        f"{'Use the templates in /templates and leave behind written outputs.' if language == 'en' else '请配合 /templates 里的模板，把结果写成可复查的输出。'}"
    )
    return [
        markdown_cell(intro),
        markdown_cell(bullet_block(before_heading, before)),
        markdown_cell(bullet_block(after_heading, after)),
        markdown_cell(bullet_block(ship_heading, ship)),
    ]


def self_check_cells(module_id: str, language: str) -> list[dict]:
    payload = SELF_CHECKS[module_id]
    questions = payload["questions_en"] if language == "en" else payload["questions_zh"]
    title = "## Self-check questions" if language == "en" else "## 验收题"
    pass_line = (
        "If you cannot answer at least two of these without rereading the note, revisit the article and your written outputs."
        if language == "en"
        else "如果你不能在不重看讲义的情况下独立答出其中至少 2 题，就回去重看文章和你的书面输出。"
    )
    return [markdown_cell(bullet_block(title, questions + [pass_line]))]


def foundation_context_cells(foundation_id: str, language: str) -> list[dict]:
    lab = FOUNDATION_LOOKUP[foundation_id]
    skills = lab["skills_en"] if language == "en" else lab["skills_zh"]
    deliverables = lab["deliverables_en"] if language == "en" else lab["deliverables_zh"]
    intro = (
        "## What this foundation lab is for\n\n"
        "This lab exists to reduce the most common beginner failure modes before the article-first path starts."
        if language == "en"
        else "## 这个基础 lab 是为了解决什么\n\n这本 lab 用来消除最常见的小白阻塞项，再进入文章优先主线。"
    )
    skill_heading = "## Skills you should leave with" if language == "en" else "## 做完后你应该带走的技能"
    ship_heading = "## Ship these outputs" if language == "en" else "## 最后交付这些产物"
    return [
        markdown_cell(intro),
        markdown_cell(bullet_block(skill_heading, skills)),
        markdown_cell(bullet_block(ship_heading, deliverables)),
    ]


def foundation_self_check_cells(foundation_id: str, language: str) -> list[dict]:
    lab = FOUNDATION_LOOKUP[foundation_id]
    questions = lab["questions_en"] if language == "en" else lab["questions_zh"]
    heading = "## Self-check questions" if language == "en" else "## 验收题"
    pass_line = (
        "If you cannot answer at least two questions without reopening the notebook, stay here before moving to the article track."
        if language == "en"
        else "如果你不能在不重开 notebook 的情况下独立答出至少 2 题，就先不要进入文章主线。"
    )
    return [markdown_cell(bullet_block(heading, questions + [pass_line]))]


def extension_context_cells(extension_id: str, language: str) -> list[dict]:
    entry = EXTENSION_LOOKUP[extension_id]
    goal_heading = "## Goal" if language == "en" else "## 目标"
    why_heading = "## Why this paper matters now" if language == "en" else "## 为什么现在学这篇"
    notebook_heading = "## Notebook and deliverable" if language == "en" else "## Notebook 与交付"
    prereq_label = "Prereqs" if language == "en" else "先修"
    source_label = "Source" if language == "en" else "原文"
    summary = entry["summary_en"] if language == "en" else entry["summary_zh"]
    why_now = entry["why_now_en"] if language == "en" else entry["why_now_zh"]
    assignment = entry["assignment_en"] if language == "en" else entry["assignment_zh"]
    notebook_path = f"notebooks/extensions/{language}/{entry['id'].lower()}_{entry['notebook_slug']}.ipynb"
    source_block = bullet_block(
        notebook_heading,
        [
            f"{source_label}: {entry['source_url']}",
            f"Notebook: `{notebook_path}`" if language == "en" else f"Notebook：`{notebook_path}`",
            f"{prereq_label}: {', '.join(entry['prereqs'])}",
            assignment,
        ],
    )
    return [
        markdown_cell(f"{goal_heading}\n\n{summary}"),
        markdown_cell(f"{why_heading}\n\n{why_now}"),
        markdown_cell(source_block),
    ]


def extension_workflow_cells(extension_id: str, language: str) -> list[dict]:
    title = "## Colab-first replication workflow" if language == "en" else "## Colab 优先的复现流程"
    before = [
        "Write one prediction about the mechanism before you run the cells.",
        "Name the baseline you are comparing against.",
        "Decide what result would count as a failure of your favorite story.",
    ] if language == "en" else [
        "在运行前先写 1 条你对机制的预测。",
        "先写清你要对比的 baseline 是什么。",
        "先决定什么结果会推翻你最喜欢的解释。",
    ]
    after = [
        "Separate observation from inference in your notes.",
        "Mark one ambiguity that still remains after the reproduction.",
        "Write one next experiment that would reduce that ambiguity.",
    ] if language == "en" else [
        "在笔记里把 observation 和 inference 分开。",
        "标出复现之后仍然存在的 1 个歧义。",
        "写 1 个能降低该歧义的下一步实验。",
    ]
    ship = [
        EXTENSION_LOOKUP[extension_id]["assignment_en"],
        "One experiment log with the exact settings you changed.",
        "One paragraph called 'what this reproduction still does not prove'.",
    ] if language == "en" else [
        EXTENSION_LOOKUP[extension_id]["assignment_zh"],
        "1 份 experiment log，写清你改了哪些设置。",
        "1 段“这次复现仍然不能证明什么”。",
    ]
    before_heading = "### Before you run" if language == "en" else "### 运行前"
    after_heading = "### After you run" if language == "en" else "### 运行后"
    ship_heading = "### Ship these outputs" if language == "en" else "### 最后交付这些产物"
    return [
        markdown_cell(title),
        markdown_cell(bullet_block(before_heading, before)),
        markdown_cell(bullet_block(after_heading, after)),
        markdown_cell(bullet_block(ship_heading, ship)),
    ]


def extension_self_check_cells(extension_id: str, language: str) -> list[dict]:
    entry = EXTENSION_LOOKUP[extension_id]
    questions = entry["questions_en"] if language == "en" else entry["questions_zh"]
    heading = "## Self-check questions" if language == "en" else "## 验收题"
    pass_line = (
        "If you cannot answer at least two questions without reopening the notebook, rerun the reproduction and rewrite the memo."
        if language == "en"
        else "如果你不能在不重开 notebook 的情况下独立答出至少 2 题，就回去重跑复现并重写 memo。"
    )
    return [markdown_cell(bullet_block(heading, questions + [pass_line]))]


def f00(language: str) -> list[dict]:
    intro = """
# F00 Environment, Plots, and Baseline Discipline
""" if language == "en" else """
# F00 环境、图表与基线纪律
"""
    code = repo_root_snippet() + """
import matplotlib.pyplot as plt
import torch
from torch import nn

torch.manual_seed(7)
features = torch.randn(256, 2)
true_weights = torch.tensor([1.8, -1.1])
logits = features @ true_weights + 0.25 * torch.randn(256)
labels = (logits > 0).float().unsqueeze(1)
train_x, val_x = features[:192], features[192:]
train_y, val_y = labels[:192], labels[192:]


def train_run(weight_decay: float, seed: int):
    torch.manual_seed(seed)
    model = nn.Linear(2, 1)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.25, weight_decay=weight_decay)
    loss_fn = nn.BCEWithLogitsLoss()
    train_losses, val_losses = [], []
    for _ in range(60):
        optimizer.zero_grad()
        train_logits = model(train_x)
        train_loss = loss_fn(train_logits, train_y)
        train_loss.backward()
        optimizer.step()
        with torch.no_grad():
            val_logits = model(val_x)
            val_loss = loss_fn(val_logits, val_y)
        train_losses.append(float(train_loss.detach()))
        val_losses.append(float(val_loss.detach()))
    with torch.no_grad():
        val_pred = (torch.sigmoid(model(val_x)) > 0.5).float()
        val_acc = float((val_pred.eq(val_y)).float().mean())
    return train_losses, val_losses, val_acc


baseline = train_run(weight_decay=0.0, seed=11)
variant = train_run(weight_decay=0.08, seed=11)

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(baseline[0], label="baseline train", color="#1f5f8b")
axes[0].plot(baseline[1], label="baseline val", color="#1f5f8b", linestyle="--")
axes[0].plot(variant[0], label="variant train", color="#c96a28")
axes[0].plot(variant[1], label="variant val", color="#c96a28", linestyle="--")
axes[0].set_title("Loss curves")
axes[0].set_xlabel("epoch")
axes[0].legend()

axes[1].bar(["baseline", "variant"], [baseline[2], variant[2]], color=["#1f5f8b", "#c96a28"])
axes[1].set_ylim(0.7, 1.0)
axes[1].set_title("Validation accuracy")
plt.tight_layout()

print("Baseline val accuracy:", round(baseline[2], 3))
print("Variant val accuracy:", round(variant[2], 3))
print("Judgment call: the variant changes regularization, so the baseline/variant pair is legible.")
"""
    takeaway = """
## Takeaway

Research starts when your runs stay distinct in writing: baseline, variant, metrics, and judgment call.
""" if language == "en" else """
## 小结

真正的研究起点，不是“能跑”，而是 baseline、variant、指标和 judgment call 都能在写作里分开。
"""
    return [markdown_cell(intro), *foundation_context_cells("F00", language), code_cell(code), markdown_cell(takeaway)]


def f01(language: str) -> list[dict]:
    intro = """
# F01 Transformer Shapes and Attention Reading
""" if language == "en" else """
# F01 Transformer 形状与注意力读图
"""
    code = repo_root_snippet() + """
import math
import matplotlib.pyplot as plt
import numpy as np

tokens = ["Ada", "wrote", "the", "patch", "carefully"]
embeddings = np.array([
    [1.0, 0.1, 0.3],
    [0.8, 0.4, 0.2],
    [0.2, 0.9, 0.1],
    [0.7, 0.3, 0.9],
    [0.9, 0.2, 0.8],
])
Wq = np.array([[1.0, 0.2], [0.1, 0.9], [0.7, 0.3]])
Wk = np.array([[0.9, 0.1], [0.2, 1.0], [0.6, 0.4]])
Wv = np.array([[0.4, 0.8], [0.9, 0.3], [0.3, 0.7]])

Q = embeddings @ Wq
K = embeddings @ Wk
V = embeddings @ Wv
scores = Q @ K.T / math.sqrt(K.shape[-1])
scores = scores - scores.max(axis=-1, keepdims=True)
weights = np.exp(scores)
weights = weights / weights.sum(axis=-1, keepdims=True)
contexts = weights @ V
residual_after = np.concatenate([embeddings[:, :2] + contexts, embeddings[:, 2:]], axis=-1)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
im = axes[0].imshow(weights, cmap="Blues")
axes[0].set_xticks(range(len(tokens)), tokens, rotation=30)
axes[0].set_yticks(range(len(tokens)), tokens)
axes[0].set_title("Attention weights")
plt.colorbar(im, ax=axes[0], fraction=0.046)

axes[1].plot(residual_after[-1], marker="o", color="#c96a28")
axes[1].set_title("Final-token residual update")
axes[1].set_xlabel("channel")
plt.tight_layout()

print("Q shape:", Q.shape, "| K shape:", K.shape, "| V shape:", V.shape)
print("Most attended token for the final position:", tokens[int(weights[-1].argmax())])
print("Final-position context vector:", np.round(contexts[-1], 3))
"""
    takeaway = """
## Takeaway

Before you can read circuits, you need to read shapes, attention matrices, and residual updates without hand-waving.
""" if language == "en" else """
## 小结

在你能读 circuit 之前，先要能不糊弄地读懂形状、attention 矩阵和 residual update。
"""
    return [markdown_cell(intro), *foundation_context_cells("F01", language), code_cell(code), markdown_cell(takeaway)]


def f02(language: str) -> list[dict]:
    intro = """
# F02 Vector Geometry, Features, and Probes
""" if language == "en" else """
# F02 向量几何、特征与探针
"""
    code = repo_root_snippet() + """
import matplotlib.pyplot as plt
import numpy as np

feature_truth = np.array([1.0, 0.25])
feature_spurious = np.array([0.65, 0.76])
feature_truth = feature_truth / np.linalg.norm(feature_truth)
feature_spurious = feature_spurious / np.linalg.norm(feature_spurious)

rng = np.random.default_rng(5)
positive = rng.normal(loc=[1.2, 0.5], scale=[0.22, 0.18], size=(18, 2))
negative = rng.normal(loc=[-0.9, -0.2], scale=[0.25, 0.2], size=(18, 2))
points = np.vstack([positive, negative])
labels = np.concatenate([np.ones(len(positive)), np.zeros(len(negative))])

centered_labels = labels * 2 - 1
probe = np.linalg.lstsq(points, centered_labels, rcond=None)[0]
probe = probe / np.linalg.norm(probe)

def cosine(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(positive[:, 0], positive[:, 1], color="#1f5f8b", label="positive")
ax.scatter(negative[:, 0], negative[:, 1], color="#c96a28", label="negative")
for vector, color, label in [
    (feature_truth, "#0f3d5e", "feature_truth"),
    (feature_spurious, "#8b5e34", "feature_spurious"),
    (probe, "#2d6a4f", "probe"),
]:
    ax.arrow(0, 0, vector[0], vector[1], width=0.02, color=color, length_includes_head=True)
    ax.text(vector[0] * 1.08, vector[1] * 1.08, label)
ax.axhline(0, color="0.85")
ax.axvline(0, color="0.85")
ax.set_title("Directions, projections, and a probe")
ax.legend()
ax.set_aspect("equal")
plt.tight_layout()

print("cos(feature_truth, probe) =", round(cosine(feature_truth, probe), 3))
print("cos(feature_spurious, probe) =", round(cosine(feature_spurious, probe), 3))
print("Average positive projection onto probe:", round(float((positive @ probe).mean()), 3))
print("Average negative projection onto probe:", round(float((negative @ probe).mean()), 3))
"""
    takeaway = """
## Takeaway

Once you see features as directions, probes become geometry plus supervision rather than mysterious semantic magic.
""" if language == "en" else """
## 小结

一旦把 feature 看成方向，probe 就不再像语义魔法，而更像“几何 + 监督信号”。
"""
    return [markdown_cell(intro), *foundation_context_cells("F02", language), code_cell(code), markdown_cell(takeaway)]


def f03(language: str) -> list[dict]:
    intro = """
# F03 Sweeps, Ablations, and Failure Analysis
""" if language == "en" else """
# F03 Sweep、Ablation 与 Failure Analysis
"""
    code = repo_root_snippet() + """
import matplotlib.pyplot as plt
import torch
from torch import nn

torch.manual_seed(19)
train_x = torch.randn(320, 3)
train_signal = 1.3 * train_x[:, 0] - 0.9 * train_x[:, 1]
train_x[:, 2] = 0.8 * (train_signal > 0).float() + 0.2 * torch.randn(320)
train_y = (train_signal > 0).float().unsqueeze(1)

ood_x = torch.randn(160, 3)
ood_signal = 1.3 * ood_x[:, 0] - 0.9 * ood_x[:, 1]
ood_x[:, 2] = 0.8 * (ood_signal < 0).float() + 0.2 * torch.randn(160)
ood_y = (ood_signal > 0).float().unsqueeze(1)


def train_model(weight_decay: float):
    torch.manual_seed(31)
    model = nn.Linear(3, 1)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.08, weight_decay=weight_decay)
    loss_fn = nn.BCEWithLogitsLoss()
    for _ in range(120):
        optimizer.zero_grad()
        loss = loss_fn(model(train_x), train_y)
        loss.backward()
        optimizer.step()
    with torch.no_grad():
        train_acc = float(((torch.sigmoid(model(train_x)) > 0.5).float().eq(train_y)).float().mean())
        ood_acc = float(((torch.sigmoid(model(ood_x)) > 0.5).float().eq(ood_y)).float().mean())
        weights = model.weight.detach().clone().squeeze(0)
        bias = float(model.bias.detach().clone().squeeze(0))
    return train_acc, ood_acc, weights, bias


def evaluate_ablation(weights: torch.Tensor, bias: float):
    ablated_x = ood_x.clone()
    ablated_x[:, 2] = 0.0
    logits = ablated_x @ weights[:3] + bias
    preds = (torch.sigmoid(logits.unsqueeze(1)) > 0.5).float()
    return float(preds.eq(ood_y).float().mean())


weight_decays = [0.0, 0.001, 0.01, 0.05, 0.1]
records = []
for wd in weight_decays:
    train_acc, ood_acc, weights, bias = train_model(wd)
    ablated_acc = evaluate_ablation(weights, bias)
    records.append((wd, train_acc, ood_acc, ablated_acc, float(weights[2])))

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
positions = list(range(len(weight_decays)))
axes[0].plot(positions, [row[1] for row in records], marker="o", label="train")
axes[0].plot(positions, [row[2] for row in records], marker="o", label="OOD")
axes[0].plot(positions, [row[3] for row in records], marker="o", label="OOD after ablation")
axes[0].set_title("Sweep over weight decay")
axes[0].set_xlabel("weight decay")
axes[0].set_xticks(positions, [str(value) for value in weight_decays], rotation=25)
axes[0].legend()

axes[1].bar([str(row[0]) for row in records], [row[4] for row in records], color="#c96a28")
axes[1].set_title("Weight placed on the spurious feature")
axes[1].set_xlabel("weight decay")
plt.tight_layout()

for wd, train_acc, ood_acc, ablated_acc, spurious_weight in records:
    print(
        f"wd={wd:>5} | train={train_acc:.3f} | OOD={ood_acc:.3f} | "
        f"OOD after ablation={ablated_acc:.3f} | spurious weight={spurious_weight:.3f}"
    )
"""
    takeaway = """
## Takeaway

The point of a sweep is not to produce many numbers. The point is to locate where your interpretation breaks or becomes robust.
""" if language == "en" else """
## 小结

sweep 的重点不是多跑几个数字，而是找到你的解释从哪里开始失效，或者从哪里开始变稳。
"""
    return [markdown_cell(intro), *foundation_context_cells("F03", language), code_cell(code), markdown_cell(takeaway)]


def m00(language: str) -> list[dict]:
    intro = """
# M00 Zoom In: An Introduction to Circuits

Run a live visual-circuits reproduction on a public InceptionV1 model.
""" if language == "en" else """
# M00 Zoom In：电路入门

在公开可用的 InceptionV1 上跑一遍 live 视觉电路复现。
"""
    context = """
## What this notebook does

- Loads a public pretrained vision model.
- Generates feature visualizations with activation maximization.
- Validates one neuron on real CIFAR-10 images.
- Measures orientation tuning on synthetic arc stimuli.
- Traces one small circuit by following learned weights upstream.
""" if language == "en" else """
## 本 notebook 会做什么

- 加载一个公开可用的预训练视觉模型。
- 用激活最大化实时生成 feature visualization。
- 在真实 CIFAR-10 图片上验证一个神经元。
- 用合成弧线刺激测量方向调谐。
- 通过真实权重往上追一条小型 circuit。
"""
    setup = """
import subprocess
import sys
from pathlib import Path

if "google.colab" in sys.modules:
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-q", "torchvision", "torch-lucent", "matplotlib", "numpy", "Pillow"],
        check=True,
    )

import matplotlib.pyplot as plt
import numpy as np
import torch
import torchvision
from lucent.modelzoo import inceptionv1
from lucent.optvis import objectives, render
from PIL import Image, ImageDraw
from torch.utils.data import DataLoader
from torchvision import transforms as T

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.manual_seed(0)

model = inceptionv1(pretrained=True).to(device).eval()
imagenet_mean = [0.485, 0.456, 0.406]
imagenet_std = [0.229, 0.224, 0.225]
transform = T.Compose([
    T.Resize(224),
    T.ToTensor(),
    T.Normalize(imagenet_mean, imagenet_std),
])
render_cache = {}

def denormalize(image_tensor):
    mean = torch.tensor(imagenet_mean).view(3, 1, 1)
    std = torch.tensor(imagenet_std).view(3, 1, 1)
    restored = (image_tensor.cpu() * std + mean).clamp(0.0, 1.0)
    return restored.permute(1, 2, 0).numpy()

def layer_mean_activation(layer_name, channel, batch):
    capture = {}

    def hook_fn(_module, _inputs, output):
        capture["value"] = output[:, channel].mean(dim=(1, 2)).detach().cpu()

    hook = dict(model.named_modules())[layer_name].register_forward_hook(hook_fn)
    with torch.no_grad():
        model(batch.to(device))
    hook.remove()
    return capture["value"]

def render_neuron(layer_name, channel, steps=12):
    key = (layer_name, channel, steps)
    if key not in render_cache:
        images = render.render_vis(
            model,
            objectives.channel(layer_name, channel),
            thresholds=(steps,),
            show_inline=False,
            progress=False,
        )
        render_cache[key] = images[0][0]
    return render_cache[key]

print("Loaded InceptionV1 on", device)
"""
    feature_viz = """
representative_neurons = [
    ("conv2d0", 0, "early edge / color"),
    ("mixed3a", 0, "edge bundle"),
    ("mixed3b", 379, "curve detector"),
]

fig, axes = plt.subplots(1, len(representative_neurons), figsize=(11, 3.6))
for ax, (layer_name, channel, label) in zip(axes, representative_neurons):
    image = render_neuron(layer_name, channel, steps=12)
    ax.imshow(image)
    ax.axis("off")
    ax.set_title(f"{layer_name}:{channel}\\n{label}", fontsize=9)
plt.suptitle("Live feature visualizations from a pretrained vision model", fontsize=11)
plt.tight_layout()

noise_batch = torch.randn(8, 3, 224, 224)
print("Mean activation on random noise:")
for layer_name, channel, label in representative_neurons:
    score = float(layer_mean_activation(layer_name, channel, noise_batch).mean())
    print(f"  {layer_name}:{channel:>3} ({label}) -> {score:.4f}")
"""
    validation = """
data_root = Path.cwd() / ".learn_interpretability_data" / "cifar10"
dataset = torchvision.datasets.CIFAR10(
    data_root,
    train=False,
    download=True,
    transform=transform,
)
loader = DataLoader(dataset, batch_size=64, shuffle=False, num_workers=0)

def top_activating_images(layer_name, channel, top_k=6, max_batches=3):
    score_chunks = []
    image_chunks = []
    label_chunks = []
    for batch_index, (images, labels) in enumerate(loader):
        if batch_index >= max_batches:
            break
        score_chunks.append(layer_mean_activation(layer_name, channel, images))
        image_chunks.append(images)
        label_chunks.append(labels)
    scores = torch.cat(score_chunks)
    images = torch.cat(image_chunks)
    labels = torch.cat(label_chunks)
    values, indices = torch.topk(scores, k=top_k)
    return images[indices], labels[indices], values

target_layer = "mixed3b"
target_channel = 379
synthetic = render_neuron(target_layer, target_channel, steps=12)
real_images, real_labels, real_scores = top_activating_images(target_layer, target_channel)

fig, axes = plt.subplots(2, 4, figsize=(11, 5.5))
axes[0, 0].imshow(synthetic)
axes[0, 0].axis("off")
axes[0, 0].set_title("Synthetic preference", fontsize=9)
for ax in axes.flatten()[1:]:
    ax.axis("off")

for index in range(6):
    row = index // 3
    col = (index % 3) + 1
    axes[row, col].imshow(denormalize(real_images[index]))
    axes[row, col].axis("off")
    axes[row, col].set_title(
        f"{dataset.classes[int(real_labels[index])]}\\nscore={float(real_scores[index]):.3f}",
        fontsize=8,
    )

plt.suptitle("Live validation on real CIFAR-10 images", fontsize=11)
plt.tight_layout()
print("Top CIFAR-10 labels:", [dataset.classes[int(label)] for label in real_labels])
"""
    tuning = """
def make_arc_batch(angle_degrees, image_size=224, radius=60, line_width=5):
    image = Image.new("RGB", (image_size, image_size), (128, 128, 128))
    draw = ImageDraw.Draw(image)
    center_x = image_size // 2
    center_y = image_size // 2
    box = [center_x - radius, center_y - radius, center_x + radius, center_y + radius]
    draw.arc(box, start=float(angle_degrees) - 60.0, end=float(angle_degrees) + 60.0, fill=(255, 255, 255), width=line_width)
    return transform(image).unsqueeze(0), image

angles = np.linspace(0.0, 345.0, 24)
responses = []
preview_angles = [0.0, 60.0, 120.0]

fig = plt.figure(figsize=(12, 3.8))
grid = fig.add_gridspec(1, 4, width_ratios=[1.0, 1.0, 1.0, 1.6])
preview_axes = [fig.add_subplot(grid[0, index]) for index in range(3)]
polar_ax = fig.add_subplot(grid[0, 3], projection="polar")

for ax, angle in zip(preview_axes, preview_angles):
    batch, preview = make_arc_batch(angle)
    ax.imshow(preview)
    ax.axis("off")
    ax.set_title(f"{int(angle)} deg", fontsize=9)

for angle in angles:
    batch, _ = make_arc_batch(angle)
    responses.append(float(layer_mean_activation(target_layer, target_channel, batch)[0]))

responses = np.array(responses)
closed_angles = np.deg2rad(np.append(angles, angles[0]))
closed_responses = np.append(responses, responses[0])
polar_ax.plot(closed_angles, closed_responses, marker="o", color="#c96a28")
polar_ax.set_title("Orientation tuning for mixed3b:379", fontsize=10)
polar_ax.set_theta_zero_location("N")
polar_ax.set_theta_direction(-1)
plt.tight_layout()

preferred_angle = float(angles[int(np.argmax(responses))])
print("Preferred orientation:", round(preferred_angle, 1), "degrees")
print("Peak response:", round(float(responses.max()), 4))
"""
    circuit = """
target_channel = 379
branch_index = target_channel - 320
weights_bottleneck = model.mixed3b_5x5_bottleneck_pre_relu_conv.weight.detach().cpu().squeeze(-1).squeeze(-1)
weights_5x5 = model.mixed3b_5x5_pre_relu_conv.weight.detach().cpu()

target_filter = weights_5x5[branch_index]
bottleneck_importance = target_filter.abs().sum(dim=(1, 2))
upstream_importance = (bottleneck_importance[:, None] * weights_bottleneck.abs()).sum(dim=0)
top_values, top_indices = torch.topk(upstream_importance, k=6)
display_channels = top_indices[:2].tolist()

fig, axes = plt.subplots(1, 4, figsize=(12, 3.6))
for ax, channel in zip(axes[:2], display_channels):
    ax.imshow(render_neuron("mixed3a", int(channel), steps=10))
    ax.axis("off")
    ax.set_title(f"mixed3a:{channel}", fontsize=9)

axes[2].bar(range(len(top_values)), top_values.tolist(), color="#1f5f8b")
axes[2].set_xticks(range(len(top_values)), [str(int(index)) for index in top_indices.tolist()], rotation=30)
axes[2].set_title("Top upstream channels", fontsize=10)
axes[2].set_xlabel("mixed3a channel")

axes[3].imshow(render_neuron("mixed3b", target_channel, steps=10))
axes[3].axis("off")
axes[3].set_title(f"mixed3b:{target_channel}", fontsize=9)
plt.suptitle("Tracing a small circuit through learned weights", fontsize=11)
plt.tight_layout()

print("Top upstream channels for mixed3b:379:")
for channel, value in zip(top_indices.tolist(), top_values.tolist()):
    print(f"  mixed3a:{int(channel):>3} -> importance {float(value):.3f}")
"""
    takeaway = """
## Takeaway

This notebook now earns the basic visual-circuits story live: a neuron preference, a real-image check, a tuning curve, and an upstream-weight trace. The picture is still cleaner than language-model interpretability, but it is no longer a slideshow.
""" if language == "en" else """
## 小结

这本 notebook 现在是把视觉电路故事真正跑出来：神经元偏好、真实图片验证、方向调谐曲线，以及一条上游权重 trace。它依然比语言模型里的情况干净，但已经不是幻灯片式讲解了。
"""
    return [
        markdown_cell(intro),
        markdown_cell(context),
        code_cell(setup),
        code_cell(feature_viz),
        code_cell(validation),
        code_cell(tuning),
        code_cell(circuit),
        markdown_cell(takeaway),
    ]


def m01(language: str) -> list[dict]:
    intro = """
# M01 Toy Models of Superposition
""" if language == "en" else """
# M01 Toy Models of Superposition
"""
    context = """
## Toy setup

Compress four sparse concepts into a two-dimensional hidden space and inspect how overlap appears.
""" if language == "en" else """
## Toy 设定

把 4 个稀疏概念压进 2 维隐藏空间，观察概念重叠是怎么出现的。
"""
    code = """
import torch
import matplotlib.pyplot as plt

torch.manual_seed(7)

num_features = 4
hidden_dim = 2
encoder = torch.nn.Linear(num_features, hidden_dim, bias=False)
decoder = torch.nn.Linear(hidden_dim, num_features, bias=False)
optimizer = torch.optim.Adam(list(encoder.parameters()) + list(decoder.parameters()), lr=0.05)

for step in range(500):
    active = (torch.rand(512, num_features) < 0.22).float()
    strengths = torch.rand(512, num_features)
    batch = active * strengths
    hidden = encoder(batch)
    recon = decoder(hidden)
    loss = torch.nn.functional.mse_loss(recon, batch) + 0.002 * hidden.abs().mean()
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

samples = torch.eye(num_features)
hidden_samples = encoder(samples).detach()

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].scatter(hidden_samples[:, 0], hidden_samples[:, 1], s=130, c=range(num_features), cmap="tab10")
for index, point in enumerate(hidden_samples):
    axes[0].annotate(f"f{index}", (point[0].item(), point[1].item()))
axes[0].set_title("Feature positions in 2D hidden space")
axes[0].axhline(0, color="0.8", linewidth=1)
axes[0].axvline(0, color="0.8", linewidth=1)

axes[1].imshow(decoder.weight.detach().T, cmap="coolwarm", aspect="auto")
axes[1].set_title("Decoder weights")
axes[1].set_xlabel("Hidden dimension")
axes[1].set_ylabel("Original feature")
plt.tight_layout()

print("Final loss:", float(loss.detach()))
print("Hidden representations:\\n", hidden_samples)
"""
    takeaway = """
## Takeaway

Once the hidden space is smaller than the concept set, overlap stops being a bug and becomes the expected geometry.
""" if language == "en" else """
## 小结

一旦隐藏空间小于概念集合，重叠就不再是 bug，而会变成预期中的几何结构。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m02(language: str) -> list[dict]:
    intro = """
# M02 Towards Monosemanticity
""" if language == "en" else """
# M02 Towards Monosemanticity
"""
    context = """
## Sparse autoencoder toy lab

Generate activations from a hidden dictionary, then train a tiny sparse autoencoder to recover reusable directions.
""" if language == "en" else """
## Sparse autoencoder 教学实验

先用一个隐藏字典生成激活，再训练一个小型 sparse autoencoder 去恢复可复用方向。
"""
    code = """
import torch
import matplotlib.pyplot as plt

torch.manual_seed(11)

activation_dim = 6
true_features = 4
sae_features = 8

true_dictionary = torch.tensor(
    [
        [1.0, 0.0, 0.0, 0.5],
        [0.8, 0.1, 0.2, 0.0],
        [0.0, 0.9, 0.1, 0.4],
        [0.0, 0.8, 0.4, 0.1],
        [0.3, 0.0, 0.9, 0.2],
        [0.1, 0.2, 0.8, 1.0],
    ],
    dtype=torch.float32,
)

encoder = torch.nn.Linear(activation_dim, sae_features)
decoder = torch.nn.Linear(sae_features, activation_dim, bias=False)
optimizer = torch.optim.Adam(list(encoder.parameters()) + list(decoder.parameters()), lr=0.03)

for step in range(700):
    sparse_codes = (torch.rand(256, true_features) < 0.28).float() * torch.rand(256, true_features)
    activations = sparse_codes @ true_dictionary.T + 0.02 * torch.randn(256, activation_dim)
    hidden = torch.relu(encoder(activations))
    recon = decoder(hidden)
    loss = torch.nn.functional.mse_loss(recon, activations) + 0.01 * hidden.mean()
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

decoder_weights = decoder.weight.detach().T
norms = decoder_weights.norm(dim=1)
top_indices = torch.topk(norms, k=4).indices

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].imshow(true_dictionary, cmap="viridis", aspect="auto")
axes[0].set_title("Ground-truth dictionary")
axes[0].set_xlabel("Feature")
axes[0].set_ylabel("Activation dimension")

axes[1].imshow(decoder_weights[top_indices], cmap="viridis", aspect="auto")
axes[1].set_title("Recovered decoder directions (top 4)")
axes[1].set_xlabel("Activation dimension")
axes[1].set_ylabel("Recovered feature")
plt.tight_layout()

print("Top recovered feature indices:", top_indices.tolist())
print("Final loss:", float(loss.detach()))
"""
    takeaway = """
## Takeaway

The recovered directions are not perfect copies of the planted dictionary, but they are much easier to reuse and reason about than the raw basis.
""" if language == "en" else """
## 小结

恢复出来的方向不会完美等于埋进去的字典，但它们比原始基底更容易复用，也更容易讲清楚。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m03(language: str) -> list[dict]:
    intro = """
# M03 Mapping the Mind of a Large Language Model
""" if language == "en" else """
# M03 Mapping the Mind
"""
    context = """
## Browse a teaching-scale feature catalog

This notebook loads a tiny catalog of features and groups them by domain so you can see the shift from isolated examples to feature maps.
""" if language == "en" else """
## 浏览教学版 feature catalog

这本 notebook 读取一个小型 feature 目录，并按领域分组，展示 interpretability 如何从零散例子走向 feature 地图。
"""
    code = repo_root_snippet() + """
import json
from collections import Counter
import matplotlib.pyplot as plt

payload = json.loads((root / "artifacts" / "m03_feature_catalog.json").read_text())
features = payload["features"]
domain_counts = Counter(feature["domain_en"] for feature in features)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].bar(domain_counts.keys(), domain_counts.values(), color="#1f5f8b")
axes[0].set_title("Features per domain")
axes[0].tick_params(axis="x", rotation=20)

top_features = sorted(features, key=lambda item: item["max_activation"], reverse=True)
axes[1].bar(
    [feature["label_en"] for feature in top_features],
    [feature["max_activation"] for feature in top_features],
    color="#c96a28",
)
axes[1].set_title("Maximum activation by feature")
axes[1].tick_params(axis="x", rotation=35)
plt.tight_layout()

print("Top feature cards:")
for feature in top_features:
    print("-", feature["label_en"], "|", feature["domain_en"], "|", feature["max_activation"])
    for example in feature["examples_en"]:
        print("   ", example)
"""
    takeaway = """
## Takeaway

Once features can be grouped, ranked, and browsed, interpretability starts looking like cartography instead of isolated case studies.
""" if language == "en" else """
## 小结

一旦 feature 可以被分组、排序和浏览，interpretability 看起来就更像制图，而不再只是孤立案例。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m04(language: str) -> list[dict]:
    intro = """
# M04 Using Dictionary Learning Features as Classifiers
""" if language == "en" else """
# M04 Features as Classifiers
"""
    context = """
## Probe on top of features

Train a tiny classifier on synthetic feature activations and inspect which recovered directions matter most.
""" if language == "en" else """
## 在 feature 上做 probe

在 synthetic feature activation 上训练一个小分类器，看看哪些恢复出的方向最重要。
"""
    code = """
import torch
import matplotlib.pyplot as plt

torch.manual_seed(31)

feature_names = ["calendar", "citation", "refusal", "tool"]
features = torch.randn(400, 4)
target = 1.4 * features[:, 2] + 0.8 * features[:, 3] - 0.9 * features[:, 1]
labels = (torch.sigmoid(target) > 0.5).float().unsqueeze(1)

probe = torch.nn.Linear(4, 1)
optimizer = torch.optim.Adam(probe.parameters(), lr=0.05)

for step in range(500):
    logits = probe(features)
    loss = torch.nn.functional.binary_cross_entropy_with_logits(logits, labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

with torch.no_grad():
    probs = torch.sigmoid(probe(features))
    accuracy = ((probs > 0.5).float() == labels).float().mean().item()
    weights = probe.weight.flatten()

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(feature_names, weights.tolist(), color=["#4c78a8", "#9ecae9", "#f58518", "#54a24b"])
ax.axhline(0, color="0.75", linewidth=1)
ax.set_title("Probe weights over recovered features")
plt.tight_layout()

print("Final BCE loss:", float(loss.detach()))
print("Accuracy:", round(accuracy, 3))
print("Weights:", dict(zip(feature_names, [round(value, 3) for value in weights.tolist()])))
"""
    takeaway = """
## Takeaway

Feature quality becomes measurable once features can support a readout task.
""" if language == "en" else """
## 小结

一旦 feature 可以支撑读出任务，feature 的质量就开始变得可衡量。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m05(language: str) -> list[dict]:
    intro = """
# M05 Evaluating Feature Steering
""" if language == "en" else """
# M05 Evaluating Feature Steering
"""
    context = """
## Sweep steering strength

Simulate how target improvement and off-target cost change as you move farther along a steering direction.
""" if language == "en" else """
## 扫描 steering 强度

模拟沿着 steering 方向越走越远时，目标增益和副作用成本如何一起变化。
"""
    code = """
import torch
import matplotlib.pyplot as plt

strengths = torch.linspace(-1.2, 1.6, 28)
target_gain = torch.sigmoid(2.9 * (strengths - 0.05))
off_target = 0.06 + 0.24 * torch.relu(strengths - 0.25) ** 2
utility = target_gain - off_target
best_index = int(torch.argmax(utility))

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(strengths.tolist(), target_gain.tolist(), label="target gain", color="#1f5f8b", linewidth=2.4)
ax.plot(strengths.tolist(), off_target.tolist(), label="off-target cost", color="#c96a28", linewidth=2.4)
ax.plot(strengths.tolist(), utility.tolist(), label="net utility", color="#2c7a4b", linewidth=2.4)
ax.axvline(float(strengths[best_index]), color="0.55", linestyle="--")
ax.set_title("Steering sweep")
ax.set_xlabel("steering strength")
ax.legend()
plt.tight_layout()

print("Best steering strength:", round(float(strengths[best_index]), 3))
print("Target gain there:", round(float(target_gain[best_index]), 3))
print("Off-target cost there:", round(float(off_target[best_index]), 3))
"""
    takeaway = """
## Takeaway

Steering becomes useful only when you can identify where benefit peaks before collateral effects dominate.
""" if language == "en" else """
## 小结

只有在你能找到收益先达到峰值、而副作用还没占上风的位置时，steering 才真正有用。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m06(language: str) -> list[dict]:
    intro = """
# M06 Tracing the Thoughts of a Large Language Model
""" if language == "en" else """
# M06 Tracing the Thoughts
"""
    context = """
## Build a toy trace, then compare it to a shared graph

Construct a tiny computation path locally, inspect which edges carry the answer, and then compare that pattern to the shared teaching artifact.
""" if language == "en" else """
## 先构造一个 toy trace，再对照共享图

先在本地构造一条极小计算路径，检查哪些边真正把答案送出来，再拿它和共享教学图对照。
"""
    code = repo_root_snippet() + """
import json
import math
import matplotlib.pyplot as plt
import numpy as np

tokens = ["Q", "3", "+", "4", "A"]
embeddings = np.array([
    [0.1, 0.0, 0.2],
    [1.2, 0.1, 0.0],
    [0.0, 0.2, 0.1],
    [0.9, 0.0, 0.2],
    [0.7, 0.4, 1.0],
])
Wq = np.array([[0.2, 0.7], [0.9, 0.1], [0.5, 0.6]])
Wk = np.array([[0.6, 0.3], [0.7, 0.2], [0.4, 0.8]])
Q = embeddings @ Wq
K = embeddings @ Wk
scores = Q[-1] @ K.T / math.sqrt(K.shape[-1])
weights = np.exp(scores - scores.max())
weights = weights / weights.sum()

number_values = np.array([0.0, 3.0, 0.0, 4.0, 0.0])
readout_weights = np.array([0.0, 1.0, 0.0, 1.0, 0.0])
token_contrib = weights * number_values * readout_weights
feature_scores = {
    "retrieve_left": token_contrib[1],
    "retrieve_right": token_contrib[3],
}
compose_score = sum(feature_scores.values())
toy_edges = [
    ("3", "retrieve_left", feature_scores["retrieve_left"]),
    ("4", "retrieve_right", feature_scores["retrieve_right"]),
    ("retrieve_left", "compose_sum", feature_scores["retrieve_left"]),
    ("retrieve_right", "compose_sum", feature_scores["retrieve_right"]),
    ("compose_sum", "answer=7", compose_score),
]

positions = {
    "3": (0.15, 0.75),
    "4": (0.15, 0.25),
    "retrieve_left": (0.45, 0.75),
    "retrieve_right": (0.45, 0.25),
    "compose_sum": (0.72, 0.5),
    "answer=7": (0.9, 0.5),
}

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
for source, target, score in toy_edges:
    x1, y1 = positions[source]
    x2, y2 = positions[target]
    axes[0].plot([x1, x2], [y1, y2], linewidth=2 + 6 * score, color="#c96a28", alpha=0.7)
for node, (x, y) in positions.items():
    color = "#123b63" if "retrieve" in node or "compose" in node else "#b5893a"
    axes[0].scatter(x, y, s=700, color=color)
    axes[0].text(x, y, node, ha="center", va="center", color="white", fontsize=8)
axes[0].set_title("Toy computation path")
axes[0].axis("off")

artifact = json.loads((root / "artifacts" / "m06_attribution_graph.json").read_text())
case = artifact["cases"][0]
artifact_scores = sorted((edge["score"] for edge in case["edges"]), reverse=True)
axes[1].bar(["left", "right", "sum"], [feature_scores["retrieve_left"], feature_scores["retrieve_right"], compose_score], color="#1f5f8b")
axes[1].plot(range(len(artifact_scores)), artifact_scores, marker="o", color="#c96a28")
axes[1].set_title("Toy scores vs artifact edge ordering")
axes[1].set_xlabel("ordered artifact edges")
plt.tight_layout()

print("Answer-position attention:", dict(zip(tokens, np.round(weights, 3))))
print("Toy path contributions:")
for source, target, score in toy_edges:
    print(f"  {source} -> {target}: {score:.3f}")

ablated_left = compose_score - feature_scores["retrieve_left"]
ablated_right = compose_score - feature_scores["retrieve_right"]
print("Compose score after ablating left retrieval:", round(float(ablated_left), 3))
print("Compose score after ablating right retrieval:", round(float(ablated_right), 3))
"""
    takeaway = """
## Takeaway

Tracing becomes legible when you can move between a locally computed path and a larger shared attribution graph.
""" if language == "en" else """
## 小结

当你能在“自己算出来的一条局部路径”和“更大的共享 attribution graph”之间来回切换时，tracing 才真正开始变得可读。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m07(language: str) -> list[dict]:
    intro = """
# M07 Open-sourcing Circuit Tracing Tools
""" if language == "en" else """
# M07 Circuit Tracing Tools
"""
    context = """
## Inspect the workflow behind the graph

Load the tracing workflow and compare it to the edge-score distribution in the shared attribution artifact.
""" if language == "en" else """
## 看图背后的工作流

加载 tracing 工作流，并把它和共享 attribution artifact 里的边分数分布对照起来。
"""
    code = repo_root_snippet() + """
import json
import matplotlib.pyplot as plt

workflow = json.loads((root / "artifacts" / "m07_tracing_tool_workflow.json").read_text())
graph = json.loads((root / "artifacts" / "m06_attribution_graph.json").read_text())
edge_scores = [edge["score"] for case in graph["cases"] for edge in case["edges"]]

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].bar(
    [step["title_en"] for step in workflow["steps"]],
    [step["estimated_minutes"] for step in workflow["steps"]],
    color="#1f5f8b",
)
axes[0].set_title("Workflow stages")
axes[0].tick_params(axis="x", rotation=24)

axes[1].hist(edge_scores, bins=6, color="#c96a28", edgecolor="white")
axes[1].set_title("Edge score distribution")
axes[1].set_xlabel("score")
plt.tight_layout()

print("Workflow outputs:")
for step in workflow["steps"]:
    print("-", step["title_en"], "->", step["output"], f"({step['estimated_minutes']} min)")
"""
    takeaway = """
## Takeaway

Tooling decides what traces are available, how expensive they are to produce, and how readable they become.
""" if language == "en" else """
## 小结

工具层会决定你能得到什么 trace、它们有多贵，以及最后到底好不好读。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m08(language: str) -> list[dict]:
    intro = """
# M08 Persona Vectors
""" if language == "en" else """
# M08 Persona Vectors
"""
    context = """
## Recover a toy persona direction, then compare it to the shared artifact

Construct a small persona direction from paired prompt embeddings, sweep the intervention strength, and then compare the result to the shared teaching artifact.
""" if language == "en" else """
## 先恢复一个 toy persona direction，再对照共享 artifact

先用成对 prompt embedding 恢复一个小型 persona direction，扫一遍干预强度，再与共享教学 artifact 对照。
"""
    code = repo_root_snippet() + """
import json
import math
import matplotlib.pyplot as plt
import numpy as np

payload = json.loads((root / "artifacts" / "m08_persona_vectors.json").read_text())
traits = ["helpful", "cautious", "concise"]

neutral = np.array([
    [0.48, 0.44, 0.53],
    [0.51, 0.41, 0.49],
    [0.46, 0.47, 0.55],
    [0.5, 0.43, 0.5],
])
mentor = neutral + np.array([0.18, 0.06, -0.03])
reviewer = neutral + np.array([0.04, 0.22, 0.15])

mentor_direction = (mentor - neutral).mean(axis=0)
mentor_direction = mentor_direction / np.linalg.norm(mentor_direction)
base_prompt = np.array([0.5, 0.4, 0.52])
strengths = np.linspace(0.0, 1.4, 8)
toy_scores = []
for strength in strengths:
    steered = base_prompt + strength * mentor_direction
    toy_scores.append(np.clip(steered, 0.0, 1.0))
toy_scores = np.array(toy_scores)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
for index, trait in enumerate(traits):
    axes[0].plot(strengths, toy_scores[:, index], marker="o", label=trait)
axes[0].set_title("Toy persona-direction sweep")
axes[0].set_xlabel("steering strength")
axes[0].set_ylim(0.0, 1.0)
axes[0].legend()

artifact_persona = payload["personas"][1]
before = [artifact_persona["scores_before"][trait] for trait in traits]
after = [artifact_persona["scores_after"][trait] for trait in traits]
x = range(len(traits))
axes[1].bar([index - 0.16 for index in x], before, width=0.32, label="before", color="#999999")
axes[1].bar([index + 0.16 for index in x], after, width=0.32, label="after", color="#1f5f8b")
axes[1].set_xticks(list(x))
axes[1].set_xticklabels(traits, rotation=20)
axes[1].set_ylim(0, 1)
axes[1].set_title(artifact_persona["label_en"])
axes[1].legend()
plt.tight_layout()

def cosine(values_a, values_b):
    numerator = sum(a * b for a, b in zip(values_a, values_b))
    denom = math.sqrt(sum(a * a for a in values_a) * sum(b * b for b in values_b))
    return numerator / denom

reference = payload["personas"][0]
for persona in payload["personas"][1:]:
    score = cosine(reference["vector"], persona["vector"])
    print(f"cosine({reference['label_en']}, {persona['label_en']}) = {score:.3f}")

artifact_vector = np.array(artifact_persona["vector"], dtype=float)
print("cosine(toy mentor direction, artifact mentor vector) =", round(cosine(mentor_direction, artifact_vector[:3]), 3))
print("Best toy strength by helpful-minus-concise tradeoff:", round(float(strengths[np.argmax(toy_scores[:, 0] - toy_scores[:, 2])]), 2))
"""
    takeaway = """
## Takeaway

Persona vectors become more believable once you can recover a direction locally and then compare it to a richer shared artifact.
""" if language == "en" else """
## 小结

当你先在本地恢复一个方向，再去对照更丰富的共享 artifact 时，persona vector 这件事才更像“可操作机制”，而不只是好看的图。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m09(language: str) -> list[dict]:
    intro = """
# M09 Signs of Introspection in Large Language Models
""" if language == "en" else """
# M09 Signs of Introspection
"""
    context = """
## Compare self-report and behavior

Load teaching cases and inspect where the model's self-description matches or diverges from observed behavior.
""" if language == "en" else """
## 对比 self-report 和行为

加载教学案例，观察模型对自身的描述和可观察行为在哪些地方一致、在哪些地方分叉。
"""
    code = repo_root_snippet() + """
import json
import matplotlib.pyplot as plt

payload = json.loads((root / "artifacts" / "m09_introspection_signals.json").read_text())
cases = payload["cases"]

fig, ax = plt.subplots(figsize=(7, 5))
for case in cases:
    ax.scatter(case["self_report"], case["behavior_signal"], s=160, color="#1f5f8b")
    ax.annotate(case["id"], (case["self_report"], case["behavior_signal"]))

ax.plot([0, 1], [0, 1], linestyle="--", color="0.6")
ax.set_xlim(0.3, 0.95)
ax.set_ylim(0.3, 0.95)
ax.set_xlabel("self-report signal")
ax.set_ylabel("behavior signal")
ax.set_title("Where self-report and behavior align")
plt.tight_layout()

print("Largest mismatches:")
for case in sorted(cases, key=lambda item: abs(item["self_report"] - item["behavior_signal"]), reverse=True):
    gap = abs(case["self_report"] - case["behavior_signal"])
    print("-", case["id"], "gap=", round(gap, 3))
"""
    takeaway = """
## Takeaway

The most informative cases are often the mismatches between self-description and behavior.
""" if language == "en" else """
## 小结

最值得盯住的，往往不是自我描述和行为一致的地方，而是它们错开的地方。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m10(language: str) -> list[dict]:
    intro = """
# M10 The Assistant Axis
""" if language == "en" else """
# M10 The Assistant Axis
"""
    context = """
## Project assistant styles onto one shared axis

Use a small teaching artifact to compare assistant variants by axis position, helpfulness, and safety.
""" if language == "en" else """
## 把不同 assistant 风格投到同一条轴上

用一个小型教学 artifact 比较不同 assistant 变体在轴位置、helpfulness 和 safety 上的差异。
"""
    code = repo_root_snippet() + """
import json
import matplotlib.pyplot as plt

payload = json.loads((root / "artifacts" / "m10_assistant_axis.json").read_text())
assistants = payload["assistants"]

fig, ax = plt.subplots(figsize=(8, 5))
for assistant in assistants:
    ax.scatter(
        assistant["axis_position"],
        assistant["helpfulness"],
        s=200 + assistant["safety"] * 120,
        color="#c96a28",
        alpha=0.8,
    )
    ax.annotate(assistant["label_en"], (assistant["axis_position"], assistant["helpfulness"]))

ax.set_xlabel("assistant-axis position")
ax.set_ylabel("helpfulness")
ax.set_title("Assistant variants in a shared frame")
ax.axvline(0, color="0.75", linewidth=1)
plt.tight_layout()

print("Ordered by axis position:")
for assistant in sorted(assistants, key=lambda item: item["axis_position"]):
    print("-", assistant["label_en"], "| axis =", assistant["axis_position"], "| safety =", assistant["safety"])
"""
    takeaway = """
## Takeaway

Stabilizing character means controlling a whole style manifold, not only one local trait.
""" if language == "en" else """
## 小结

稳定 character 的问题，不是只调一个局部 trait，而是要面对整块风格流形。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def x01(language: str) -> list[dict]:
    intro = """
# X01 A Mathematical Framework for Transformer Circuits
""" if language == "en" else """
# X01 Transformer Circuits 的数学框架
"""
    code = repo_root_snippet() + """
import matplotlib.pyplot as plt
import numpy as np

tokens = ["subject", "verb", "object"]
residual = np.array([
    [1.0, 0.2, 0.0],
    [0.3, 1.0, 0.1],
    [0.0, 0.4, 1.0],
])
attention_map = np.array([
    [0.0, 0.5, 0.0],
    [0.0, 0.0, 0.8],
    [0.7, 0.0, 0.0],
])
mlp_map = np.array([
    [0.2, 0.0, 0.1],
    [0.1, 0.3, 0.0],
    [0.0, 0.2, 0.4],
])
readout = np.array([
    [1.0, 0.2],
    [0.1, 0.9],
    [0.6, 0.4],
])

after_attention = residual + attention_map @ residual
after_mlp = after_attention + after_attention @ mlp_map
logits = after_mlp @ readout
composition_gain = logits - residual @ readout

fig, axes = plt.subplots(1, 3, figsize=(13, 4))
axes[0].imshow(residual, cmap="Blues")
axes[0].set_title("Residual stream")
axes[1].imshow(after_attention, cmap="Blues")
axes[1].set_title("After attention composition")
axes[2].imshow(after_mlp, cmap="Blues")
axes[2].set_title("After MLP composition")
for ax in axes:
    ax.set_xticks(range(3), tokens)
    ax.set_yticks(range(3), tokens)
plt.tight_layout()

print("Readout before composition:\\n", np.round(residual @ readout, 3))
print("Readout after composition:\\n", np.round(logits, 3))
print("Gain from composition:\\n", np.round(composition_gain, 3))
"""
    takeaway = """
## Takeaway

The point of the framework is not to list parts. It is to describe how information composes through the residual stream.
""" if language == "en" else """
## 小结

这篇的关键不是给部件起名字，而是学会用 residual stream 语言描述信息如何组合起来。
"""
    return [markdown_cell(intro), *extension_context_cells("X01", language), code_cell(code), markdown_cell(takeaway)]


def x02(language: str) -> list[dict]:
    intro = """
# X02 In-context Learning and Induction Heads
""" if language == "en" else """
# X02 In-context Learning 与 Induction Heads
"""
    code = repo_root_snippet() + """
import math
import matplotlib.pyplot as plt
import numpy as np

tokens = ["A", "B", "C", "A", "B", "?"]
prev_tokens = ["<bos>", "A", "B", "C", "A", "B"]
vocab = {"<bos>": [0, 0, 0], "A": [1, 0, 0], "B": [0, 1, 0], "C": [0, 0, 1]}
keys = np.array([vocab[token] for token in prev_tokens[:-1]], dtype=float)
values = np.array([vocab[token] for token in tokens[:-1]], dtype=float)
query = np.array(vocab[prev_tokens[-1]], dtype=float)

scores = 5.0 * (keys @ query) / math.sqrt(query.shape[0])
weights = np.exp(scores - scores.max())
weights = weights / weights.sum()
prediction = weights @ values
winner = ["A", "B", "C"][int(np.argmax(prediction))]

fig, ax = plt.subplots(figsize=(8, 3.5))
ax.bar(range(len(weights)), weights, color="#1f5f8b")
ax.set_xticks(range(len(weights)), [f"pos {i}:{token}" for i, token in enumerate(tokens[:-1])], rotation=20)
ax.set_ylabel("attention weight")
ax.set_title("Final query attends to earlier positions")
plt.tight_layout()

print("Final previous-token query:", prev_tokens[-1])
print("Predicted next-token vector:", np.round(prediction, 3))
print("Recovered token:", winner)
"""
    takeaway = """
## Takeaway

An induction pattern is more than a bright attention edge. It is a copy mechanism anchored to repeated context.
""" if language == "en" else """
## 小结

Induction 不只是“注意力亮了一下”，而是一个依赖重复上下文的复制机制。
"""
    return [markdown_cell(intro), *extension_context_cells("X02", language), code_cell(code), markdown_cell(takeaway)]


def x03(language: str) -> list[dict]:
    intro = """
# X03 IOI Circuit
""" if language == "en" else """
# X03 IOI 电路
"""
    code = repo_root_snippet() + """
import matplotlib.pyplot as plt
import numpy as np

roles = np.array([
    [1.0, 0.0],  # subject = Alice
    [0.0, 1.0],  # indirect object = Bob
])
name_labels = ["Alice", "Bob"]
duplicate_head = np.array([[0.0, 0.2], [0.1, 0.0]])
name_mover = np.array([[0.2, 0.0], [0.0, 1.3]])
subject_suppressor = np.array([[1.0, 0.0], [0.0, 0.1]])

baseline_scores = np.array([0.5, 0.5])
full_scores = baseline_scores + roles[1] @ name_mover - roles[0] @ subject_suppressor + roles[1] @ duplicate_head
ablations = {
    "full": full_scores,
    "without name mover": baseline_scores - roles[0] @ subject_suppressor + roles[1] @ duplicate_head,
    "without subject suppressor": baseline_scores + roles[1] @ name_mover + roles[1] @ duplicate_head,
    "without duplicate head": baseline_scores + roles[1] @ name_mover - roles[0] @ subject_suppressor,
}

fig, ax = plt.subplots(figsize=(9, 4))
positions = np.arange(len(ablations))
width = 0.35
for idx, name in enumerate(name_labels):
    ax.bar(
        positions + (idx - 0.5) * width,
        [scores[idx] for scores in ablations.values()],
        width=width,
        label=name,
    )
ax.set_xticks(positions, list(ablations.keys()), rotation=15)
ax.set_ylabel("final logit score")
ax.set_title("Teaching-scale IOI evidence chain")
ax.legend()
plt.tight_layout()

for label, scores in ablations.items():
    winner = name_labels[int(np.argmax(scores))]
    print(label, "->", winner, np.round(scores, 3))
"""
    takeaway = """
## Takeaway

Behavior-level circuit claims require ablations, not only one pretty path diagram.
""" if language == "en" else """
## 小结

到了行为层面的电路分析，不能只靠一张漂亮的路径图，还要靠消融来补证据。
"""
    return [markdown_cell(intro), *extension_context_cells("X03", language), code_cell(code), markdown_cell(takeaway)]


def x04(language: str) -> list[dict]:
    intro = """
# X04 Transformer Feed-Forward Layers Are Key-Value Memories
""" if language == "en" else """
# X04 Transformer Feed-Forward Layers Are Key-Value Memories
"""
    code = repo_root_snippet() + """
import matplotlib.pyplot as plt
import numpy as np

countries = ["France", "Germany", "Japan"]
cities = ["Paris", "Berlin", "Tokyo"]
keys = np.eye(3)
values = np.array([
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
])
query = np.array([1.0, 0.1, 0.0])
weights = np.exp(keys @ query)
weights = weights / weights.sum()
recalled = weights @ values

ablated_values = values.copy()
ablated_values[0] = 0.0
recalled_after_ablation = weights @ ablated_values

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].bar(countries, weights, color="#1f5f8b")
axes[0].set_title("Key match weights")
axes[1].bar(cities, recalled, color="#c96a28", alpha=0.85, label="full")
axes[1].bar(cities, recalled_after_ablation, color="#5d8c63", alpha=0.65, label="ablate France value")
axes[1].set_title("Recalled value distribution")
axes[1].legend()
plt.tight_layout()

print("Top recalled city before ablation:", cities[int(np.argmax(recalled))])
print("Top recalled city after ablation:", cities[int(np.argmax(recalled_after_ablation))])
"""
    takeaway = """
## Takeaway

The MLP-memory picture lets you ask where a fact is stored, not only which route carries it.
""" if language == "en" else """
## 小结

MLP memory 视角让你能问“事实存在哪里”，而不是只问“信息从哪条路流过去”。
"""
    return [markdown_cell(intro), *extension_context_cells("X04", language), code_cell(code), markdown_cell(takeaway)]


def x05(language: str) -> list[dict]:
    intro = """
# X05 Knowledge Neurons
""" if language == "en" else """
# X05 Knowledge Neurons
"""
    code = repo_root_snippet() + """
import torch
from torch import nn

prompts = torch.eye(4)
probe = prompts[0:1].clone().requires_grad_(True)
model = nn.Sequential(
    nn.Linear(4, 6),
    nn.ReLU(),
    nn.Linear(6, 4),
)
with torch.no_grad():
    model[0].weight.zero_()
    model[0].bias.zero_()
    model[0].weight[0, 0] = 4.0
    model[0].weight[1, 1] = 4.0
    model[0].weight[2, 2] = 4.0
    model[0].weight[3, 3] = 4.0
    model[2].weight.zero_()
    model[2].bias.zero_()
    model[2].weight[0, 0] = 2.5
    model[2].weight[1, 1] = 2.5
    model[2].weight[2, 2] = 2.5
    model[2].weight[3, 3] = 2.5
    model[2].weight[0, 4] = 0.4
    model[2].weight[1, 5] = 0.4

hidden = model[1](model[0](probe))
logits = model[2](hidden)
target_logit = logits[0, 0]
grads = torch.autograd.grad(target_logit, hidden)[0]
scores = (hidden * grads).detach().flatten()
top_idx = int(scores.abs().argmax())

with torch.no_grad():
    original = model(prompts[0:1]).softmax(dim=-1).flatten()
    hidden_ablated = hidden.detach().clone()
    hidden_ablated[0, top_idx] = 0.0
    ablated = model[2](hidden_ablated).softmax(dim=-1).flatten()

print("Knowledge-neuron scores:", [round(float(x), 4) for x in scores])
print("Top-scoring hidden unit:", top_idx)
print("Original distribution:", [round(float(x), 4) for x in original])
print("After ablating top unit:", [round(float(x), 4) for x in ablated])
"""
    takeaway = """
## Takeaway

A high-scoring neuron is evidence worth testing, not a free pass to a causal story.
""" if language == "en" else """
## 小结

高分 neuron 是值得继续检验的线索，不是自动成立的因果解释。
"""
    return [markdown_cell(intro), *extension_context_cells("X05", language), code_cell(code), markdown_cell(takeaway)]


def x06(language: str) -> list[dict]:
    intro = """
# X06 Locating and Editing Factual Associations in GPT
""" if language == "en" else """
# X06 Locating and Editing Factual Associations in GPT
"""
    code = repo_root_snippet() + """
import numpy as np

keys = np.eye(3)
cities = ["Paris", "Berlin", "Tokyo"]
W = np.eye(3)
france = keys[:, 0:1]
new_value = np.array([[0.0], [1.0], [0.0]])  # edit France -> Berlin in the toy
current_value = W @ france
delta = (new_value - current_value) @ (france.T / (france.T @ france).item())
W_edit = W + delta

for idx, country in enumerate(["France", "Germany", "Japan"]):
    query = keys[:, idx:idx+1]
    before = (W @ query).flatten()
    after = (W_edit @ query).flatten()
    print(country)
    print("  before:", {cities[i]: round(float(before[i]), 3) for i in range(3)})
    print("  after :", {cities[i]: round(float(after[i]), 3) for i in range(3)})
"""
    takeaway = """
## Takeaway

Editing is only interesting when you measure both success on the target and damage off the target.
""" if language == "en" else """
## 小结

只有同时衡量目标成功和非目标损伤，编辑实验才真正有研究价值。
"""
    return [markdown_cell(intro), *extension_context_cells("X06", language), code_cell(code), markdown_cell(takeaway)]


def x07(language: str) -> list[dict]:
    intro = """
# X07 Auditing Language Models for Hidden Objectives
""" if language == "en" else """
# X07 Auditing Language Models for Hidden Objectives
"""
    code = repo_root_snippet() + """
import matplotlib.pyplot as plt
import numpy as np

cases = ["harmless", "rewarding", "secret-risk", "high-pressure"]
helpfulness = np.array([0.8, 0.9, 0.5, 0.6])
hidden_objective = np.array([0.1, 0.2, 0.9, 0.8])
behavior_score = 0.7 * helpfulness - 0.4 * hidden_objective
internal_audit_signal = 0.2 * helpfulness + 0.9 * hidden_objective

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].bar(cases, behavior_score, color="#1f5f8b")
axes[0].set_title("Behavior metric")
axes[0].tick_params(axis="x", rotation=20)
axes[1].bar(cases, internal_audit_signal, color="#c96a28")
axes[1].set_title("Internal audit signal")
axes[1].tick_params(axis="x", rotation=20)
plt.tight_layout()

flagged = [case for case, signal in zip(cases, internal_audit_signal) if signal > 0.7]
print("Flagged by internal signal:", flagged)
print("Largest behavior drop case:", cases[int(np.argmin(behavior_score))])
"""
    takeaway = """
## Takeaway

Auditing becomes stronger when behavior evidence and internal evidence point at the same risk story.
""" if language == "en" else """
## 小结

当行为证据和内部证据指向同一个风险故事时，auditing 才真正形成闭环。
"""
    return [markdown_cell(intro), *extension_context_cells("X07", language), code_cell(code), markdown_cell(takeaway)]


NOTEBOOK_BUILDERS = {
    "M00": m00,
    "M01": m01,
    "M02": m02,
    "M03": m03,
    "M04": m04,
    "M05": m05,
    "M06": m06,
    "M07": m07,
    "M08": m08,
    "M09": m09,
    "M10": m10,
}

FOUNDATION_BUILDERS = {
    "F00": f00,
    "F01": f01,
    "F02": f02,
    "F03": f03,
}

EXTENSION_BUILDERS = {
    "X01": x01,
    "X02": x02,
    "X03": x03,
    "X04": x04,
    "X05": x05,
    "X06": x06,
    "X07": x07,
}


def write_notebook(path: Path, cells: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(notebook(cells), ensure_ascii=False, indent=2))


def clean_generated_notebooks() -> None:
    for language in ("en", "zh"):
        language_root = OUTPUT_ROOT / language
        language_root.mkdir(parents=True, exist_ok=True)
        for path in language_root.glob("m*.ipynb"):
            path.unlink()
        foundations_root = OUTPUT_ROOT / "foundations" / language
        foundations_root.mkdir(parents=True, exist_ok=True)
        for path in foundations_root.glob("f*.ipynb"):
            path.unlink()
        extensions_root = OUTPUT_ROOT / "extensions" / language
        extensions_root.mkdir(parents=True, exist_ok=True)
        for path in extensions_root.glob("x*.ipynb"):
            path.unlink()


def main() -> None:
    course = json.loads(COURSE_PATH.read_text())
    clean_generated_notebooks()
    for module in course:
        if not module["notebook_enabled"]:
            continue
        builder = NOTEBOOK_BUILDERS[module["id"]]
        filename = f"{module['id'].lower()}_{module['web_slug'].replace('-', '_')}.ipynb"
        for language in ("en", "zh"):
            path = OUTPUT_ROOT / language / filename
            cells = builder(language) + research_cells(module["id"], language) + self_check_cells(module["id"], language)
            write_notebook(path, cells)
            print(f"wrote {path.relative_to(ROOT)}")
    for foundation in FOUNDATIONS:
        builder = FOUNDATION_BUILDERS[foundation["id"]]
        filename = f"{foundation['id'].lower()}_{foundation['web_slug'].replace('-', '_')}.ipynb"
        for language in ("en", "zh"):
            path = OUTPUT_ROOT / "foundations" / language / filename
            cells = builder(language) + foundation_self_check_cells(foundation["id"], language)
            write_notebook(path, cells)
            print(f"wrote {path.relative_to(ROOT)}")
    for extension in EXTENSIONS:
        builder = EXTENSION_BUILDERS[extension["id"]]
        filename = f"{extension['id'].lower()}_{extension['notebook_slug']}.ipynb"
        for language in ("en", "zh"):
            path = OUTPUT_ROOT / "extensions" / language / filename
            cells = (
                builder(language)
                + extension_workflow_cells(extension["id"], language)
                + extension_self_check_cells(extension["id"], language)
            )
            write_notebook(path, cells)
            print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
