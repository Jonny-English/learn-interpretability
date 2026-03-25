# M01 Superposition

## Goal

Show why neurons are often poor semantic units: many concepts can be packed into fewer dimensions, forcing overlap.

## Core reference

- [Toy Models of Superposition](https://www.anthropic.com/research/toy-models-of-superposition)

## What to look for

- Sparse concepts can still compress into a smaller hidden space.
- The model can reconstruct inputs while mixing concepts across dimensions.
- “A neuron means one thing” is often the wrong default.

## Notebook and artifacts

- Notebook: `notebooks/en/m01_superposition.ipynb`
- Shared artifact: `artifacts/concept_graph.json`

## Takeaway

Superposition motivates the rest of the course. Once readers see why semantic cleanliness is hard, they are ready for dictionary learning.
