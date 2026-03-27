# D04 神经网络中的自然涌现等变性

- Distill 原文：[Naturally Occurring Equivariance in Neural Networks](https://distill.pub/2020/circuits/equivariance/)
- 日期：2020-05-20
- 前置：[D03 曲线检测器](d03-curve-detectors.md)
- 镜像：[English](../../en/articles/d04-equivariance.md)
- Notebook: [Notebook](../../../notebooks/zh/d04_equivariance.ipynb)
- Colab: [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d04_equivariance.ipynb)

## 摘要

实时寻找变换对应的滤波器对，比对旋转和平移响应，观察 feature 家族如何一起移动。

## Notebook 范围

这本 notebook 先在权重空间里搜索等变结构，再用刺激 sweep 去验证这些关系。

## Live 覆盖

- 在 Inception 分支里搜索旋转相似滤波器对
- 匹配通道的旋转弧线响应 sweep
- 平移刺激上的响应一致性检查

## 诚实边界

这是对公开 InceptionV1 权重和激活中等变结构的教学尺度 live 分析，不宣称逐一复现 Distill 原文里的所有案例。
