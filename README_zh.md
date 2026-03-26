# Learn Interpretability

[**English README**](README.md) ·
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ·
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

`Learn Interpretability` 是一个面向有基础 Python / PyTorch 读者的双语、Colab 优先 interpretability 训练仓库。项目按“论文驱动、live code 优先”来组织：每篇主线论文都有镜像讲义，凡是能诚实实时运行的条目，都配一份独立 Colab notebook。

如果这个仓库确实帮你节省了时间、给了清晰路径，或者让你不再随机跳论文，就给它一个 star。

## 序言

这个项目从一个很简单的拒绝开始：
我们不愿意在大模型时代，只做那些自己并不真正理解之物的被动使用者。

这个时代最重要的技术，正在变得更强、更像行动者，也更深地嵌进研究、软件和决策流程里。如果我们学到的只是在外面调用它、消费它、绕着它做工作流，那我们始终站在真正问题的下游。真正的问题是：这些模型内部到底表示了什么、依靠了什么机制、会在什么地方失效，以及人类怎样才能仍然有资格去理解它、干预它、控制它。

所以这个仓库不是单纯的论文目录，也不是一堆 notebook 的堆砌。它是一块训练场。它写给那些不满足于站在黑箱外面惊叹的人，写给那些愿意亲手打开它、复现它、追踪它、记录判断，并把零散好奇心压成研究能力的人。

你不需要一开始就是专家。
但你需要从一开始就认真。

## 从这里开始

- notebook、图表、实验纪律还不稳：先做 `F00 -> F03`
- 已经会基本 PyTorch 和 notebook：直接走 live 主线 `M00 -> M05`
- 还不确定这个仓库适不适合你：先看[第一周验证路径](docs/zh/program/first-week-checklist.md)
- 你的目标是完整结果而不是只跑几本 Colab：先读 [research-ready.md](docs/zh/program/research-ready.md) 和 [p6-graduation-checklist.md](docs/zh/program/p6-graduation-checklist.md)

## 这个仓库承诺什么

- `双语镜像`：英文和中文保持结构对齐
- `Colab 优先`：主 runnable 路径按 CPU 或免费 Colab 设计
- `只认 live code`：运行时实时产出结果的才算 runnable；其他一律标成 `reading-only`
- `P6-ready 目标`：诚实说法不是“跑几个 notebook 就毕业”，而是“普通本科生在完成完整路径和证据门槛后，可以达到可信的 `P6-ready`”

## 仓库快照

- `4` 个基础 lab
- `5` 个 live 主线 notebook
- `7` 个可运行扩展方法练习
- `32` 本 notebook 通过 smoke test
- 完整 `P6-ready` 路径建议投入 `180-250` 小时

## 基础包

如果环境、图表、attention 读图或实验纪律还不稳，就先补这里。

<!-- FOUNDATION_TABLE:START -->
| ID | 基础 Lab | Notebook | Colab | 运行层级 | 你会补齐什么 |
|---|---|---|---|---|---|
| `F00` | 环境、图表与基线纪律 | [打开](notebooks/foundations/zh/f00_environment_plots_baselines.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/foundations/zh/f00_environment_plots_baselines.ipynb) | `cpu-colab` | 建立本地/Colab 工作流，学会读 loss 曲线，并理解 baseline、variant 与日志记录的最小纪律。 |
| `F01` | Transformer 形状与注意力读图 | [打开](notebooks/foundations/zh/f01_transformer_shapes_attention.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/foundations/zh/f01_transformer_shapes_attention.ipynb) | `cpu-colab` | 用一个极小 attention 例子掌握 token、head、QK 打分、softmax 和 residual update 的形状感。 |
| `F02` | 向量几何、特征与探针 | [打开](notebooks/foundations/zh/f02_vector_geometry_features_probes.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/foundations/zh/f02_vector_geometry_features_probes.ipynb) | `cpu-colab` | 在二维和高维 toy 向量上练习 cosine、投影、方向相似和线性 probe，给 feature 语言补上几何底座。 |
| `F03` | Sweep、Ablation 与 Failure Analysis | [打开](notebooks/foundations/zh/f03_sweeps_ablations_failure_analysis.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/foundations/zh/f03_sweeps_ablations_failure_analysis.ipynb) | `cpu-colab` | 用一个小实验练习 sweep、ablation、停止条件和 failure analysis，把“会跑 notebook”推进到“会设计最小实验”。 |
<!-- FOUNDATION_TABLE:END -->

