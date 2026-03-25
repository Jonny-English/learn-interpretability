# X05 Knowledge Neurons

## 目标

练习把“知识”局部化到一组更可干预的单元上，并区分相关线索与因果承载位点。

## 核心参考

- [Knowledge Neurons in Pretrained Transformers](https://arxiv.org/abs/2104.08696)

## 为什么它对 P8 路径重要

- 这篇会逼你认真区分 readout、localization 和 causality。
- 如果未来要做更强的 editing 或 auditing，不能把高分单元直接当因果结论。

## Notebook 与交付

- Notebook：`notebooks/extensions/zh/x05_knowledge_neurons.ipynb`
- 交付：1 份 neuron 打分与消融记录，外加 1 段说明高分 neuron 为什么仍然不自动等于因果解释。

## 验收题

- 为什么一个 neuron 分数很高，仍然可能只是相关线索？
- 在你的 toy 消融里，哪种结果最支持“局部承载”的解释？
- knowledge neurons 和 feature probes 在解释力度上最大的差别是什么？

## 扩展结论

这篇的价值不在于“终于找到知识在哪”，而在于训练你如何对局部化 claim 保持严格标准。
