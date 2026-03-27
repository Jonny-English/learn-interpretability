# D06 曲线电路

- Distill 原文：[Curve Circuits](https://distill.pub/2020/circuits/curve-circuits/)
- 日期：2020-06-14
- 前置：[D05 高低频检测器](d05-high-low-frequency-detectors.md)
- 镜像：[English](../../en/articles/d06-curve-circuits.md)
- Notebook: [Notebook](../../../notebooks/zh/d06_curve_circuits.ipynb)
- Colab: [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d06_curve_circuits.ipynb)

## 摘要

通过 live 的上游重要度、消融和最小代理模型，在 mixed3a 与 mixed3b 之间追踪一条曲线电路。

## Notebook 范围

这本 notebook 把一条曲线电路改写成公开栈可跑的 trace：找上游通道、做消融，再把真实目标响应和最小代理模型对比起来。

## Live 覆盖

- 从 mixed3b 回溯到 mixed3a 的上游重要度搜索
- 对最关键上游通道做消融
- 最小代理模型与真实目标响应对比

## 诚实边界

这本 notebook 直接使用公开 InceptionV1 的实时权重、激活和消融结果。它是教学尺度的 circuit trace，不是 Distill 原文所有工件的完整重建。
