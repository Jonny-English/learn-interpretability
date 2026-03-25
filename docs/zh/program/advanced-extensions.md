# 扩展论文轨道

主线课程故意围绕 Anthropic interpretability 弧线来组织，因为这样最清楚。但如果目标是朝 `P8` 方向成长，主线只是地基，不是终点。

## 这条轨道为什么重要

- 严肃的 interpretability 研究不会只围绕一条论文线或一个实验室的局部叙事展开。
- 你需要补上更通用的 transformer circuits 语言、memory/editing 问题形状和 auditing 视角。
- 更重要的是：这些扩展论文现在不是“阅读列表”，而是一组要在 Colab 里亲手复现的训练任务。

## 这条轨道怎么用

- 不要一口气全做完。每完成主线的一个阶段，就插入一篇对应的扩展复现。
- 每篇扩展论文都至少留下 4 个产物：Colab 复现、experiment log、短 memo、下一步实验。
- 如果时间有限，优先选能把你刚做完的主线模块重新解释一遍的那篇。

## 推荐顺序

1. `X01` 先补 transformer circuits 总语言。
2. `X02` 看 induction heads，把 attention 图变成具体机制。
3. `X03` 看 IOI，把电路分析推进到自然语言行为。
4. `X04-X06` 进入 memory、knowledge 和 factual editing。
5. `X07` 把 interpretability、editing 和 auditing hidden objectives 接起来。

## 什么才算完成一篇扩展论文

- 不是“我读过了”。
- 也不是“我把 notebook 跑通了”。
- 而是“我在 Colab 里复现了一个教学版最小实验，并能写清这次复现支持什么、不支持什么、下一步该做什么”。

## 这条轨道和 P8 的关系

- `P5/P6` 往往要求你会复现、会写、会批判。
- `P7` 开始要求你能把不同论文放进同一种研究语言里。
- `P8` 则要求你能把这些论文转成一个子方向的判断、工具需求和研究推进节奏。

所以扩展轨道的真正作用，不只是让你“多看几篇”，而是逼你从单篇理解走向方向级理解。
