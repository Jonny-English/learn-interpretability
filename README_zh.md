# Learn Interpretability: Distill Circuits

一个双语、Colab 优先、严格 live-only 的仓库，专门服务 [Distill 2020 Circuits 线程](https://distill.pub/2020/circuits/)。

这个仓库现在只做一件事：

- 把 Distill Circuits 线程收口成一条 `D00-D09` 学习线
- 维护中英双语镜像讲义
- 为 `D01-D09` 生成 live notebooks
- 明确拒绝预渲染 `figures/`、预计算 `artifacts/` 和幻灯片式讲解

## 从这里开始

- 先读线程入口：[D00 Circuits 线程总览](docs/zh/articles/d00-thread-circuits.md)
- 直接打开第一本 live notebook：[D01 Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d01_zoom_in.ipynb)
- 浏览中文文档首页：[docs/zh/index.md](docs/zh/index.md)

## 为什么要做这个仓库

Distill 的 Circuits 线程依然是公开世界里最清晰的神经电路入门材料之一。问题在于，很多读者接触到它时，看到的是一串漂亮的静态页面。这个仓库把它改造成一条可运行的学习路径：每一本 live notebook 都必须用公开权重、公开数据和运行时生成的分析来为自己的说法负责。

## Distill 顺序

| ID | Article | Paper | Mode | Docs | Colab |
| --- | --- | --- | --- | --- | --- |
| D00 | Circuits 线程总览 | [Thread: Circuits](https://distill.pub/2020/circuits/) | 只读 | [D00](docs/zh/articles/d00-thread-circuits.md) | - |
| D01 | Zoom In：电路入门 | [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/) | live | [D01](docs/zh/articles/d01-zoom-in.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d01_zoom_in.ipynb) |
| D02 | InceptionV1 早期视觉总览 | [An Overview of Early Vision in InceptionV1](https://distill.pub/2020/circuits/early-vision/) | live | [D02](docs/zh/articles/d02-early-vision.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d02_early_vision.ipynb) |
| D03 | 曲线检测器 | [Curve Detectors](https://distill.pub/2020/circuits/curve-detectors) | live | [D03](docs/zh/articles/d03-curve-detectors.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d03_curve_detectors.ipynb) |
| D04 | 神经网络中的自然涌现等变性 | [Naturally Occurring Equivariance in Neural Networks](https://distill.pub/2020/circuits/equivariance/) | live | [D04](docs/zh/articles/d04-equivariance.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d04_equivariance.ipynb) |
| D05 | 高低频检测器 | [High-Low Frequency Detectors](https://distill.pub/2020/circuits/frequency-edges/) | live | [D05](docs/zh/articles/d05-high-low-frequency-detectors.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d05_high_low_frequency_detectors.ipynb) |
| D06 | 曲线电路 | [Curve Circuits](https://distill.pub/2020/circuits/curve-circuits/) | live | [D06](docs/zh/articles/d06-curve-circuits.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d06_curve_circuits.ipynb) |
| D07 | 权重可视化 | [Visualizing Weights](https://distill.pub/2020/circuits/visualizing-weights/) | live | [D07](docs/zh/articles/d07-visualizing-weights.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d07_visualizing_weights.ipynb) |
| D08 | 分支专门化 | [Branch Specialization](https://distill.pub/2020/circuits/branch-specialization/) | live | [D08](docs/zh/articles/d08-branch-specialization.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d08_branch_specialization.ipynb) |
| D09 | 权重带状结构 | [Weight Banding](https://distill.pub/2020/circuits/weight-banding/) | live | [D09](docs/zh/articles/d09-weight-banding.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d09_weight_banding.ipynb) |

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
