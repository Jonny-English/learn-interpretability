# M02 Monosemantic Features and Dictionary Learning

## Goal

Move from neurons to learned features by using a teaching-scale sparse autoencoder on synthetic activations.

## Core references

- [Towards Monosemanticity](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning)
- [Mapping the Mind of a Large Language Model](https://www.anthropic.com/research/mapping-mind-language-model)

## What to look for

- Why a sparse code can recover more interpretable directions than raw neurons.
- How a learned dictionary gives you reusable units for probing and steering.
- Why feature discovery is a modeling choice, not a magical revelation.

## Notebook and artifacts

- Notebook: `notebooks/en/m02_monosemantic_features.ipynb`
- Shared artifact: `artifacts/concept_graph.json`

## Takeaway

Dictionary learning turns interpretability from “looking at neurons” into “working with reusable features.”
