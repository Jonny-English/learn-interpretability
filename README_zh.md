# Learn Interpretability

[**English README**](README.md) ·
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

`Learn Interpretability` 是一个面向初学者的双语、Colab 优先 interpretability 训练项目。仓库现在改成了“论文复现优先”结构：核心路径里的每一篇论文，都有一份同步讲义；凡是能诚实实时复现的论文，再配一份独立 Colab notebook。

如果这个仓库帮你省掉了大量零散找论文、找复现、找路径的时间，或者确实帮你建立了靠谱的 interpretability 学习习惯，请给它一个 star。

## 为什么这个仓库值得点开

- 你不需要先有 interpretability 背景；它就是按“会基础 Python/PyTorch 的小白”来设计的。
- 你可以在第一轮学习里就打开真实 Colab，而不是先看几个小时材料再碰代码。
- live-code 边界写得很清楚：能跑的就是能跑，不能诚实实时跑的就标成 `reading-only`。
- 长期承诺也不是空话：完整路径瞄准的是可信的 `P6-ready`，不是“看过不少内容”。

## 仓库快照

- `4` 个基础 lab，补环境、图表、attention 读图和实验纪律
- `5` 个严格可运行的主线 notebook：`M00`、`M01`、`M02`、`M04`、`M05`
- `7` 个主线后的扩展方法练习
- 当前仓库里有 `32` 本 notebook 通过 smoke test
- 完整 `P6-ready` 路径建议投入 `180-250` 小时

## 快速回答

- `需要 GPU 吗？` 不需要。当前 live 路径按 CPU 或免费 Colab 设计。
- `需要 interpretability 基础吗？` 不需要。你需要的是基础 Python/PyTorch，以及愿意写笔记和实验记录。
- `多快能知道这个仓库适不适合我？` 一般第一个周末试完 `F00`、`M00`、`M01` 就能判断。
- `仓库是不是承诺我自动变成 P6？` 不是。只有完整跑完路径并通过证据门槛，仓库才会把结果叫做 `P6-ready`。

## 第一小时直接试

- `30-45 分钟`：[F00 Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/foundations/zh/f00_environment_plots_baselines.ipynb)
  搭好 Colab 工作流，读一张 loss 曲线，搞清 baseline 是什么。
- `45-60 分钟`：[M00 Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/m00_zoom_in_circuits.ipynb)
  用视觉模型建立 feature、circuit、intervention 的第一层直觉。
- `60-90 分钟`：[M01 Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/m01_toy_models_superposition.ipynb)
  跑第一篇真正有“论文形状”的复现，看清为什么神经元会混装多个语义。

如果你想在投入完整路径之前先做一次更严格的适配验证，就看这份[第一周验证路径](docs/zh/program/first-week-checklist.md)。

## 从这里开始

- 如果你对 notebook 环境、图表或实验纪律还不稳，先做 `F00 -> F03`。
- 如果你已经能跑 notebook，也会基本 PyTorch，就直接进入 live 主线：`M00 -> M05`。
- 如果你的目标是完整的 `P6-ready` 路径，开始前先读 [docs/zh/program/research-ready.md](docs/zh/program/research-ready.md) 和 [docs/zh/program/p6-graduation-checklist.md](docs/zh/program/p6-graduation-checklist.md)。
- 如果你更想看英文镜像路径，就从 [README.md](README.md) 和 [docs/en/index.md](docs/en/index.md) 进入。

仓库由三层核心同步层组成：

- `content/course.json`：顺序、先修关系、论文链接和 artifact 引用的唯一真相源。
- `docs/zh` 与 `docs/en`：结构完全镜像的文章讲义。
- `notebooks/zh` 与 `notebooks/en`：结构完全镜像的文章 notebook；只有可运行条目才生成 live notebook，`reading-only` 条目不会生成 notebook。

现在仓库还多了四层强化内容：

- `Pre-P4 基础包`：补环境、attention 形状感、向量几何和实验纪律。
- `research-ready path`：12 周训练营、memo 模板、rubric 和独立研究冲刺任务。
- `参考答案层`：用样例校准输出密度。
- `扩展论文复现轨道`：用更多 Colab 复现，把视野扩到 Anthropic 主线之外。

