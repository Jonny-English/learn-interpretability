# M06 Tracing the Thoughts

## 目标

学习如何阅读一张局部 attribution graph，并解释一条从输入走到答案的计算路径，但不假装当前仓库已经具备公开实时 tracing 栈。

## 核心参考

- [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)

## 重点观察

- 输入、中间特征和输出可以通过带权路径连起来。
- 好的 trace 是有选择地暴露局部，而不是一次性摊开整个模型。
- “解释答案是什么”与“解释答案是怎么算出来的”是两件不同的事。

## 当前状态

- 在严格实时规则下是 `reading-only`
- 当前仓库不再提供这里的 live notebook，因为那会依赖预计算 attribution artifact。
- 共享参考 artifact：`artifacts/m06_attribution_graph.json`

## 验收题

- 不用照抄图上的标签，解释这张 attribution graph 里最重要的 3 条贡献路径在做什么。
- 这张图支持什么结论，又明确不支持什么结论？
- 如果你只能再做一个后续实验来降低这张图的歧义，你会选什么？

## 模块结论

这篇论文把焦点从孤立 feature 推进到局部计算图，而当前仓库只把它保留为阅读与批判入口，直到公开实时 tracing 栈可用。
