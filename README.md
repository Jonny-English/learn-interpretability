# Learn Interpretability: Distill Circuits

A bilingual, Colab-first repository for working through the entire [Distill 2020 Circuits thread](https://distill.pub/2020/circuits/) with strict live-only notebooks.

This repository now does one thing only:

- map the Distill Circuits thread into a single `D00-D09` sequence
- keep mirrored English and Chinese notes
- generate live notebooks for `D01-D09`
- refuse pre-rendered `figures/`, precomputed `artifacts/`, and slideshow-style walkthroughs

## Start Here

- Read the thread entry: [D00 Thread: Circuits](docs/en/articles/d00-thread-circuits.md)
- Open the first live notebook: [D01 in Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/d01_zoom_in.ipynb)
- Browse the docs index: [docs/en/index.md](docs/en/index.md)

## Why This Repo Exists

The Distill Circuits thread is still one of the clearest public introductions to neural circuits. The problem is that many readers meet it as a sequence of beautiful static pages. This repository rebuilds the thread as a runnable study path: each live notebook has to earn its claims with public weights, public data, and runtime-generated analysis.

## Distill Sequence

| ID | Article | Paper | Mode | Docs | Colab |
| --- | --- | --- | --- | --- | --- |
| D00 | Thread: Circuits | [Thread: Circuits](https://distill.pub/2020/circuits/) | reading-only | [D00](docs/en/articles/d00-thread-circuits.md) | - |
| D01 | Zoom In: An Introduction to Circuits | [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/) | live | [D01](docs/en/articles/d01-zoom-in.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/d01_zoom_in.ipynb) |
| D02 | An Overview of Early Vision in InceptionV1 | [An Overview of Early Vision in InceptionV1](https://distill.pub/2020/circuits/early-vision/) | live | [D02](docs/en/articles/d02-early-vision.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/d02_early_vision.ipynb) |
| D03 | Curve Detectors | [Curve Detectors](https://distill.pub/2020/circuits/curve-detectors) | live | [D03](docs/en/articles/d03-curve-detectors.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/d03_curve_detectors.ipynb) |
| D04 | Naturally Occurring Equivariance in Neural Networks | [Naturally Occurring Equivariance in Neural Networks](https://distill.pub/2020/circuits/equivariance/) | live | [D04](docs/en/articles/d04-equivariance.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/d04_equivariance.ipynb) |
| D05 | High-Low Frequency Detectors | [High-Low Frequency Detectors](https://distill.pub/2020/circuits/frequency-edges/) | live | [D05](docs/en/articles/d05-high-low-frequency-detectors.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/d05_high_low_frequency_detectors.ipynb) |
| D06 | Curve Circuits | [Curve Circuits](https://distill.pub/2020/circuits/curve-circuits/) | live | [D06](docs/en/articles/d06-curve-circuits.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/d06_curve_circuits.ipynb) |
| D07 | Visualizing Weights | [Visualizing Weights](https://distill.pub/2020/circuits/visualizing-weights/) | live | [D07](docs/en/articles/d07-visualizing-weights.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/d07_visualizing_weights.ipynb) |
| D08 | Branch Specialization | [Branch Specialization](https://distill.pub/2020/circuits/branch-specialization/) | live | [D08](docs/en/articles/d08-branch-specialization.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/d08_branch_specialization.ipynb) |
| D09 | Weight Banding | [Weight Banding](https://distill.pub/2020/circuits/weight-banding/) | live | [D09](docs/en/articles/d09-weight-banding.md) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/d09_weight_banding.ipynb) |

## Repo Shape

- `content/course.json`: the single source of truth for `D00-D09`
- `docs/en` and `docs/zh`: mirrored article notes and navigation pages
- `notebooks/en` and `notebooks/zh`: mirrored live notebooks for `D01-D09`
- `utils/distill_circuits.py`: shared runtime helpers for InceptionV1, stimuli, searches, and weight analysis
- `scripts/`: notebook generation, README/docs rendering, validation, link checks, audit, and smoke tests

## Regenerate And Verify

```bash
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py
python3 scripts/validate_course.py
python3 scripts/audit_realtime_policy.py
python3 scripts/check_links.py
python3 scripts/smoke_notebooks.py
```
