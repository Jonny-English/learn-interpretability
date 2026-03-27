# D09 Weight Banding

- Distill article: [Weight Banding](https://distill.pub/2020/circuits/weight-banding/)
- Date: 2020-09-01
- Prerequisites: [D08 Branch Specialization](d08-branch-specialization.md)
- Mirror: [Chinese](../../zh/articles/d09-weight-banding.md)
- Notebook: [Notebook](../../../notebooks/en/d09_weight_banding.ipynb)
- Colab: [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/d09_weight_banding.ipynb)

## Summary

Analyze the final classifier weight matrix live: reorder classes and channels, visualize bands, and compare against shuffled baselines.

## Notebook Scope

This notebook treats banding as a live weight-analysis problem on the public classifier head rather than a static export of a finished figure.

## Live Coverage

- Final-layer weight-matrix reordering
- Band-span versus shuffled-baseline measurements
- Candidate class-group inspection from the reordered matrix

## Integrity Note

The matrix views and banding scores are computed live from the public classifier head. This is a runtime analysis notebook, not a bundled static export.
