# D01 Zoom In：电路入门

- Distill 原文：[Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/)
- 日期：2020-03-10
- 前置：[D00 Circuits 线程总览](d00-thread-circuits.md)
- 镜像：[English](../../en/articles/d01-zoom-in.md)
- Notebook: [Notebook](../../../notebooks/zh/d01_zoom_in.ipynb)
- Colab: [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d01_zoom_in.ipynb)

## 摘要

在 InceptionV1 上跑一条 live 视觉电路入门线：feature visualization、真实图片验证、方向调谐和一条小型 circuit trace。

## Notebook 范围

这本 notebook 保留原文的直觉主线，但把关键图和测量改成公开栈上的实时产出，而不是预渲染图片。

## Live 覆盖

- 代表性通道的激活最大化
- 曲线偏好神经元的 CIFAR-10 真实图片验证
- 合成弧线刺激上的方向调谐
- 一条 mixed3b 小型电路的上游权重 trace

## 诚实边界

这是对原文核心动作的公开栈 live 重建，但不宣称复现 Distill 页面里的每一张定制图或人工注释。
