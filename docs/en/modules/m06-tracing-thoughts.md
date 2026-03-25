# M06 Tracing the Thoughts of a Large Language Model

## Goal

Learn how to read an attribution graph and explain one computation path from input to answer without pretending that this repository has a fully public real-time tracing stack.

## Core reference

- [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)

## What to look for

- Inputs, intermediate features, and outputs can be linked by weighted paths.
- A useful trace is selective; it does not need the whole model at once.
- Explaining a route through the model is different from paraphrasing the final answer.

## Status

- `reading-only` under the strict realtime policy
- This repository does not currently ship a live notebook here because that would depend on precomputed attribution artifacts.
- Shared reference artifact: `artifacts/m06_attribution_graph.json`

## Self-check questions

- Explain the three most important contribution paths in the graph without just reading the labels back.
- What conclusion does this graph support, and what conclusion does it clearly not support?
- If you could run one follow-up experiment to reduce the graph's ambiguity, what would it be?

## Takeaway

This paper shifts the focus from isolated features to local computation graphs, and in this repository it is now treated as reading and critique until a public real-time tracing stack exists.
