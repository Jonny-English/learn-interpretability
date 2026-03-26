# X02 Induction Heads

## 目标

把注意力图推进到一个具体复制机制上，理解 repeated context 为什么会让 transformer 展现出 in-context copying 行为。

## 核心参考

- [In-context Learning and Induction Heads](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html)

## 为什么它对方向级成长重要

- 这篇会强迫你区分“热点图案”和“机制”。
- 对真正超出单篇复述的成长来说，能不能把 pattern 说成 mechanism，是很关键的分水岭。

## Notebook 与交付

- Notebook：`notebooks/extensions/zh/x02_induction_heads.ipynb`
- 交付：1 份 copying-task 复现记录，外加 1 段说明 induction head 为什么比单个热点更像机制。

## 验收题

- 为什么“某个位置向前看了”还不等于发现了 induction？
- 你的 toy copying 任务里，重复距离变化时表现怎么变？
- 如果没有前序匹配线索，induction head 会失去什么？

## 扩展结论

这篇让 attention 从“图像可视化对象”变成“可被论证的行为机制”。
