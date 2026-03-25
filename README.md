# From Circuits to Claude

[**中文版 README**](README_zh.md) ·
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Next.js Static Export](https://img.shields.io/badge/web-next.js-black.svg)](web/)

`From Circuits to Claude` is a bilingual interpretability course built for readers who know basic Python and PyTorch, but are new to mechanistic interpretability. It keeps the visual clarity of the original `circuits-zoom-in` project, then extends that intuition into Anthropic's core line of work on superposition, dictionary learning, circuit tracing, and character control.

The repository now has three synced layers:

- `content/course.json` is the single source of truth for module order, titles, prerequisites, papers, and artifacts.
- `docs/en` and `docs/zh` mirror each other exactly.
- `notebooks/en` and `notebooks/zh` mirror each other exactly, while `web/` turns the same metadata into a static course explorer.

## Course map

<!-- COURSE_TABLE:START -->
| Module | Topic | Runnable tier | Why it matters |
|---|---|---|---|
| `M00` | Vision Circuits Warm-up | `warmup` | Reuse the original Zoom In visual-circuits material to establish intuition for features, circuits, and interventions. |
| `M01` | Superposition | `cpu-colab` | Use a sparse toy model to understand why neurons are often not clean semantic units. |
| `M02` | Monosemantic Features and Dictionary Learning | `cpu-colab` | Use a teaching-scale SAE to understand the shift from neuron-centric to feature-centric analysis. |
| `M03` | Feature Probes and Steering | `cpu-colab` | Show, in a small runnable experiment, how features can support both reading and intervention. |
| `M04` | Circuit Tracing | `artifact-guided` | Learn to read local computation paths in an LLM through precomputed attribution graphs. |
| `M05` | Character and Control | `artifact-guided` | Connect interpretability to character control through persona vectors and frontier reading. |
<!-- COURSE_TABLE:END -->

## Learning design

- `M00` keeps the original visual circuits notebook as a warm-up so readers first see interpretable circuits in a concrete visual model.
- `M01-M03` are fully runnable CPU labs covering superposition, monosemantic features, and feature probes/steering.
- `M04-M05` use precomputed artifacts to teach attribution graphs and persona vectors without requiring proprietary models or large-scale tracing runs.
- `Timeline` and `concept graph` views in `web/` help readers connect papers, ideas, and labs without losing the runnable path.

## Quick start

```bash
pip install -r requirements.txt

# Refresh derived assets after editing course metadata
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py

# Validate metadata, docs, notebook parity, and links
python3 scripts/validate_course.py
python3 scripts/check_links.py

# Execute all generated notebooks as a smoke test
python3 scripts/smoke_notebooks.py
```

To build the static site:

```bash
cd web
npm install
npm run build
```

## Repo structure

```text
.
├── content/               # Course metadata and glossary
├── docs/                  # Mirrored zh/en concept docs
├── notebooks/             # Legacy notebook + mirrored course notebooks
├── artifacts/             # Shared JSON artifacts for notebooks and web
├── web/                   # Static Next.js explorer
├── scripts/               # Notebook generation and validation
├── figures/               # Legacy visual circuit figures reused by M00
└── utils/                 # Shared plotting helpers from the original tutorial
```

## Legacy material

The original notebooks remain in place:

- `notebooks/circuits_zoom_in_en.ipynb`
- `notebooks/circuits_zoom_in_zh.ipynb`

They now serve as the long-form source material behind `M00`.

## References

The core curriculum is anchored in official Anthropic research pages as of `2026-03-25`, with the interpretability team page as the index:

- [Anthropic Interpretability team page](https://www.anthropic.com/research/team/interpretability)
- [Toy Models of Superposition](https://www.anthropic.com/research/toy-models-of-superposition)
- [Towards Monosemanticity](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning)
- [Mapping the Mind of a Large Language Model](https://www.anthropic.com/research/mapping-mind-language-model)
- [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)

## License

[MIT](LICENSE)
