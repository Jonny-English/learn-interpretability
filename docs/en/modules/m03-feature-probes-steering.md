# M03 Feature Probes and Steering

## Goal

Demonstrate that learned features are useful both for measurement and for intervention.

## Core references

- [Using dictionary learning features as classifiers](https://www.anthropic.com/research/features-as-classifiers)
- [Evaluating feature steering](https://www.anthropic.com/research/evaluating-feature-steering)

## What to look for

- A simple classifier can operate on feature activations instead of raw hidden states.
- Steering is strongest when the intervention is aligned and not too large.
- Every intervention introduces tradeoffs, including off-target effects.

## Notebook and artifacts

- Notebook: `notebooks/en/m03_feature_probes_steering.ipynb`
- Shared artifact: `artifacts/concept_graph.json`

## Takeaway

If features can both explain and steer behavior, they become an actionable unit of analysis rather than just a descriptive one.
