# M04 Circuit Tracing

## Goal

Teach readers how to inspect an attribution graph and explain a small computation path without pretending to reproduce a full production tracing stack.

## Core references

- [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)
- [Open-sourcing circuit tracing tools](https://www.anthropic.com/research/open-source-circuit-tracing)

## What to look for

- Inputs, intermediate features, and outputs can be linked through weighted contribution paths.
- A good tracing artifact is selective: it shows a useful slice, not the whole network.
- “Explaining the answer” and “explaining the internal route to the answer” are different tasks.

## Notebook and artifacts

- Notebook: `notebooks/en/m04_circuit_tracing.ipynb`
- Shared artifact: `artifacts/m04_attribution_graph.json`

## Takeaway

This module shifts interpretability from isolated features to local computation graphs.
