# X07 Auditing Hidden Objectives

## Goal

Place interpretability, editing, behavior evaluation, and auditing inside one judgment frame.

## Core reference

- [Auditing Language Models for Hidden Objectives](https://www.anthropic.com/research/auditing-hidden-objectives)

## Why it matters for the P8 path

- This pushes the question from "can I understand the model?" toward "what might the model be optimizing secretly?"
- If you want to move from interpretability reading into risk-facing research judgment, this is one of the clearest transition points.

## Notebook and deliverable

- Notebook: `notebooks/extensions/en/x07_auditing_hidden_objectives.ipynb`
- Deliverable: one auditing-toy reproduction plus one memo on how behavior signals, internal evidence, and stop conditions should close the loop.

## Self-check

- Why is abnormal behavior alone often insufficient for judging whether a hidden objective exists?
- In your toy audit, which internal signal best closes the loop with behavior evidence?
- If you were handing auditing work to a team, what would you write as the stop condition?

## Extension conclusion

This paper is where the project most clearly touches real auditing judgment, because it forces you to turn interpretability evidence into executable risk reasoning.