这些层的目的，是避免自学里最常见的失败模式：内容看完了，但复现习惯、写作习惯和研究判断都没有建立起来。

从现在起增加一条硬规则：

- 只有运行时实时产生输出的代码，才算可运行内容
- 凡是仍然依赖预计算 JSON artifact 的部分，一律降级成 `reading-only`
- 即使有简化版 live notebook，也只能叫 `method-lab`，不能再包装成完整论文复现

## 这个项目适合谁

- 适合有基础 Python / PyTorch，但几乎没有 mechanistic interpretability 背景的小白。
- 适合想从“能看懂一点论文”升级到“能在 Colab 里复现论文、批判论文，并最终承担一条明确 interpretability 研究线”的读者。
- 不适合把它当成纯浏览型科普。它要求你写 reading note、experiment log 和 memo。

这个项目的目标产出不是“看过很多论文的人”，而是帮助一个认真完成它的本科生或个人研究者达到这里描述的阿里式 `P6`：能承担明确研究任务、批判证据，并提出下一步实验。

这里直接改成更接近阿里巴巴技术岗常见理解的 `P4-P12` 说法：

| 等级 | 对应能力 |
|---|---|
| `P4` | 校招生 / 初级工程师水平：能在明确指导下完成环境搭建、跑通 notebook、复述概念，但独立研究判断还很弱。 |
| `P5` | 工程师水平：能独立完成小范围复现、记录实验、比较 baseline 与 variant，并写出基本结论。 |
| `P6` | 高级工程师 / 资深 IC 起步水平：能在实验室、读书小组或个人项目里承担明确研究任务，完成读论文、复现、批判、提出下一步实验。 |
| `P7` | 专家水平：能独立定义一个小方向、设计两周级研究计划，并把实验、工具和汇报串成闭环。 |
| `**P8**` | 高级专家水平：能负责一个研究子方向或工具线，对多名研究工程师形成稳定技术带动。 |
| `P9` | 资深专家 / Principal 水平：能定义中期研究主题，影响多个团队的判断、方法和协作方式。 |
| `P10` | 研究 Fellow / 组织级专家水平：能主导组织级研究方向，决定关键方法路线，并影响产品与安全策略。 |
| `P11` | 公司级顶层技术负责人水平：能定义长期 agenda、技术标准和人才体系。 |
| `P12` | 行业级顶尖人物水平：能显著改变整个行业对技术路线和问题框架的理解。 |

如果按这个尺度说，`P6` 以上的行更多是背景参照，不是这个仓库的直接完成承诺。更诚实的说法是：如果一个普通本科生认真完成整套项目，包括扩展复现和证据门槛，把结果描述成 `P6-ready` 是合理的。

更准确的理解应该是分阶段推进：

- `F00-F03` 加早期主线，把“还没进入 `P4` 状态”的小白推进到 `P4/P5`。
- `M00-M10` 加上 research-ready bootcamp，构成 `P6-ready` 路径里的核心学徒阶段。
- 至少 3 篇扩展复现，再加 dossier、memo、critique 和 proposal 这些门槛，才足以让仓库把结果叫做 `P6-ready`。
- `X01-X07` 的完整轨道、反复做 capstone、接受外部反馈和累计作品集，则进一步把这块 `P6` 地板打深，并帮助强完成者开始往早期 `P7` 走。
- `P8` 需要多年原创工作和协作者层面的技术带动，不属于这个仓库的直接承诺。

所以这个项目应该按“能不能让一个普通本科生在完整项目下诚实达到 `P6-ready`”来评估，而不是按“能不能直接产出 `P8`”来评估。在严格规则下，只有 `paper-faithful` 和 `method-lab` 状态的条目才算 live code。

## 两条起跑线

为了同时服务小白和有一定基础的读者，这个项目现在明确提供两条起跑线：

### 小白起跑线

