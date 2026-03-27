# D02 InceptionV1 早期视觉总览

- Distill 原文：[An Overview of Early Vision in InceptionV1](https://distill.pub/2020/circuits/early-vision/)
- 日期：2020-03-31
- 前置：[D01 Zoom In：电路入门](d01-zoom-in.md)
- 镜像：[English](../../en/articles/d02-early-vision.md)
- Notebook: [Notebook](../../../notebooks/zh/d02_early_vision.ipynb)
- Colab: [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d02_early_vision.ipynb)

## 摘要

用 live feature render、family-response 统计和逐层通道快照，梳理 InceptionV1 的早期视觉层。

## Notebook 范围

这本 notebook 直接从公开 InceptionV1 里采样早期层，概括 feature 家族如何从边缘扩展到小型图案。

## Live 覆盖

- 逐层 feature render 图库
- 早期层上的合成刺激家族响应热图
- 选定通道的真实图片激活快照

## 诚实边界

这本 notebook 在公开模型上用 live render 和实测激活做分析。规模是教学尺度，但所有图都在运行时生成。
