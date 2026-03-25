# X03 IOI 电路

## 目标

把电路分析从 toy 任务推进到自然语言行为，并练习更长、更脏、更不确定的证据链。

## 核心参考

- [Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 Small](https://arxiv.org/abs/2211.00593)

## 为什么它对 P8 路径重要

- 这篇迫使你面对自然语言行为定义、更多组件和更复杂的 ablation 证据。
- 如果你未来要负责一个研究子方向，不能只会处理干净 toy，需要会处理这种证据复杂度。

## Notebook 与交付

- Notebook：`notebooks/extensions/zh/x03_ioi_circuit.ipynb`
- 交付：1 份 IOI evidence-chain 速记，外加 1 段说明这类行为任务比 M06 toy trace 多了哪些不确定性。

## 验收题

- 为什么 IOI 比 toy trace 更难建立证据闭环？
- 在你的教学版证据链里，哪一条边最像“必要但不充分”的证据？
- 如果一个头在图里很亮，你还需要什么额外证据？

## 扩展结论

这篇会把你逼到真正的行为电路问题前，让你开始习惯“证据不再整齐”的研究现实。
