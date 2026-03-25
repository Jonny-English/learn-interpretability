#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "course.json"
OUTPUT_ROOT = ROOT / "notebooks"


def repo_root_snippet() -> str:
    return """from pathlib import Path

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


def m00(language: str) -> list[dict]:
    if language == "zh":
        intro = """
# M00 视觉电路热身

这一章复用原始 `Zoom In` 教程里最强的视觉直觉：神经元会偏好特定模式，多个神经元会组合成一个可读的电路。
"""
        context = """
## 本章你会做什么

- 重新浏览原始教程留下的 4 张关键图。
- 用最轻量的方式把 feature、circuit、universality 放在同一张桌子上。
- 为后面语言模型中的 superposition 和 feature tracing 建立直觉。
"""
        notes = """
## 继续阅读

- 长篇背景材料在 `notebooks/circuits_zoom_in_zh.ipynb`
- 对应讲义在 `docs/zh/modules/m00-vision-circuits.md`
"""
    else:
        intro = """
# M00 Vision Circuits Warm-up

This module reuses the strongest intuition from the original `Zoom In` tutorial: neurons can prefer recognizable patterns, and multiple neurons can combine into an interpretable circuit.
"""
        context = """
## What you will do

- Revisit the four key figures from the original tutorial.
- Put features, circuits, and universality on one page.
- Build the intuition that later gets complicated by superposition and feature tracing.
"""
        notes = """
## Continue from here

- The long-form background notebook is `notebooks/circuits_zoom_in_en.ipynb`
- The matching concept note is `docs/en/modules/m00-vision-circuits.md`
"""
    code = f"""{repo_root_snippet()}
import matplotlib.pyplot as plt
from PIL import Image

figure_specs = [
    ("feature_viz_grid.png", "Feature visualization"),
    ("polar_tuning.png", "Orientation tuning"),
    ("circuit_diagram.png", "Circuit composition"),
    ("universality_comparison.png", "Universality"),
]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, (filename, title) in zip(axes.flatten(), figure_specs):
    image = Image.open(root / "figures" / filename)
    ax.imshow(image)
    ax.set_title(title)
    ax.axis("off")

plt.tight_layout()
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(notes)]


def m01(language: str) -> list[dict]:
    intro = """
# M01 Superposition
""" if language == "en" else """
# M01 Superposition
"""
    description = """
## Toy setup

We compress four sparse concepts into a two-dimensional hidden space. Reconstruction can stay good even while concepts overlap in the hidden plane.
""" if language == "en" else """
## Toy 设定

我们把 4 个稀疏概念压进 2 维隐藏空间。即使隐藏平面发生重叠，重建依然可能很好。
"""
    code = """import torch
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

The hidden space is smaller than the concept set, so the model is forced to pack multiple ideas together. That is the basic pressure behind superposition.
""" if language == "en" else """
## 小结

隐藏空间比概念集合更小，于是模型只能把多个概念塞进同一片区域里。这就是 superposition 的基本压力来源。
"""
    return [markdown_cell(intro), markdown_cell(description), code_cell(code), markdown_cell(takeaway)]


def m02(language: str) -> list[dict]:
    intro = """
# M02 Monosemantic Features and Dictionary Learning
""" if language == "en" else """
# M02 单语义特征与字典学习
"""
    description = """
## Sparse autoencoder toy lab

We generate activations from a hidden dictionary, then train a tiny sparse autoencoder to recover reusable directions.
""" if language == "en" else """
## Sparse autoencoder 教学实验

我们先用一个隐藏字典生成激活，再训练一个小型 sparse autoencoder 去恢复可复用方向。
"""
    code = """import torch
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

The recovered directions are not perfect copies of the planted dictionary, but they are reusable, sparse, and much easier to reason about than raw neurons.
""" if language == "en" else """
## 小结

恢复出来的方向不会完美等于我们埋进去的字典，但它们已经比原始神经元更可复用、更稀疏，也更容易讲清楚。
"""
    return [markdown_cell(intro), markdown_cell(description), code_cell(code), markdown_cell(takeaway)]