- 适合：会一点 Python，但环境、数学、实验记录都还不稳定的人。
- 进入信号：你还不能稳定跑 notebook、看懂基础图表，或者还说不清 baseline 是什么。
- 建议走法：先完成 `F00-F03` 和 `M00`、`M01`，把 reading note 和 experiment log 模板用熟，再进入完整课程和后续扩展复现。
- 目标：先把自己推进到接近阿里式 `P4`，再借助主线、bootcamp 和扩展轨道进入可信的 `P6-ready` 状态。

### 基础者起跑线

- 适合：已经能跑 notebook、会基本 PyTorch、能看懂常见图表，但还没有系统 interpretability 路线的人。
- 进入信号：你已经能独立做简单复现、写基础笔记，只是缺一条完整主线。
- 建议走法：先快速完成可运行的 `M00 → M05` 主线，再把 `M03` 和 `M06-M10` 当成阅读与批判任务插入，然后尽早进入 research-ready 模式，开始写 memo、failure analysis 和扩展复现。
- 目标：直接进入完整的 `P6-ready` 路径，而不是停在“我把 notebook 跑通了”。

## 为什么要学这个

珍妮纺纱机出现之后，行业竞争的重点就不再是“谁的手工纺纱动作更熟练”，而转向了：

- 谁更理解机器原理
- 谁更会使用机器
- 谁更会改造机器
- 谁更会围绕机器组织新的生产流程

大模型时代也一样。

当模型已经能自动完成大量局部认知工作时，最稀缺的能力不再只是“手工把每一步文字、推理、代码一点点织出来”，而是：

- 理解模型内部到底在表示什么
- 理解它为什么会成功、为什么会失败
- 理解哪些方向可以被安全地读出、干预、控制
- 理解怎样把这些判断变成研究、工具和产品决策

所以学 interpretability，不只是学一套论文话术；本质上是在学“机器智能出现之后，研究者应该如何理解机器原理并驾驭机器”。

更准确地说，AI 也只是对底层计算的又一层封装。

- 就像汇编语言是对机器语言的一层封装
- 就像高级语言又是对汇编语言的一层封装
- 大模型和 AI 系统，则是在这些计算抽象之上再包出来的一层更高抽象

正确的关注点因此不该停留在“手工完成旧流程的细碎技巧”上，而应该转向：

- 这一层封装到底暴露了什么能力
- 这一层封装隐藏了什么机制
- 我们怎样理解、使用、调试和控制这一层封装

这也是为什么这个项目既讲论文，也讲 Colab 复现、实验、artifact、steering、tracing、editing、auditing 和研究写作。

## 如果你持续做下去，会得到什么

- 第一小时之后：你至少应该已经跑通 1 个真实 notebook，并写下 reading note 或 experiment log 的开头。
- 第一个周末之后：你应该已经知道自己更适合走小白起跑线还是基础者起跑线，并完成 1 个 live 论文复现。
- 完整路径之后：你应该能拿出 notes、logs、memos、critiques 和扩展复现组成的作品集，强到足以让仓库把结果叫做 `P6-ready`。

## Pre-P4 基础包

如果你连 notebook、图表、attention 形状、baseline/sweep/ablation 这些都还不稳，就不要急着直接读主线论文，先补这 4 个 lab。

<!-- FOUNDATION_TABLE:START -->
| ID | 基础 Lab | Notebook | Colab | 运行层级 | 你会补齐什么 |
|---|---|---|---|---|---|
| `F00` | 环境、图表与基线纪律 | [打开](notebooks/foundations/zh/f00_environment_plots_baselines.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/foundations/zh/f00_environment_plots_baselines.ipynb) | `cpu-colab` | 建立本地/Colab 工作流，学会读 loss 曲线，并理解 baseline、variant 与日志记录的最小纪律。 |
| `F01` | Transformer 形状与注意力读图 | [打开](notebooks/foundations/zh/f01_transformer_shapes_attention.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/foundations/zh/f01_transformer_shapes_attention.ipynb) | `cpu-colab` | 用一个极小 attention 例子掌握 token、head、QK 打分、softmax 和 residual update 的形状感。 |
| `F02` | 向量几何、特征与探针 | [打开](notebooks/foundations/zh/f02_vector_geometry_features_probes.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/foundations/zh/f02_vector_geometry_features_probes.ipynb) | `cpu-colab` | 在二维和高维 toy 向量上练习 cosine、投影、方向相似和线性 probe，给 feature 语言补上几何底座。 |
| `F03` | Sweep、Ablation 与 Failure Analysis | [打开](notebooks/foundations/zh/f03_sweeps_ablations_failure_analysis.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/foundations/zh/f03_sweeps_ablations_failure_analysis.ipynb) | `cpu-colab` | 用一个小实验练习 sweep、ablation、停止条件和 failure analysis，把“会跑 notebook”推进到“会设计最小实验”。 |
<!-- FOUNDATION_TABLE:END -->

