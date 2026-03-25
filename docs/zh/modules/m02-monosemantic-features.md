# M02 单语义特征与字典学习

## 目标

用教学版 sparse autoencoder 展示：为什么从 neuron 视角切到 feature 视角，会得到更稳定、更可复用的分析单位。

## 核心参考

- [Towards Monosemanticity](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning)
- [Mapping the Mind of a Large Language Model](https://www.anthropic.com/research/mapping-mind-language-model)

## 重点观察

- 为什么稀疏编码能学到比原始神经元更干净的方向。
- 为什么一个“字典”会自然变成后续 probe 与 steering 的底座。
- 为什么特征发现不是神奇显微镜，而是一种有偏但有用的建模选择。

## Notebook 与 artifact

- Notebook：`notebooks/zh/m02_monosemantic_features.ipynb`
- 共享 artifact：`artifacts/concept_graph.json`

## 模块结论

字典学习让 interpretability 从“看神经元”转向“操作可复用特征”。
