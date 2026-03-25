# M09 Signs of Introspection

## 目标

检查模型“怎么描述自己”和“行为上暴露出什么”之间的差距，但不假装当前仓库已经具备原论文层面的实时实验栈。

## 核心参考

- [Signs of introspection in large language models](https://www.anthropic.com/research/introspection)

## 重点观察

- self-report 和可观察行为有时一致，但不会完美一致。
- 真正值得盯住的，是那些不一致的案例。
- “出现内省迹象”更应该扩大问题，而不是过早下结论。

## 当前状态

- 在严格实时规则下是 `reading-only`
- 当前仓库不再提供这里的 live notebook，因为那会依赖预计算 introspection-signal artifact。
- 共享参考 artifact：`artifacts/m09_introspection_signals.json`

## 验收题

- 为什么 self-report 不能被直接当成内部状态的证据？
- 在这些 mismatch case 里，哪一个最值得继续追，替代解释可能有哪些？
- 如果你想把“内省迹象”这个 claim 说得更强，还缺哪类关键证据？

## 模块结论

这篇论文更像对 self-modeling 的前沿探针，而不是对稳健内省的证明。
