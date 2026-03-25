# M05 Character and Control

## 目标

通过 persona vectors 和两篇前沿阅读，把 interpretability 与模型 character/control 的问题接起来。

## 核心参考

- [Persona vectors](https://www.anthropic.com/research/persona-vectors)
- [Signs of introspection in large language models](https://www.anthropic.com/research/introspection)
- [The assistant axis](https://www.anthropic.com/research/assistant-axis)

## 重点观察

- character trait 可以被表示成方向，而不只是 prompt 层面的效果。
- 调人格不等于解决 alignment，也不等于证明模型真的“自知”。
- 前沿论文的作用是扩大问题空间，而不是制造虚假的确定性。

## Notebook 与 artifact

- Notebook：`notebooks/zh/m05_character_control.ipynb`
- 共享 artifact：`artifacts/m05_persona_vectors.json`

## 模块结论

interpretability 可以开始触及模型 character，但它打开的是一组新的控制问题，而不是终点答案。
