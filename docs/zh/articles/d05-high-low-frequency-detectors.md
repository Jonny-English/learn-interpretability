# D05 高低频检测器

- Distill 原文：[High-Low Frequency Detectors](https://distill.pub/2020/circuits/frequency-edges/)
- 日期：2020-06-03
- 前置：[D04 神经网络中的自然涌现等变性](d04-equivariance.md)
- 镜像：[English](../../en/articles/d05-high-low-frequency-detectors.md)
- Notebook: [Notebook](../../../notebooks/zh/d05_high_low_frequency_detectors.ipynb)
- Colab: [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/d05_high_low_frequency_detectors.ipynb)

## 摘要

实时生成有方向性的高低频过渡刺激，并测量哪些通道偏好这种频率边界。

## Notebook 范围

这本 notebook 在运行时合成频率边界刺激，并搜索对它们强响应且具有选择性的通道。

## Live 覆盖

- 高低频刺激生成
- 频率边界偏好通道搜索
- 最佳频率检测器的方向调谐

## 诚实边界

刺激由公开代码实时生成，图像和曲线都是运行时测量结果，而不是仓库内打包好的 Distill 图片副本。
