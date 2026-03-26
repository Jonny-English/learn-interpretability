# Learn Interpretability

[**中文版 README**](README_zh.md) ·
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ·
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

`Learn Interpretability` is a bilingual, Colab-first training repo for readers who know basic Python and PyTorch but are new to mechanistic interpretability. The project is paper-guided and live-code-first: every core paper has a mirrored note, and every honestly runnable item has a paired Colab notebook.

If the repository saves you time, gives you a usable path, or helps you stop random paper-hopping, star it.

## Preface

This repository starts from a simple refusal:
we do not want to spend the large-model era as passive users of systems we do not understand.

The most important technology of our time is becoming more capable, more agentic, and more deeply woven into research, software, and decision-making. If we only learn how to prompt it, consume it, or route around it, we stay downstream from the real question. The real question is what these models are representing, what mechanisms they are actually using, where they break, and how human beings can still earn the right to understand, steer, and control them.

That is why this project is not just a reading list and not just a notebook collection. It is a training ground. It is for readers who are willing to stop admiring the black box from the outside and start opening it, reproducing its behaviors, tracing its internals, writing down their judgments, and turning scattered curiosity into disciplined research work.

You do not need to begin as an expert. You do need to begin seriously.

## Start Here

- New to notebooks, plots, or experiment discipline: start with `F00 -> F03`
- Already comfortable with basic PyTorch and notebooks: start with the live core `M00 -> M05`
- Not sure whether the repo fits you: use the [first-week proof path](docs/en/program/first-week-checklist.md)
- Want the full target instead of just a few Colabs: read [research-ready.md](docs/en/program/research-ready.md) and [p6-graduation-checklist.md](docs/en/program/p6-graduation-checklist.md)

## What This Repo Promises

- `Bilingual`: English and Chinese stay structurally mirrored
- `Colab-first`: the main runnable path is designed for CPU or free Colab
- `Live-code only`: runnable work must generate outputs at runtime; anything else is marked `reading-only`
- `P6-ready target`: the honest claim is not “finish a few notebooks”; it is “an ordinary undergraduate can reach a credible `P6-ready` result after the full path and evidence gates”

## Repo Snapshot

- `4` foundation labs
- `5` live core notebooks
- `7` runnable extension drills
- `32` notebooks smoke-tested
- `180-250` focused hours for the full `P6-ready` path

## Foundations

Use these labs if setup, plots, attention reading, or experiment discipline still feel unstable.

<!-- FOUNDATION_TABLE:START -->
| ID | Foundation Lab | Notebook | Colab | Runnable tier | What it repairs |
|---|---|---|---|---|---|
| `F00` | Environment, Plots, and Baseline Discipline | [Open](notebooks/foundations/en/f00_environment_plots_baselines.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/foundations/en/f00_environment_plots_baselines.ipynb) | `cpu-colab` | Set up a local or Colab workflow, read loss curves, and learn the minimum discipline of baselines, variants, and logging. |
| `F01` | Transformer Shapes and Attention Reading | [Open](notebooks/foundations/en/f01_transformer_shapes_attention.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/foundations/en/f01_transformer_shapes_attention.ipynb) | `cpu-colab` | Use a tiny attention example to build intuition for tokens, heads, QK scores, softmax, and residual updates. |
| `F02` | Vector Geometry, Features, and Probes | [Open](notebooks/foundations/en/f02_vector_geometry_features_probes.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/foundations/en/f02_vector_geometry_features_probes.ipynb) | `cpu-colab` | Practice cosine, projection, directional similarity, and linear probes on toy vectors to build the geometric floor under the feature language. |
| `F03` | Sweeps, Ablations, and Failure Analysis | [Open](notebooks/foundations/en/f03_sweeps_ablations_failure_analysis.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/foundations/en/f03_sweeps_ablations_failure_analysis.ipynb) | `cpu-colab` | Use one small experiment to practice sweeps, ablations, stop conditions, and failure analysis so 'I can run notebooks' becomes 'I can design a minimal experiment.' |
<!-- FOUNDATION_TABLE:END -->