## 主线论文路径

这是项目的主文章路径。`reading-only` 的意思是：讲义保留，但 notebook 不生成，因为它达不到严格 live-code 规则。

<!-- COURSE_TABLE:START -->
| ID | 文章 | 日期 | 状态 | Notebook | Colab | 运行层级 | 你会做什么 |
|---|---|---|---|---|---|---|---|
| `M00` | Zoom In：电路入门 | `2020-03-10` | `method-lab` | [打开](notebooks/zh/m00_zoom_in_circuits.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/m00_zoom_in_circuits.ipynb) | `cpu-colab` | 在公开 InceptionV1 上实时生成 feature visualization、真实图片验证、方向调谐与小型 circuit trace。 |
| `M01` | Toy Models of Superposition | `2022-09-14` | `paper-faithful` | [打开](notebooks/zh/m01_toy_models_superposition.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/m01_toy_models_superposition.ipynb) | `cpu-colab` | 用最小 toy model 理解为什么神经元会混装多个语义。 |
| `M02` | Towards Monosemanticity | `2023-10-05` | `method-lab` | [打开](notebooks/zh/m02_towards_monosemanticity.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/m02_towards_monosemanticity.ipynb) | `cpu-colab` | 通过教学版 sparse autoencoder 理解为什么 feature 视角比 neuron 视角更稳。 |
| `M03` | Mapping the Mind | `2024-05-21` | `reading-only` | 阅读 | - | `reading-only` | 浏览教学版 feature catalog，理解“发现大量特征”到底意味着什么。 |
| `M04` | Features as Classifiers | `2024-10-16` | `method-lab` | [打开](notebooks/zh/m04_features_as_classifiers.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/m04_features_as_classifiers.ipynb) | `cpu-colab` | 把 feature 当成分类器输入，理解“读出”能力从哪里来。 |
| `M05` | Evaluating Feature Steering | `2024-10-25` | `method-lab` | [打开](notebooks/zh/m05_evaluating_feature_steering.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/m05_evaluating_feature_steering.ipynb) | `cpu-colab` | 扫描 steering 强度，观察 target gain、sweet spot 与 off-target cost 的平衡。 |
| `M06` | Tracing the Thoughts | `2025-03-27` | `reading-only` | 阅读 | - | `reading-only` | 阅读共享 attribution graph，学会描述一条局部计算路径以及实时复现还缺哪些公开工具。 |
| `M07` | Circuit Tracing Tools | `2025-05-29` | `reading-only` | 阅读 | - | `reading-only` | 查看 tracing artifact 与工作流拆解，理解工具层如何支撑分析。 |
| `M08` | Persona Vectors | `2025-08-01` | `reading-only` | 阅读 | - | `reading-only` | 阅读共享 persona artifact，比较 trait 前后变化，并说明诚实的实时复现还缺什么。 |
| `M09` | Signs of Introspection | `2025-10-29` | `reading-only` | 阅读 | - | `reading-only` | 用教学数据对比 self-report 与行为信号，讨论“内省迹象”到底意味着什么。 |
| `M10` | The Assistant Axis | `2026-01-19` | `reading-only` | 阅读 | - | `reading-only` | 把不同 assistant 风格投到同一条轴上，观察 character 稳定化问题。 |
<!-- COURSE_TABLE:END -->

## Research-Ready 层

如果你的目标已经从“我看懂了”变成“我能像一个入门研究者那样工作”，就开始用这些文档。

- [研究就绪总览](docs/zh/program/research-ready.md)
- [第一周验证路径](docs/zh/program/first-week-checklist.md)
- [能力成长弧线与 P6 证据门槛](docs/zh/program/capability-arc.md)
- [P6 毕业清单](docs/zh/program/p6-graduation-checklist.md)
- [12 周训练营](docs/zh/program/week-by-week.md)
- [研究工作流](docs/zh/program/research-playbook.md)
- [独立研究冲刺](docs/zh/program/independent-sprints.md)

## 参考输出

