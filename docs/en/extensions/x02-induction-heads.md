# X02 Induction Heads

## Goal

Push beyond attention heatmaps into a concrete copying mechanism and understand why repeated context gives transformers an in-context copying behavior.

## Core reference

- [In-context Learning and Induction Heads](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html)

## Why it matters for direction-level growth

- This paper forces you to separate a hot pattern from a mechanism.
- For serious growth beyond single-paper summaries, the ability to turn a pattern story into a mechanism story is a major dividing line.

## Notebook and deliverable

- Notebook: `notebooks/extensions/en/x02_induction_heads.ipynb`
- Deliverable: one copying-task reproduction log plus one paragraph explaining why an induction head is more like a mechanism than a single hotspot.

## Self-check

- Why does "one position looks backward" still not count as induction?
- In your toy copying task, how does performance change as the repeat distance changes?
- What does an induction head lose if there is no earlier matching cue?

## Extension conclusion

This paper turns attention from a visualization object into a behavior mechanism that can actually be argued about.
