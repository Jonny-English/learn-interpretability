# M07 Circuit Tracing Tools

## 目标

把 circuit tracing 背后的工作流和 artifact 结构摊开来看，而不是假装自己已经复现了一整套工业级栈。

## 核心参考

- [Open-sourcing circuit tracing tools](https://www.anthropic.com/research/open-source-circuit-tracing)

## 重点观察

- tracing 需要的是一条管线，不只是一个可视化。
- 中间文件和打分阶段会直接影响你最后能看见什么。
- 工具层的设计会决定后续图的保真度和可用性。

## 当前状态

- 在严格实时规则下是 `reading-only`
- 当前仓库不再提供这里的 live notebook，因为工具工作流说明仍然依赖预计算 artifact。
- 共享参考 artifact：`artifacts/m06_attribution_graph.json` 与 `artifacts/m07_tracing_tool_workflow.json`

## 验收题

- 在 tracing workflow 里，哪一个步骤最像瓶颈，为什么？
- 如果你要给研究工程师提一个优先实现的工具需求，你会提什么，怎么衡量它值不值得做？
- 为什么说工具层不仅影响效率，还会改变团队能问什么研究问题？

## 模块结论

好的 interpretability 结果，依赖的不只是好想法，也依赖好工具。