当你需要判断自己的 notes、logs、proposal 密度够不够时，就看这里。

<!-- REFERENCE_TABLE:START -->
| ID | 参考输出 | 文件 | 什么时候用 |
|---|---|---|---|
| `R01` | 参考论文简报 | [examples/zh/reference_paper_brief.md](examples/zh/reference_paper_brief.md) | 用在独立研究冲刺任务 T1 或任何 paper reading note 之后的压缩写作。 |
| `R02` | 参考实验日志 | [examples/zh/reference_experiment_log.md](examples/zh/reference_experiment_log.md) | 用在任何 sweep、ablation 或 feature-steering notebook 之后。 |
| `R03` | 参考 Artifact Critique | [examples/zh/reference_artifact_critique.md](examples/zh/reference_artifact_critique.md) | 用在 M03、M07、M09、M10 或独立研究冲刺任务 T3。 |
| `R04` | 参考两周提案 | [examples/zh/reference_two_week_proposal.md](examples/zh/reference_two_week_proposal.md) | 用在 capstone 或独立研究冲刺任务 T4 之前校准自己的提案密度。 |
<!-- REFERENCE_TABLE:END -->

## 扩展轨道

只做 Anthropic 主线还不够。主线之后继续进入 transformer circuits、memory/editing 和 auditing 方向。完整顺序看 [docs/zh/extensions/index.md](docs/zh/extensions/index.md)。

<!-- EXTENSION_TABLE:START -->
| ID | 扩展论文 | 状态 | 讲义 | Notebook | Colab |
|---|---|---|---|---|---|
| `X01` | A Mathematical Framework for Transformer Circuits | `method-lab` | [讲义](docs/zh/extensions/x01-transformer-circuits-framework.md) | [打开](notebooks/extensions/zh/x01_transformer_circuits_framework.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/zh/x01_transformer_circuits_framework.ipynb) |
| `X02` | In-context Learning and Induction Heads | `method-lab` | [讲义](docs/zh/extensions/x02-induction-heads.md) | [打开](notebooks/extensions/zh/x02_induction_heads.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/zh/x02_induction_heads.ipynb) |
| `X03` | Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 Small | `method-lab` | [讲义](docs/zh/extensions/x03-ioi-circuit.md) | [打开](notebooks/extensions/zh/x03_ioi_circuit.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/zh/x03_ioi_circuit.ipynb) |
| `X04` | Transformer Feed-Forward Layers Are Key-Value Memories | `method-lab` | [讲义](docs/zh/extensions/x04-ffn-key-value-memories.md) | [打开](notebooks/extensions/zh/x04_ffn_key_value_memories.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/zh/x04_ffn_key_value_memories.ipynb) |
| `X05` | Knowledge Neurons in Pretrained Transformers | `method-lab` | [讲义](docs/zh/extensions/x05-knowledge-neurons.md) | [打开](notebooks/extensions/zh/x05_knowledge_neurons.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/zh/x05_knowledge_neurons.ipynb) |
| `X06` | Locating and Editing Factual Associations in GPT | `method-lab` | [讲义](docs/zh/extensions/x06-rome-factual-editing.md) | [打开](notebooks/extensions/zh/x06_rome_factual_editing.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/zh/x06_rome_factual_editing.ipynb) |
| `X07` | Auditing Language Models for Hidden Objectives | `method-lab` | [讲义](docs/zh/extensions/x07-auditing-hidden-objectives.md) | [打开](notebooks/extensions/zh/x07_auditing_hidden_objectives.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/zh/x07_auditing_hidden_objectives.ipynb) |
<!-- EXTENSION_TABLE:END -->

## 本地工作流

```bash
pip install -r requirements.txt
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py
python3 scripts/validate_course.py
python3 scripts/audit_realtime_policy.py
python3 scripts/check_links.py
python3 scripts/smoke_notebooks.py
```

如果你只是来学习，直接点上面的 Colab 链接就行，本地环境可以后面再配。

## 项目导航

- [英文 docs 索引](docs/en/index.md)
- [中文 docs 索引](docs/zh/index.md)
- [英文仓库地图](docs/en/repo-map.md)
- [中文仓库地图](docs/zh/repo-map.md)

## 许可证

[MIT](LICENSE)
