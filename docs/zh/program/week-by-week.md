# Week-by-Week Bootcamp

把这 12 周当成学徒训练，而不是播放列表。每周末都有一个 gate；如果过不了，就重复这一周或缩小范围，不要硬往后推。训练营只是核心学徒阶段，不是完整的 `P6-ready` 结论；第 12 周之后还要再走毕业清单。

## 第 1 周：环境、术语和阅读方法

- 文章：`M00`
- 目标：先把环境变成稳定、无聊的基础设施，让真正的学习能开始
- 核心工作：
  - 在本地或 Colab 跑通仓库
  - 写第一份 paper reading note
  - 建立一个只记录“自己真的不懂”的术语表
- 输出：
  - 1 份 reading note
  - 1 次完整 notebook 运行
  - 1 份包含 5 个不懂术语的列表
- Gate：不用看 notebook，也能用自己的话解释 feature、circuit、intervention

## 第 2 周：从视觉电路到 superposition

- 文章：`M00`、`M01`
- 目标：理解为什么干净的 neuron 图像不再够用
- 核心工作：
  - 复现 toy model 图
  - 扫一个变量家族，比如 hidden dimension 或 sparsity
  - 写下重叠出现的几何原因
- 输出：
  - 1 份 experiment log
  - 1 张带注释的图
  - 1 段关于为什么 neuron semantics 会失效的短 memo
- Gate：你能把 superposition 讲成一个几何问题，而不只是说“神经元混了多个概念”

## 第 3 周：Sparse Autoencoder 与 Monosemanticity

- 文章：`M02`
- 目标：看到为什么 feature recovery 比原始 neuron 分析更干净
- 核心工作：
  - 跑通 SAE toy lab
  - 改一个维度，比如 sparsity、feature 数量或噪声
  - 记录 feature 恢复开始变差的边界
- 输出：
  - 1 份 experiment log
  - 1 份失败边界说明
  - 1 份关于“恢复出来的 feature 到底解决了什么”的短 memo
- Gate：你能指出 monosemanticity 变差至少有一个具体原因

## 第 4 周：从单例到 feature 地图

- 文章：`M03`
- 目标：不再把 feature 当成单个有趣例子，而开始把它们当作地图
- 核心工作：
  - 浏览教学版 feature catalog
  - 自己做一套分类
  - 提出一个你觉得值得找但还没被列出来的 feature
- 输出：
  - 1 份 taxonomy note
  - 1 个缺失 feature 问题
  - 1 份短 memo
- Gate：你能解释 catalog 改变的是研究方式，而不是只改变例子数量

## 第 5 周：Feature Probe

- 文章：`M04`
- 目标：把 feature 变成 readout 工具
- 核心工作：
  - 跑 probe notebook
  - 改目标标签或加入一个 confounder
  - 写清 accuracy 能说明什么、不能说明什么
- 输出：
  - 1 份 probe memo
  - 1 张 feature 权重图
  - 3 个潜在 confounders
- Gate：你能同时讨论 classifier 表现、baseline 和 confounders

## 第 6 周：Feature Steering

- 文章：`M05`
- 目标：学会看 utility，而不是只看 gain
- 核心工作：
  - 做 steering strength sweep
  - 自己定义 1 个 off-target metric
  - 解释 sweet spot 为什么出现
- 输出：
  - 1 份 steering memo
  - 1 个 off-target metric
  - 1 份 failure-analysis note
- Gate：你的结论里同时包含收益和副作用

## 第 7 周：中期复盘

- 文章：`M01`、`M02`、`M04`、`M05`
- 目标：把前半程沉淀成证据，而不是零散印象
- 核心工作：
  - 收集前六周的 notes、logs 和 memos
  - 用 rubric 自评
  - 针对最弱项做一个补短板动作
- 输出：
  - 1 份两页中期 memo
  - 1 次 rubric 自评
  - 1 个 corrective action
- Gate：你能指出自己最弱的研究习惯，并给出一个具体修复动作

## 第 8 周：Tracing Graph 阅读

- 文章：`M06`
- 目标：学会把图当证据来读，而不是当装饰来看
- 核心工作：
  - 完成一份 attribution graph walkthrough
  - 解释 3 条高贡献路径
  - 写 1 段关于图上歧义的说明
- 输出：
  - 1 份 graph walkthrough
  - 1 份路径解释
  - 1 份 ambiguity note
- Gate：你能明确说出“这张图还不能证明什么”

## 第 9 周：Tracing Tooling

- 文章：`M07`
- 目标：理解工具会反过来决定一个研究者能研究什么
- 核心工作：
  - 画 workflow
  - 分析 1 个 tooling bottleneck
  - 写一份 tooling-needs note
- 输出：
  - 1 张 workflow 图
  - 1 份 bottleneck analysis
  - 1 份工具需求 note
- Gate：你能解释工具层是如何约束或放大一条研究线的

## 第 10 周：Character 与 Self-Modeling

- 文章：`M08`、`M09`、`M10`
- 目标：把表示分析和控制问题联系起来
- 核心工作：
  - 比较 persona vectors、introspection signals 和 assistant axis
  - 写一份把 evidence 和 interpretation 分开的 critique
  - 提出 1 个 follow-up experiment
- 输出：
  - 1 份 comparative critique
  - 1 个 follow-up experiment 想法
  - 1 份短 memo
- Gate：你不会把 self-report 直接当作内部状态的充分证据

## 第 11 周：Capstone 设计

- 文章：`M03`、`M05`、`M06`、`M08`
- 目标：把理解压缩成一个可信的研究提案
- 核心工作：
  - 选一个能从课程中延展出来的问题
  - 定义假设、baseline、预算和 stop condition
  - 列出最可能失败的点
- 输出：
  - 1 份 capstone proposal
  - 1 份资源预算
  - 1 份风险列表
- Gate：你的提案足够小，能在两周做完；也足够具体，能真正失败

## 第 12 周：最终研究汇报

- 文章：`M08`、`M09`、`M10`
- 目标：像早期研究者一样汇报，而不是像在复述课程笔记
- 核心工作：
  - 写最终 memo
  - 准备 10 分钟口头汇报
  - 写 next-step plan
- 输出：
  - 1 份 final memo
  - 1 份 next-step plan
  - 1 次简短汇报
- Gate：你的汇报里有判断、有证据、有风险，也有下一步行动，而且它能被当成一份 scoped research-task dossier 来辩护，而不是课程内容回顾
