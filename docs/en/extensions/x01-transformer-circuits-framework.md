# X01 Mathematical Framework for Transformer Circuits

## Goal

Put residual streams, attention, MLPs, and composition into one language so that later tracing, editing, and auditing work does not collapse into a pile of isolated terms.

## Core reference

- [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html)

## Why it matters for the P8 path

- This moves you from "I can read one graph" to "I can describe how a whole class of mechanisms composes."
- Without this language, many later explanations stay at the level of listing parts instead of making direction-level judgments.

## Notebook and deliverable

- Notebook: `notebooks/extensions/en/x01_transformer_circuits_framework.ipynb`
- Deliverable: one framework brief plus one paragraph that rewrites the M06 toy trace in residual-stream language.

## Self-check

- Why is residual-stream language better than layer-local description when you want to talk about mechanism?
- In your toy reproduction, which composition step actually changed the final readout?
- If an explanation can only list head names and cannot describe composition, what is it missing?

## Extension conclusion

This paper is not just one more terminology list. It gives you an explanatory grammar that should stay reusable across the later papers.
