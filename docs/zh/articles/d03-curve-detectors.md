# D03 曲线检测器

- Distill 原文：[Curve Detectors](https://distill.pub/2020/circuits/curve-detectors)
- 日期：2020-04-21
- 前置：[D02 InceptionV1 早期视觉总览](d02-early-vision.md)
- 镜像：[English](../../en/articles/d03-curve-detectors.md)
- Notebook: [Notebook](../../../notebooks/zh/d03_curve_detectors.ipynb)
- Colab: [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d03_curve_detectors.ipynb)

## 摘要

实时搜索曲线偏好通道，对比直线、弧线和曲率刺激，并用真实图片验证最佳通道。

## Notebook 范围

这本 notebook 不再复读静态故事，而是在运行时直接搜索曲线偏好通道，再检验它们到底偏好什么。

## Live 覆盖

- 在 mixed3b 里搜索曲线偏好通道
- 直线、弧线和整圆刺激对比
- 对最强曲线通道做真实图片验证

## 诚实边界

搜索空间和验证集都比 Distill 原文更小，但检测器发现和测量都是在公开模型上实时生成的。
