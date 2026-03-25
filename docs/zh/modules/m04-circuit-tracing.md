# M04 Circuit Tracing

## 目标

教读者如何阅读 attribution graph、解释一条局部计算路径，同时不假装自己已经复现了完整的工业级 tracing 栈。

## 核心参考

- [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)
- [Open-sourcing circuit tracing tools](https://www.anthropic.com/research/open-source-circuit-tracing)

## 重点观察

- 输入、中间特征和输出可以通过带权贡献路径连起来。
- 好的 tracing artifact 不是把整张网络摊开，而是只暴露有解释价值的局部切片。
- “解释答案是什么”与“解释答案是怎么算出来的”是两件不同的事。

## Notebook 与 artifact

- Notebook：`notebooks/zh/m04_circuit_tracing.ipynb`
- 共享 artifact：`artifacts/m04_attribution_graph.json`

## 模块结论

这一章把 interpretability 从孤立特征推进到局部计算图。
