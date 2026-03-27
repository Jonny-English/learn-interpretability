# D08 分支专门化

- Distill 原文：[Branch Specialization](https://distill.pub/2020/circuits/branch-specialization/)
- 日期：2020-08-26
- 前置：[D07 权重可视化](d07-visualizing-weights.md)
- 镜像：[English](../../en/articles/d08-branch-specialization.md)
- Notebook: [Notebook](../../../notebooks/zh/d08_branch_specialization.ipynb)
- Colab: [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d08_branch_specialization.ipynb)

## 摘要

测量不同 Inception 分支对直线、弧线和频率刺激家族的响应，再实时渲染各分支的代表性通道。

## Notebook 范围

这本 notebook 把分支专门化写成一张 live 的“分支 × 刺激家族”响应图，而不是从论文里搬一张静态示意图。

## Live 覆盖

- 刺激家族上的分支响应热图
- 各分支内部的 top-channel 搜索
- 分支代表通道的 live feature render

## 诚实边界

这里的专门化结论来自公开分支和公开刺激上的实时测量，目标是透明可检查，而不是穷尽式地追平论文所有细节。