## 一篇文章，一个 Colab

下面每一行都对应一篇文章和一份 notebook。现在每篇讲义和每本 Colab 也都带有验收题，用来帮助读者检查自己到底学到了什么。

<!-- COURSE_TABLE:START -->
| ID | 文章 | 日期 | 状态 | Notebook | Colab | 运行层级 | 你会做什么 |
|---|---|---|---|---|---|---|---|
| `M00` | Zoom In：电路入门 | `2020-03-10` | `method-lab` | [打开](notebooks/zh/m00_zoom_in_circuits.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/m00_zoom_in_circuits.ipynb) | `warmup` | 用视觉模型建立 feature、circuit 与 intervention 的最初直觉。 |
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

## 推荐路径

- `Pre-P4 基础包`：`F00 → F01 → F02 → F03`
- `实时主线`：`M00 → M01 → M02 → M04 → M05`
- `当前只读论文`：`M03`、`M06`、`M07`、`M08`、`M09`、`M10`
- `扩展方法练习`：`X01 → X02 → X03 → X04 → X05 → X06 → X07`

如果你想先走最短的严格 live-code 路径，建议先做 `F00`、再看 `M00`、`M01`、`M02`、`M05`、`X01`。

## Research-Ready Path

如果你的目标不是“看懂”，而是“能以学生研究者或个人研究者的方式开始做事”，请把下面这些文件和文章 notebook 一起用：

- [研究就绪总览](docs/zh/program/research-ready.md)
- [Colab 优先路径](docs/zh/program/colab-first-path.md)
- [能力成长弧线与 P6 证据门槛](docs/zh/program/capability-arc.md)
- [P6 毕业清单](docs/zh/program/p6-graduation-checklist.md)
- [12 周训练营](docs/zh/program/week-by-week.md)
- [研究工作流](docs/zh/program/research-playbook.md)
- [评估 rubric](docs/zh/program/evaluation-rubric.md)
- [独立研究冲刺](docs/zh/program/independent-sprints.md)
- [参考答案层](docs/zh/program/reference-outputs.md)
- [扩展论文轨道](docs/zh/program/advanced-extensions.md)

模板：

- [Paper reading note](templates/paper_reading_note_zh.md)
- [Experiment log](templates/experiment_log_zh.md)
- [Research memo](templates/research_memo_zh.md)

内部训练阶段现在统一用 `S0-S4` 命名，和上面的阿里式 `P4-P12` 能力映射分开，避免把“课程阶段”误读成“公司职级”。`S0-S4` 是搭地板的核心段，不是完整长期成长弧线的全部。

把 research-ready path 当成一套工作系统，而不是额外阅读：

- 每篇文章都应该留下 reading note、experiment log、短 memo 和 next-question list。
- 这条路径默认你每周投入 `8-12` 小时的专注学习时间。
- 结营时应该拿得出真实作品集：notes、logs、memos、artifact critique 和两周 capstone proposal。
- 标准不是“我跟着 notebook 跑过了”，而是“我能读、能复现、能批判、也能提出下一步实验”。
- 单独完成 12 周训练营还不等于 `P6-ready`；只有再通过 P6 毕业清单，仓库才应该把结果叫做 `P6-ready`。

## 参考答案层

这层不是给你抄，而是给你校准“什么叫一个能交给导师、研究同伴、协作者或同行评审看的输出”。进入扩展复现之后，这一层会更重要。