def m03(language: str) -> list[dict]:
    intro = """
# M03 Feature Probes and Steering
""" if language == "en" else """
# M03 特征探针与 Steering
"""
    description = """
## Probe first, then intervene

We create synthetic feature activations, train a tiny classifier on them, and then add a steering vector to see how the prediction moves.
""" if language == "en" else """
## 先 probe，再 intervention

我们先构造 synthetic feature activation，在其上训练一个小分类器，再加上 steering vector 看输出如何移动。
"""
    code = """import torch
import matplotlib.pyplot as plt

torch.manual_seed(23)

feature_names = ["helpful", "cautious", "concise"]
features = torch.randn(300, 3)
logits_target = 1.2 * features[:, 0] - 0.8 * features[:, 1] + 0.4 * features[:, 2]
labels = (torch.sigmoid(logits_target) > 0.5).float().unsqueeze(1)

probe = torch.nn.Linear(3, 1)
optimizer = torch.optim.Adam(probe.parameters(), lr=0.05)

for step in range(500):
    logits = probe(features)
    loss = torch.nn.functional.binary_cross_entropy_with_logits(logits, labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

weights = probe.weight.detach().flatten()
steering_vector = torch.tensor([0.7, 0.15, -0.1])
example = torch.tensor([[0.1, 0.35, 0.2]])
before = torch.sigmoid(probe(example)).item()
after = torch.sigmoid(probe(example + 0.8 * steering_vector)).item()

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].bar(feature_names, weights.tolist(), color=["#1f77b4", "#ff7f0e", "#2ca02c"])
axes[0].set_title("Learned probe weights")
axes[0].axhline(0, color="0.75", linewidth=1)

axes[1].bar(["before", "after"], [before, after], color=["#666666", "#c44e52"])
axes[1].set_ylim(0, 1)
axes[1].set_title("Prediction shift under steering")
plt.tight_layout()

print("Final BCE loss:", float(loss.detach()))
print("Probe weights:", dict(zip(feature_names, [round(v, 3) for v in weights.tolist()])))
print("Example score before steering:", round(before, 3))
print("Example score after steering:", round(after, 3))
"""
    takeaway = """
## Takeaway

Features become actionable once they support both a readable probe and a controlled intervention. The shift is useful, but it is never free of side effects.
""" if language == "en" else """
## 小结

当 feature 既能提供可读 probe，又能支撑可控 intervention 时，它才真正成为“可操作单位”。但任何偏移都不可能没有副作用。
"""
    return [markdown_cell(intro), markdown_cell(description), code_cell(code), markdown_cell(takeaway)]


def m04(language: str) -> list[dict]:
    intro = """
# M04 Circuit Tracing
""" if language == "en" else """
# M04 Circuit Tracing
"""
    description = """
## Read a precomputed attribution graph

This notebook loads a teaching artifact and turns it into a visible path: input nodes, intermediate features, and the output token.
""" if language == "en" else """
## 阅读一个预计算 attribution graph

这一章直接加载教学 artifact，把输入节点、中间特征和输出 token 变成可见路径。
"""
    code = f"""{repo_root_snippet()}
import json
import matplotlib.pyplot as plt

graph = json.loads((root / "artifacts" / "m04_attribution_graph.json").read_text())
case = graph["cases"][0]

fig, ax = plt.subplots(figsize=(10, 4))
for edge in case["edges"]:
    source = next(node for node in case["nodes"] if node["id"] == edge["source"])
    target = next(node for node in case["nodes"] if node["id"] == edge["target"])
    ax.plot(
        [source["x"], target["x"]],
        [source["y"], target["y"]],
        linewidth=2 + 4 * edge["score"],
        color="#c44e52",
        alpha=0.6,
    )

for node in case["nodes"]:
    ax.scatter(node["x"], node["y"], s=700, color="#1f4b99" if node["kind"] == "feature" else "#d9a441")
    ax.text(node["x"], node["y"], node["label_en"], ha="center", va="center", color="white", fontsize=9)

ax.set_title(case["title_en"])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
plt.tight_layout()

sorted_edges = sorted(case["edges"], key=lambda edge: edge["score"], reverse=True)
print("Top contributions:")
for edge in sorted_edges:
    print(f"  {{edge['source']}} -> {{edge['target']}}: {{edge['score']:.2f}}")
"""
    takeaway = """
## Takeaway

Tracing is less about dumping the whole network and more about choosing a faithful, small slice of the computation to inspect.
""" if language == "en" else """
## 小结

tracing 的重点不是把整张网络都摊开，而是挑出一块足够忠实、又足够小的计算切片来阅读。
"""
    return [markdown_cell(intro), markdown_cell(description), code_cell(code), markdown_cell(takeaway)]


