# From Circuits to Claude

[**English README**](README.md) ·
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Next.js Static Export](https://img.shields.io/badge/web-next.js-black.svg)](web/)

`From Circuits to Claude` 是一个面向初学者的双语 interpretability 教程。它先复用原始 `circuits-zoom-in` 项目里最直观的视觉电路材料，再把读者带到 Anthropic 这条核心研究主线：superposition、dictionary learning、feature probes、circuit tracing，以及 character control。

仓库现在由三层同步组成：

- `content/course.json`：模块顺序、标题、先修关系、论文链接、artifact 引用的唯一真相源。
- `docs/zh` 与 `docs/en`：结构完全镜像的概念讲义。
- `notebooks/zh` 与 `notebooks/en`：结构完全镜像的运行材料，`web/` 则把同一份元数据渲染成静态课程站。

## 课程地图

<!-- COURSE_TABLE:START -->
| 模块 | 主题 | 运行层级 | 说明 |
|---|---|---|---|
| `M00` | 视觉电路热身 | `warmup` | 复用原始 Zoom In 视觉电路材料，先建立 feature、circuit 和 intervention 的直觉。 |
| `M01` | Superposition | `cpu-colab` | 用小型稀疏 toy model 理解为什么神经元经常不是干净的语义单位。 |
| `M02` | 单语义特征与字典学习 | `cpu-colab` | 用教学版 SAE 理解从 neuron 视角过渡到 feature 视角的原因与收益。 |
| `M03` | 特征探针与 Steering | `cpu-colab` | 在小型可运行实验里展示 feature 如何同时承担读取和干预的角色。 |
| `M04` | Circuit Tracing | `artifact-guided` | 借助预计算 attribution graph 学会如何阅读 LLM 的局部计算路径。 |
| `M05` | Character and Control | `artifact-guided` | 通过 persona vectors 和前沿阅读，把 interpretability 与 character control 连接起来。 |
<!-- COURSE_TABLE:END -->

## 学习设计

- `M00` 保留原始视觉电路 notebook，帮助读者先建立 feature、circuit、intervention 的直觉。
- `M01-M03` 是可以在 CPU 或免费 Colab 上跑通的必修 lab，覆盖 superposition、monosemantic features 与 feature steering。
- `M04-M05` 通过预计算 artifact 教 attribution graph 和 persona vectors，不要求读者复现完整研究流水线。
- `web/` 提供论文时间线、概念依赖图、术语卡片和章节进度，帮助读者把论文、概念和 notebook 串起来。

## 快速开始

```bash
pip install -r requirements.txt

# 在修改课程元数据后，刷新派生内容
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py

# 校验 metadata、文档、notebook 镜像和外链
python3 scripts/validate_course.py
python3 scripts/check_links.py

# 执行所有生成的 notebook 烟雾测试
python3 scripts/smoke_notebooks.py
```

构建静态站：

```bash
cd web
npm install
npm run build
```

## 仓库结构

```text
.
├── content/               # 课程元数据与术语表
├── docs/                  # 中英文镜像讲义
├── notebooks/             # 旧版长 notebook + 新版课程 notebook
├── artifacts/             # 供 notebook / web 共享的 JSON artifact
├── web/                   # 静态 Next.js 课程站
├── scripts/               # notebook 生成与校验脚本
├── figures/               # M00 继续复用的视觉电路图片
└── utils/                 # 原教程留下的绘图辅助函数
```

## 旧版材料

原始 notebook 仍然保留在仓库中：

- `notebooks/circuits_zoom_in_zh.ipynb`
- `notebooks/circuits_zoom_in_en.ipynb`

它们现在是 `M00` 的长篇背景材料，不再是整个项目唯一的入口。

## 参考来源

核心课程按 `2026-03-25` 的官方页面状态冻结，索引页是：

- [Anthropic Interpretability team page](https://www.anthropic.com/research/team/interpretability)
- [Toy Models of Superposition](https://www.anthropic.com/research/toy-models-of-superposition)
- [Towards Monosemanticity](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning)
- [Mapping the Mind of a Large Language Model](https://www.anthropic.com/research/mapping-mind-language-model)
- [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)

## 许可证

[MIT](LICENSE)
