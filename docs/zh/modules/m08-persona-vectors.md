# M08 Persona Vectors

## 目标

把 feature 风格的思路接到 character trait 上，把 persona 看成表示空间中的方向，但不假装当前仓库已经具备公开实时 persona-vectors 栈。

## 核心参考

- [Persona Vectors](https://www.anthropic.com/research/persona-vectors)

## 重点观察

- character 可以被监控成一个方向上的移动。
- 干预前后可以比较 trait 的变化。
- persona vector 是一个有用把手，但不是完整的人格理论。

## 当前状态

- 在严格实时规则下是 `reading-only`
- 当前仓库不再提供这里的 live notebook，因为那会依赖预计算 persona-vector artifact。
- 共享参考 artifact：`artifacts/m08_persona_vectors.json`

## 验收题

- persona vectors 让哪些原本模糊的 character 属性变得可比较、可测量？
- 即使一个向量方向在当前 artifact 里有效，character control 仍然可能在哪些地方漂移或失稳？
- 如果你要评估 persona control 的稳定性，你会在不同 prompt、任务或时序上怎么测？

## 模块结论

一旦表示方向开始具有行为意义，interpretability 就会碰到模型 character；但当前仓库把这一篇只保留为阅读与批判入口，直到公开实时栈可用。