## Core Paper Track

This is the main article path. `reading-only` means the note stays in the repo, but the notebook is intentionally not generated because it would not meet the strict live-code policy.

<!-- COURSE_TABLE:START -->
| ID | Paper | Date | Status | Notebook | Colab | Runnable tier | What you will do |
|---|---|---|---|---|---|---|---|
| `M00` | Zoom In: An Introduction to Circuits | `2020-03-10` | `method-lab` | [Open](notebooks/en/m00_zoom_in_circuits.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/m00_zoom_in_circuits.ipynb) | `cpu-colab` | Run live feature visualization, real-image validation, orientation tuning, and a small circuit trace on public InceptionV1. |
| `M01` | Toy Models of Superposition | `2022-09-14` | `paper-faithful` | [Open](notebooks/en/m01_toy_models_superposition.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/m01_toy_models_superposition.ipynb) | `cpu-colab` | Use a minimal toy model to see why neurons can mix multiple semantics. |
| `M02` | Towards Monosemanticity | `2023-10-05` | `method-lab` | [Open](notebooks/en/m02_towards_monosemanticity.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/m02_towards_monosemanticity.ipynb) | `cpu-colab` | Use a teaching-scale sparse autoencoder to see why a feature view can be cleaner than a neuron view. |
| `M03` | Mapping the Mind of a Large Language Model | `2024-05-21` | `reading-only` | Reading | - | `reading-only` | Browse a teaching-scale feature catalog to understand what it means to discover many reusable features. |
| `M04` | Using Dictionary Learning Features as Classifiers | `2024-10-16` | `method-lab` | [Open](notebooks/en/m04_features_as_classifiers.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/m04_features_as_classifiers.ipynb) | `cpu-colab` | Treat features as classifier inputs and study where readout ability comes from. |
| `M05` | Evaluating Feature Steering | `2024-10-25` | `method-lab` | [Open](notebooks/en/m05_evaluating_feature_steering.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/en/m05_evaluating_feature_steering.ipynb) | `cpu-colab` | Sweep steering strength to inspect target gain, sweet spots, and off-target costs. |
| `M06` | Tracing the Thoughts of a Large Language Model | `2025-03-27` | `reading-only` | Reading | - | `reading-only` | Read a shared attribution graph and learn to describe one local computation path plus the public tooling gaps that still block a live reproduction. |
| `M07` | Open-sourcing Circuit Tracing Tools | `2025-05-29` | `reading-only` | Reading | - | `reading-only` | Inspect tracing artifacts and workflow stages to understand the tooling layer behind the analysis. |
| `M08` | Persona Vectors | `2025-08-01` | `reading-only` | Reading | - | `reading-only` | Read a shared persona artifact, compare before/after trait shifts, and state what is still missing for an honest live reproduction. |
| `M09` | Signs of Introspection in Large Language Models | `2025-10-29` | `reading-only` | Reading | - | `reading-only` | Compare self-report and behavior signals in teaching data to discuss what 'signs of introspection' actually mean. |
| `M10` | The Assistant Axis | `2026-01-19` | `reading-only` | Reading | - | `reading-only` | Project multiple assistant styles onto one axis and inspect the problem of stabilizing character. |
<!-- COURSE_TABLE:END -->

## Research-Ready Layer

Use these docs when your goal shifts from “I followed the notebook” to “I can work like a junior interpretability researcher.”

- [Research-ready overview](docs/en/program/research-ready.md)
- [First-week proof path](docs/en/program/first-week-checklist.md)
- [Capability arc and P6 evidence gates](docs/en/program/capability-arc.md)
- [P6 graduation checklist](docs/en/program/p6-graduation-checklist.md)
- [12-week bootcamp](docs/en/program/week-by-week.md)
- [Research playbook](docs/en/program/research-playbook.md)
- [Independent research sprints](docs/en/program/independent-sprints.md)

## Reference Outputs

Use these when you need to calibrate whether your notes, logs, or proposals are dense enough.