<!-- REFERENCE_TABLE:START -->
| ID | 参考输出 | 文件 | 什么时候用 |
|---|---|---|---|
| `R01` | 参考论文简报 | [examples/zh/reference_paper_brief.md](examples/zh/reference_paper_brief.md) | 用在独立研究冲刺任务 T1 或任何 paper reading note 之后的压缩写作。 |
| `R02` | 参考实验日志 | [examples/zh/reference_experiment_log.md](examples/zh/reference_experiment_log.md) | 用在任何 sweep、ablation 或 feature-steering notebook 之后。 |
| `R03` | 参考 Artifact Critique | [examples/zh/reference_artifact_critique.md](examples/zh/reference_artifact_critique.md) | 用在 M03、M07、M09、M10 或独立研究冲刺任务 T3。 |
| `R04` | 参考两周提案 | [examples/zh/reference_two_week_proposal.md](examples/zh/reference_two_week_proposal.md) | 用在 capstone 或独立研究冲刺任务 T4 之前校准自己的提案密度。 |
<!-- REFERENCE_TABLE:END -->

## 扩展论文轨道

主线课程故意围绕 Anthropic interpretability 弧线来组织，但如果你的目标是让 `P6-ready` 这句结论诚实成立，或者继续往上长，这还不够。做完核心学徒阶段后，还要继续用更多 Colab 方法练习补 transformer circuits、经典行为电路、memory/editing 和 auditing 视角。

在严格实时规则下，状态列要这样理解：

- `paper-faithful`：可运行，且对论文问题形状是诚实的
- `method-lab`：可运行，但明确只是 live 方法练习，不冒充完整论文复现
- `reading-only`：只保留阅读与批判入口，因为否则就会依赖预计算 artifact 或不可公开栈

