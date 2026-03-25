# M03 特征探针与 Steering

## 目标

通过一个可运行的小实验，展示 learned feature 既能拿来读，也能拿来改。

## 核心参考

- [Using dictionary learning features as classifiers](https://www.anthropic.com/research/features-as-classifiers)
- [Evaluating feature steering](https://www.anthropic.com/research/evaluating-feature-steering)

## 重点观察

- 简单分类器可以直接作用在 feature activation 上，而不是原始隐藏状态。
- 干预强度并非越大越好，通常存在 sweet spot。
- 每一次 steering 都有副作用，off-target effects 不是补充问题，而是主问题。

## Notebook 与 artifact

- Notebook：`notebooks/zh/m03_feature_probes_steering.ipynb`
- 共享 artifact：`artifacts/concept_graph.json`

## 模块结论

当 feature 既能解释又能干预时，它就从“描述单位”变成了“操作单位”。
