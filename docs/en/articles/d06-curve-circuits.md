# D06 Curve Circuits

- Distill article: [Curve Circuits](https://distill.pub/2020/circuits/curve-circuits/)
- Date: 2020-06-14
- Prerequisites: [D05 High-Low Frequency Detectors](d05-high-low-frequency-detectors.md)
- Mirror: [Chinese](../../zh/articles/d06-curve-circuits.md)
- Notebook: [Notebook](../../../notebooks/en/d06_curve_circuits.ipynb)
- Colab: [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/d06_curve_circuits.ipynb)

## Summary

Trace a curve circuit through mixed3a and mixed3b with live upstream importance, ablation, and a minimal proxy model.

## Notebook Scope

The notebook turns one curve circuit into a public-stack trace: find upstream channels, ablate them, and compare the real target response to a minimal proxy.

## Live Coverage

- Upstream importance search from mixed3b back to mixed3a
- Ablation on the top contributing upstream channels
- Minimal proxy-model comparison against the true target response

## Integrity Note

This notebook uses live weights, activations, and ablations from public InceptionV1. It is a teaching-scale circuit trace, not a complete rebuild of every Distill artifact.