<!-- REFERENCE_TABLE:START -->
| ID | Reference Output | File | When to use it |
|---|---|---|---|
| `R01` | Reference Paper Brief | [examples/en/reference_paper_brief.md](examples/en/reference_paper_brief.md) | Use it after independent sprint T1 or any paper reading note that needs to be compressed for a mentor or peer. |
| `R02` | Reference Experiment Log | [examples/en/reference_experiment_log.md](examples/en/reference_experiment_log.md) | Use it after any sweep, ablation, or feature-steering notebook. |
| `R03` | Reference Artifact Critique | [examples/en/reference_artifact_critique.md](examples/en/reference_artifact_critique.md) | Use it for M03, M07, M09, M10, or independent sprint T3. |
| `R04` | Reference Two-Week Proposal | [examples/en/reference_two_week_proposal.md](examples/en/reference_two_week_proposal.md) | Use it before a capstone or independent sprint T4 to calibrate the density of your proposal. |
<!-- REFERENCE_TABLE:END -->

## Extension Track

The Anthropic core is not enough by itself. After the core, continue into transformer circuits, memory/editing, and auditing through the extension notes and Colabs. Full reading order lives in [docs/en/extensions/index.md](docs/en/extensions/index.md).

<!-- EXTENSION_TABLE:START -->
| ID | Extension Paper | Status | Note | Notebook | Colab |
|---|---|---|---|---|---|
| `X01` | A Mathematical Framework for Transformer Circuits | `method-lab` | [Note](docs/en/extensions/x01-transformer-circuits-framework.md) | [Open](notebooks/extensions/en/x01_transformer_circuits_framework.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/en/x01_transformer_circuits_framework.ipynb) |
| `X02` | In-context Learning and Induction Heads | `method-lab` | [Note](docs/en/extensions/x02-induction-heads.md) | [Open](notebooks/extensions/en/x02_induction_heads.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/en/x02_induction_heads.ipynb) |
| `X03` | Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 Small | `method-lab` | [Note](docs/en/extensions/x03-ioi-circuit.md) | [Open](notebooks/extensions/en/x03_ioi_circuit.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/en/x03_ioi_circuit.ipynb) |
| `X04` | Transformer Feed-Forward Layers Are Key-Value Memories | `method-lab` | [Note](docs/en/extensions/x04-ffn-key-value-memories.md) | [Open](notebooks/extensions/en/x04_ffn_key_value_memories.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/en/x04_ffn_key_value_memories.ipynb) |
| `X05` | Knowledge Neurons in Pretrained Transformers | `method-lab` | [Note](docs/en/extensions/x05-knowledge-neurons.md) | [Open](notebooks/extensions/en/x05_knowledge_neurons.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/en/x05_knowledge_neurons.ipynb) |
| `X06` | Locating and Editing Factual Associations in GPT | `method-lab` | [Note](docs/en/extensions/x06-rome-factual-editing.md) | [Open](notebooks/extensions/en/x06_rome_factual_editing.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/en/x06_rome_factual_editing.ipynb) |
| `X07` | Auditing Language Models for Hidden Objectives | `method-lab` | [Note](docs/en/extensions/x07-auditing-hidden-objectives.md) | [Open](notebooks/extensions/en/x07_auditing_hidden_objectives.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/extensions/en/x07_auditing_hidden_objectives.ipynb) |
<!-- EXTENSION_TABLE:END -->

## Local Workflow

```bash
pip install -r requirements.txt
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py
python3 scripts/validate_course.py
python3 scripts/audit_realtime_policy.py
python3 scripts/check_links.py
python3 scripts/smoke_notebooks.py
```

If you only want to learn, open the Colab links above and ignore local setup until you need it.

## Project Navigation

- [English docs index](docs/en/index.md)
- [Chinese docs index](docs/zh/index.md)
- [English repo map](docs/en/repo-map.md)
- [Chinese repo map](docs/zh/repo-map.md)

## License

[MIT](LICENSE)
