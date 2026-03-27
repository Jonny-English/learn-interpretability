# D03 Curve Detectors

- Distill article: [Curve Detectors](https://distill.pub/2020/circuits/curve-detectors)
- Date: 2020-04-21
- Prerequisites: [D02 An Overview of Early Vision in InceptionV1](d02-early-vision.md)
- Mirror: [Chinese](../../zh/articles/d03-curve-detectors.md)
- Notebook: [Notebook](../../../notebooks/en/d03_curve_detectors.ipynb)
- Colab: [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/d03_curve_detectors.ipynb)

## Summary

Search for curve-preferring channels live, compare line/arc/curvature stimuli, and validate the best channel on real images.

## Notebook Scope

Instead of replaying a static story, the notebook searches the model for curve-preferring channels at runtime and then tests what makes them special.

## Live Coverage

- Curve-preference search inside mixed3b
- Line versus arc versus circle response comparisons
- Real-image validation for the strongest curve channel

## Integrity Note

The search space and validation set are smaller than the Distill write-up, but the detector discovery and measurements are generated live on the public model.
