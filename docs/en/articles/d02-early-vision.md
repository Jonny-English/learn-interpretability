# D02 An Overview of Early Vision in InceptionV1

- Distill article: [An Overview of Early Vision in InceptionV1](https://distill.pub/2020/circuits/early-vision/)
- Date: 2020-03-31
- Prerequisites: [D01 Zoom In: An Introduction to Circuits](d01-zoom-in.md)
- Mirror: [Chinese](../../zh/articles/d02-early-vision.md)
- Notebook: [Notebook](../../../notebooks/en/d02_early_vision.ipynb)
- Colab: [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/d02_early_vision.ipynb)

## Summary

Survey early InceptionV1 layers with live feature renders, family-response statistics, and layer-by-layer channel snapshots.

## Notebook Scope

The notebook samples early layers directly from a pretrained InceptionV1 and summarizes how feature families broaden from edges to small motifs.

## Live Coverage

- Layer-by-layer feature render gallery
- Synthetic family response heatmap across early layers
- Real-image activation snapshots for selected channels

## Integrity Note

This notebook uses live renders and measured activations on the public model. The scope is teaching-scale, but every figure is produced at runtime.