<!-- EXTENSION_TABLE:START -->
| ID | 扩展论文 | 链接 | 状态 | Notebook | Colab | 运行层级 | 为什么现在读 | 你要交什么 |
|---|---|---|---|---|---|---|---|---|
| `X01` | A Mathematical Framework for Transformer Circuits | [原文](https://transformer-circuits.pub/2021/framework/index.html) | `method-lab` | [打开](notebooks/extensions/zh/x01_transformer_circuits_framework.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/zh/x01_transformer_circuits_framework.ipynb) | `cpu-colab` | 当你已经做完 M06 之后，这篇能把你从“会读一张图”推进到“会说一个一般框架”。 | 在 Colab 里复现一个最小 residual-composition toy，并写 1 页 framework brief，把 M06 里的一个 toy trace 用 residual-stream 与 composition 语言重述。 |
| `X02` | In-context Learning and Induction Heads | [原文](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html) | `method-lab` | [打开](notebooks/extensions/zh/x02_induction_heads.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/zh/x02_induction_heads.ipynb) | `cpu-colab` | 它把 attention 读图、circuit 语言和具体行为现象连起来，是进入经典 transformer-circuits 的第一站。 | 在 Colab 里复现一个最小 copying task，并说明 induction head 为什么比单个 attention 热点更像“机制”。 |
| `X03` | Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 Small | [原文](https://arxiv.org/abs/2211.00593) | `method-lab` | [打开](notebooks/extensions/zh/x03_ioi_circuit.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/zh/x03_ioi_circuit.ipynb) | `cpu-colab` | 做完 Anthropic 主线后，这篇能逼你处理更脏的行为定义、更多的头和更复杂的证据链。 | 在 Colab 里复现一个教学版 IOI 证据链，并写 1 份 evidence-chain 速记，指出这类行为任务比 M06 toy trace 多了哪些不确定性。 |
| `X04` | Transformer Feed-Forward Layers Are Key-Value Memories | [原文](https://arxiv.org/abs/2012.14913) | `method-lab` | [打开](notebooks/extensions/zh/x04_ffn_key_value_memories.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/zh/x04_ffn_key_value_memories.ipynb) | `cpu-colab` | 如果你只会读 attention 电路，不会解释 MLP 存了什么，就很难进一步理解 factual recall 和编辑。 | 在 Colab 里复现一个教学版 key-value memory toy，并写 1 段说明为什么某些事实更像被 MLP 检索而不是被 attention 即时计算。 |
| `X05` | Knowledge Neurons in Pretrained Transformers | [原文](https://arxiv.org/abs/2104.08696) | `method-lab` | [打开](notebooks/extensions/zh/x05_knowledge_neurons.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/zh/x05_knowledge_neurons.ipynb) | `cpu-colab` | 这篇能迫使你区分“一个现象可被某些单元预测”与“这个现象真的由这些单元承载”之间的差别。 | 在 Colab 里复现一个教学版 knowledge-neuron 打分与消融实验，并写 1 段说明高分 neuron 为什么仍然不自动等于因果解释。 |
| `X06` | Locating and Editing Factual Associations in GPT | [原文](https://arxiv.org/abs/2202.05262) | `method-lab` | [打开](notebooks/extensions/zh/x06_rome_factual_editing.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/zh/x06_rome_factual_editing.ipynb) | `cpu-colab` | 如果你想从读图走到能做 intervention judgment，只会读图不够；你还得能讨论编辑是否稳定、是否局部、是否值得继续推进。 | 在 Colab 里复现一个教学版 rank-one factual edit，并写 1 份 edit memo，说明 edit success、locality 和 collateral damage 如何一起评估。 |
| `X07` | Auditing Language Models for Hidden Objectives | [原文](https://www.anthropic.com/research/auditing-hidden-objectives) | `method-lab` | [打开](notebooks/extensions/zh/x07_auditing_hidden_objectives.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/zh/x07_auditing_hidden_objectives.ipynb) | `cpu-colab` | 如果你想把 feature、tracing、editing 和 auditing 连成一条自洽研究线，这篇能把它们放到同一张图里。 | 在 Colab 里复现一个教学版 auditing toy，并写 1 份 memo，说明如果怀疑模型有隐藏目标，你会先看哪些行为信号、哪些内部证据、哪些停机标准。 |
<!-- EXTENSION_TABLE:END -->

## 快速开始

```bash
pip install -r requirements.txt

# 在修改课程元数据后，刷新派生内容
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py

# 校验 metadata、文档、notebook 镜像和外链
python3 scripts/validate_course.py
python3 scripts/check_links.py

# 强制检查 live notebook 不得依赖预计算 artifact
python3 scripts/audit_realtime_policy.py

# 执行所有生成的 notebook 烟雾测试
python3 scripts/smoke_notebooks.py
```

如果你想走最轻量的路径，直接点上表里的 Colab 链接即可，先不要把注意力花在本地工程栈上。

## 仓库结构

```text
.
├── content/               # 课程元数据与术语表
├── docs/                  # 中英文镜像文章讲义 + 基础包 + 扩展轨道 + 训练营文档
├── notebooks/             # 旧版长 notebook + 文章 notebook + foundation labs + 扩展复现
├── examples/              # 论文简报、实验日志、critique、proposal 参考样例
├── artifacts/             # 只读参考数据；严格 live notebook 不允许依赖这里
├── scripts/               # notebook 生成与校验脚本
├── figures/               # M00 继续复用的视觉电路图片
└── utils/                 # 原教程留下的绘图辅助函数
```

## 原项目保留内容

原始 notebook 仍然保留在仓库中：

- `notebooks/circuits_zoom_in_zh.ipynb`
- `notebooks/circuits_zoom_in_en.ipynb`

它们现在是 `M00` 的长篇背景材料。

## 参考来源

核心阅读路径按 `2026-03-25` 的官方页面状态冻结，索引页是：

- [Anthropic Interpretability team page](https://www.anthropic.com/research/team/interpretability)
- [Toy Models of Superposition](https://www.anthropic.com/research/toy-models-of-superposition)
- [Towards Monosemanticity](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning)
- [Mapping the Mind of a Large Language Model](https://www.anthropic.com/research/mapping-mind-language-model)
- [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)

## 许可证

[MIT](LICENSE)
