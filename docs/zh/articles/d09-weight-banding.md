# D09 权重带状结构

- Distill 原文：[Weight Banding](https://distill.pub/2020/circuits/weight-banding/)
- 日期：2020-09-01
- 前置：[D08 分支专门化](d08-branch-specialization.md)
- 镜像：[English](../../en/articles/d09-weight-banding.md)
- Notebook: [Notebook](../../../notebooks/zh/d09_weight_banding.ipynb)
- Colab: [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d09_weight_banding.ipynb)

## 摘要

实时分析最终分类器权重矩阵：重排行与列、可视化带状结构，并和打乱基线比较。

## Notebook 范围

这本 notebook 把带状结构当成公开分类头上的实时权重分析问题来做，而不是直接导出一张完成图。

## Live 覆盖

- 最终层权重矩阵重排
- 带宽跨度与打乱基线的比较
- 从重排矩阵里检查候选类别分组

## 诚实边界

矩阵图和 banding 分数都直接从公开分类头实时计算而来。这是运行时分析 notebook，不是预先打包好的静态导出。
