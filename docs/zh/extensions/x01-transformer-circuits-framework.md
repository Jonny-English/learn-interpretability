# X01 Transformer Circuits 的数学框架

## 目标

把 residual stream、attention、MLP、composition 放进同一套语言里，避免后面的 tracing、editing 和 auditing 只剩下术语堆叠。

## 核心参考

- [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html)

## 为什么它对 P8 路径重要

- 这篇会把你从“我会读某一张图”推进到“我能描述一整类机制如何组合”。
- 如果没有这套语言，后面很多解释都会停在部件罗列，而无法进入方向级判断。

## Notebook 与交付

- Notebook：`notebooks/extensions/zh/x01_transformer_circuits_framework.ipynb`
- 交付：1 份 framework brief，外加 1 段把 M06 toy trace 改写成 residual-stream 语言的说明。

## 验收题

- 为什么 residual stream 语言比逐层局部描述更适合说“机制”？
- 在你的 toy 复现里，哪一次 composition 真正改变了最终读出？
- 如果一个解释只会列 head 名称、不会说 composition，它缺了什么？

## 扩展结论

这篇不是给你多一个名词表，而是给你一套可以复用到后续所有论文上的解释语法。
