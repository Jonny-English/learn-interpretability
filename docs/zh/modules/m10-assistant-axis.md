# M10 The Assistant Axis

## 目标

研究不同 assistant 风格如何被放到同一条轴上，以及为什么“稳定这条轴”会成为问题。

## 核心参考

- [The assistant axis](https://www.anthropic.com/research/assistant-axis)

## 重点观察

- 多种 assistant 风格可以放进同一个比较框架里。
- helpfulness、safety 和 warmth 并不是彼此独立移动的。
- 稳定 character 既是 interpretability 问题，也是产品问题。

## 当前状态

- 在严格实时规则下是 `reading-only`
- 当前仓库不再提供这里的 live notebook，因为那会依赖预计算 assistant-axis artifact。
- 共享参考 artifact：`artifacts/m10_assistant_axis.json`

## 验收题

- 为什么用一条 assistant axis 来压缩多种风格是有用的，但又不够？
- 沿着这条轴，哪些属性看起来会平滑变化，哪些属性明显不会？
- 如果给你两周时间研究 character stabilization，你会围绕这条轴设计什么最小实验？

## 模块结论

这篇论文把 character control 从局部干预问题推进到了更广义的稳定性问题。
