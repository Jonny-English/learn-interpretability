# M00 Zoom In：电路入门

## 目标

在公开 InceptionV1 上跑一遍教学尺度的 live 视觉电路复现。

## 核心参考

- [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/)

## 重点观察

- 单个神经元可以在实时激活最大化里表现出稳定视觉偏好。
- 同一个神经元可以再用真实图片去交叉验证，而不是只看合成图。
- 方向调谐可以被真实测出来，而不是从静态图里倒推。
- 一条小型 circuit 可以由真实学到的权重往上追出来，而不是手画示意图。

## Notebook 与 artifact

- Notebook：`notebooks/zh/m00_zoom_in_circuits.ipynb`
- 这本 notebook 会自己生成 feature visualization、CIFAR 验证面板、调谐曲线和上游权重 trace
- 延伸背景：`notebooks/circuits_zoom_in_zh.ipynb`

## 验收题

- 不用看原文，解释 feature、circuit、intervention 三个词分别是什么意思，以及它们之间是什么关系。
- 为什么 Zoom In 这套视觉电路故事对初学者非常有用，但直接照搬到语言模型上会出问题？
- 如果把这篇文章当成后续 interpretability 研究的起点，最先会被打破的是哪一部分直觉，为什么？

## 模块结论

这本 notebook 现在是把视觉电路直觉真正跑出来。它依然比语言模型 interpretability 更干净，但已经不再只是看图热身。
