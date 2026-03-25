# M01 Superposition

## 目标

用一个小型稀疏 toy model 解释为什么“一个神经元只代表一个语义”通常是错误默认。

## 核心参考

- [Toy Models of Superposition](https://www.anthropic.com/research/toy-models-of-superposition)

## 重点观察

- 稀疏概念也会因为维度不足而被压进同一空间。
- 模型可以一边重建输入，一边把多个概念混在同一维度里。
- 神经元层面的阅读方式，天然会错过这种混装现象。

## Notebook 与 artifact

- Notebook：`notebooks/zh/m01_superposition.ipynb`
- 共享 artifact：`artifacts/concept_graph.json`

## 模块结论

superposition 是后续所有章节的动机来源。先看到“为什么神经元不够用”，再谈 feature 才不会像空降概念。