def m05(language: str) -> list[dict]:
    intro = """
# M05 Character and Control
""" if language == "en" else """
# M05 Character and Control
"""
    description = """
## Persona-vector walkthrough

We inspect a small teaching artifact that records before/after trait scores under light steering.
""" if language == "en" else """
## Persona vector 演示

我们读取一个小型教学 artifact，观察在轻量 steering 前后，trait score 如何变化。
"""
    code = f"""{repo_root_snippet()}
import json
import math
import matplotlib.pyplot as plt

payload = json.loads((root / "artifacts" / "m05_persona_vectors.json").read_text())
traits = ["helpful", "cautious", "concise"]

fig, axes = plt.subplots(1, len(payload["personas"]), figsize=(12, 4), sharey=True)
for ax, persona in zip(axes, payload["personas"]):
    before = [persona["scores_before"][trait] for trait in traits]
    after = [persona["scores_after"][trait] for trait in traits]
    x = range(len(traits))
    ax.bar([index - 0.16 for index in x], before, width=0.32, label="before", color="#999999")
    ax.bar([index + 0.16 for index in x], after, width=0.32, label="after", color="#2c7fb8")
    ax.set_xticks(list(x))
    ax.set_xticklabels(traits, rotation=20)
    ax.set_ylim(0, 1)
    ax.set_title(persona["label_en"])

axes[0].legend()
plt.tight_layout()

def cosine(values_a, values_b):
    numerator = sum(a * b for a, b in zip(values_a, values_b))
    denom = math.sqrt(sum(a * a for a in values_a) * sum(b * b for b in values_b))
    return numerator / denom

reference = payload["personas"][0]
for persona in payload["personas"][1:]:
    score = cosine(reference["vector"], persona["vector"])
    print(f"cosine({{reference['label_en']}}, {{persona['label_en']}}) = {{score:.3f}}")

print("\\nSample prompt shifts:")
for prompt in payload["prompts"]:
    print("-", prompt["prompt"])
    print("  before:", prompt["response_before"])
    print("  after :", prompt["response_after"])
"""
    takeaway = """
## Takeaway

Persona vectors are useful teaching objects because they sit at the border between interpretability and control. They help us reason about behavior without pretending that behavior is fully solved.
""" if language == "en" else """
## 小结

persona vector 很适合做教学对象，因为它正好站在 interpretability 和 control 的边界上：既能帮助我们理解行为，又不会假装行为问题已经被解决。
"""
    return [markdown_cell(intro), markdown_cell(description), code_cell(code), markdown_cell(takeaway)]


NOTEBOOK_BUILDERS = {
    "M00": m00,
    "M01": m01,
    "M02": m02,
    "M03": m03,
    "M04": m04,
    "M05": m05,
}


def write_notebook(path: Path, cells: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(notebook(cells), ensure_ascii=False, indent=2))


def main() -> None:
    course = json.loads(COURSE_PATH.read_text())
    for module in course:
        builder = NOTEBOOK_BUILDERS[module["id"]]
        filename = f"{module['id'].lower()}_{module['web_slug'].replace('-', '_')}.ipynb"
        for language in ("en", "zh"):
            path = OUTPUT_ROOT / language / filename
            write_notebook(path, builder(language))
            print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
