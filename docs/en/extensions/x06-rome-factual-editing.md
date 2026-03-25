# X06 ROME Factual Editing

## Goal

Push from "explanation" into "controllable editing" while tracking edit success, locality, and collateral damage together.

## Core reference

- [Locating and Editing Factual Associations in GPT](https://arxiv.org/abs/2202.05262)

## Why it matters for the P8 path

- Reading graphs is not enough. Real research also needs to discuss whether an edit is stable, local, and worth shipping.
- This paper pulls interpretability toward intervention and product-facing judgment.

## Notebook and deliverable

- Notebook: `notebooks/extensions/en/x06_rome_factual_editing.ipynb`
- Deliverable: one rank-one factual edit log plus one edit memo discussing success, locality, and side effects.

## Self-check

- Why is "the edit worked" still not enough to prove the method is reliable?
- In your toy rank-one update, where does the clearest collateral damage appear?
- If locality and edit success conflict, which would you protect first?

## Extension conclusion

This paper starts building the habit that a research conclusion is not only "can it be changed?" but also "what are the cost and boundary after the change?"
