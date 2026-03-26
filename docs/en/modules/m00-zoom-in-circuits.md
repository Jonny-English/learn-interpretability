# M00 Zoom In: An Introduction to Circuits

## Goal

Run a live, teaching-scale visual-circuits reproduction on a public InceptionV1 model.

## Core reference

- [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/)

## What to look for

- A single neuron can align with a recognizable visual pattern under live activation maximization.
- That same neuron can be checked against real images instead of only a synthetic visualization.
- Orientation tuning can be measured directly rather than asserted from a static figure.
- A small circuit story can be grounded in learned weights instead of a hand-drawn diagram.

## Notebook and artifacts

- Notebook: `notebooks/en/m00_zoom_in_circuits.ipynb`
- The notebook generates its own feature visualizations, CIFAR validation panels, tuning curves, and upstream-weight trace
- Extended background: `notebooks/circuits_zoom_in_en.ipynb`

## Self-check questions

- Explain feature, circuit, and intervention in your own words and state how they relate to one another.
- Why is the visual-circuits story such a good beginner picture, yet a risky one to transfer directly to language models?
- If this article gives the starting intuition for later interpretability, which part of the picture breaks first, and why?

## Takeaway

This notebook now earns the visual-circuits intuition live. The picture is still cleaner than language-model interpretability, but it is no longer just a static walkthrough.
