# D07 权重可视化

- Distill 原文：[Visualizing Weights](https://distill.pub/2020/circuits/visualizing-weights/)
- 日期：2020-07-13
- 前置：[D06 曲线电路](d06-curve-circuits.md)
- 镜像：[English](../../en/articles/d07-visualizing-weights.md)
- Notebook: [Notebook](../../../notebooks/zh/d07_visualizing_weights.ipynb)
- Colab: [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d07_visualizing_weights.ipynb)

## 摘要

直接可视化真实的 InceptionV1 权重，并比较权重视角和 feature visualization 视角各自揭示了什么。

## Notebook 范围

这本 notebook 全程使用运行时生成的权重视图，再配上同一批通道的 live feature render，让两种视角建立直接对应。

## Live 覆盖

- 第一层 RGB 滤波器直接可视化
- 更深卷积滤波器的能量图视角
- 同一通道上的权重视角与 feature 视角对比

## 诚实边界

所有图像都在运行时直接从公开模型权重生成，仓库里不再打包任何预渲染的权重图。
