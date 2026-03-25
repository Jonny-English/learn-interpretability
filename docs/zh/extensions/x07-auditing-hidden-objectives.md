# X07 Auditing Hidden Objectives

## 目标

把 interpretability、editing、behavior evaluation 和 auditing 放进同一套判断框架里。

## 核心参考

- [Auditing Language Models for Hidden Objectives](https://www.anthropic.com/research/auditing-hidden-objectives)

## 为什么它对 P8 路径重要

- 这篇会把“看懂模型”推进到“判断模型可能在偷偷优化什么”。
- 如果终点是公司研究，这类工作最接近真正的方向负责人与安全接口。

## Notebook 与交付

- Notebook：`notebooks/extensions/zh/x07_auditing_hidden_objectives.ipynb`
- 交付：1 份 auditing toy 复现记录，外加 1 份 memo，说明行为信号、内部证据和 stop condition 如何形成闭环。

## 验收题

- 为什么只看行为异常，常常不足以判断是否存在隐藏目标？
- 你的 toy audit 里，哪一种内部证据最能和行为信号形成闭环？
- 如果你要把 auditing 工作交给团队，你会把 stop condition 写成什么样？

## 扩展结论

这篇让项目真正连到公司研究现场，因为它要求你把 interpretability 结果转成可执行的风险判断。
