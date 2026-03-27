# D07 Visualizing Weights

- Distill article: [Visualizing Weights](https://distill.pub/2020/circuits/visualizing-weights/)
- Date: 2020-07-13
- Prerequisites: [D06 Curve Circuits](d06-curve-circuits.md)
- Mirror: [Chinese](../../zh/articles/d07-visualizing-weights.md)
- Notebook: [Notebook](../../../notebooks/en/d07_visualizing_weights.ipynb)
- Colab: [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/d07_visualizing_weights.ipynb)

## Summary

Visualize real InceptionV1 weights directly and compare what weight views reveal versus what feature visualizations reveal.

## Notebook Scope

This notebook stays entirely in runtime-generated weight views and pairs them with live feature renders so the comparison is grounded in the same channels.

## Live Coverage

- Direct visualization of first-layer RGB filters
- Energy-map views for deeper convolutional filters
- Weight-view versus feature-view comparisons on matched channels

## Integrity Note

All visualizations are generated at runtime from public model weights. No pre-rendered weight figures are bundled in the repository.
