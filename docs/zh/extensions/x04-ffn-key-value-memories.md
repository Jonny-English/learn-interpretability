# X04 Key-Value Memories

## 目标

把 MLP 层看成 key-value memory，理解事实召回为什么不只是 attention routing 问题。

## 核心参考

- [Transformer Feed-Forward Layers Are Key-Value Memories](https://arxiv.org/abs/2012.14913)

## 为什么它对 P8 路径重要

- 如果你不会解释 MLP 存了什么，就很难进入 factual recall、editing 和 memory localization。
- 这会把你的研究语言从“注意力电路”推进到“模型内部存储”。

## Notebook 与交付

- Notebook：`notebooks/extensions/zh/x04_ffn_key_value_memories.ipynb`
- 交付：1 份 key-value memory toy 复现记录，外加 1 段说明为什么某些事实更像被 MLP 检索。

## 验收题

- 在你的 toy 里，什么扮演 key，什么扮演 value？
- 为什么把某个 recall 行为解释成 MLP 检索，会改变你下一步实验设计？
- MLP memory 和 attention routing 在解释事实召回时各自更擅长说明什么？

## 扩展结论

一旦把 MLP 看成记忆层，很多关于知识、编辑和局部化的问题都会变得更可讨论。
