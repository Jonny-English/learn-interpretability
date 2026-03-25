# From Circuits to Claude

[**中文版 README**](README_zh.md) ·
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

`From Circuits to Claude` is a bilingual, Colab-first interpretability training project for readers who know basic Python and PyTorch but are new to mechanistic interpretability. The repository is now paper-reproduction-first: every core paper in the path has one mirrored note, and every honestly runnable paper gets one Colab notebook.

The repository has three core synced layers:

- `content/course.json` is the single source of truth for order, prerequisites, links, and artifacts.
- `docs/en` and `docs/zh` mirror each other exactly.
- `notebooks/en` and `notebooks/zh` mirror each other exactly so the whole core path can be run in Colab or locally.

It now also has four reinforcement layers:

- a `Pre-P4 foundation pack` that repairs environment setup, attention-shape intuition, vector geometry, and experiment discipline
- a `research-ready path` with a 12-week bootcamp, memo templates, a rubric, and self-directed research sprints
- a `reference-output layer` that calibrates deliverable quality against concrete examples
- an `extension reproduction track` that widens the research view beyond the Anthropic core arc with more Colab reproductions

The point is to stop the most common self-study failure mode: finishing the reading without building reproduction habits, writing habits, or research judgment.

Strict rule from this point on:

- only code that generates its outputs live at runtime counts as runnable work
- anything that still depends on precomputed JSON artifacts is downgraded to `reading-only`
- a simplified live notebook may exist as a `method-lab`, but it may not be advertised as a full paper reproduction

## Who This Project Is For

- It is beginner-friendly for readers with basic Python and PyTorch but little or no mechanistic-interpretability background.
- It is for readers who want to move from "I can follow a few papers" to "I can reproduce papers in Colab, critique them, and eventually own a scoped line of interpretability work."
- It is not designed as passive popularization. You are expected to write reading notes, experiment logs, and short memos.

The target output of this repository is not "a person who has seen many papers." The north-star target is a long-horizon path toward the capability density of an Alibaba-style `P8` interpretability researcher.

To reduce ambiguity, the ladder below is rewritten to match the public, commonly used understanding of Alibaba-style `P4-P12` technical levels:

| Level | Capability |
|---|---|
| `P4` | Entry-level engineer: can work under explicit guidance, run notebooks, reproduce setup steps, and explain basic concepts, but still lacks strong independent research judgment. |
| `P5` | Engineer: can independently reproduce a scoped result, keep experiment logs, compare baseline versus variant, and write basic conclusions. |
| `P6` | Senior engineer / strong IC starting point: can take a clearly scoped research task in a lab, study group, or independent project, read papers, reproduce results, critique evidence, and propose the next experiment. |
| `P7` | Expert: can define a small direction, design a two-week research plan, and close the loop across experiments, tools, and reporting. |
| `**P8**` | Senior expert: can own a research sub-area or tooling line and create sustained technical leverage across multiple collaborators. |
| `P9` | Principal / senior expert: can define a medium-term research thread and influence methods, judgment, and collaboration across teams. |
| `P10` | Fellow / organization-level expert: can set organization-level research direction, choose key methodological bets, and influence product and safety strategy. |
| `P11` | Company-level top technical leader: can define long-term agenda, standards, and talent systems. |
| `P12` | Industry-shaping figure: can significantly change how the field frames the technology and its control problems. |

On that scale, no single teaching project should claim "finish 12 weeks and become `P10`." In Alibaba-style language, `P10` is already a very high organization-level expert bar.

The correct framing is staged:

- `F00-F03` plus the early core move a true beginner from below `P4` toward `P4/P5`.
- `M00-M10` plus the research-ready bootcamp build a credible `P5/P6` floor.
- `X01-X07`, repeated capstones, and portfolio work are what continue the path toward `P7/P8`.

So the repository is `P8`-oriented in its north star, but it gets there by building floors rather than by pretending one pass through the material equals a senior-expert title. Under the strict policy, only `paper-faithful` and `method-lab` items count as live code.

## Two Starting Lines

To serve both true beginners and readers with some prior foundation, the repository now defines two explicit runways:

### Beginner Runway

- Best for: readers who know some Python but still have unstable environment setup, math fluency, and experiment discipline.
- Entry signal: you still cannot run notebooks reliably, read basic plots comfortably, or explain what a baseline is.
- Recommended path: finish `F00-F03` plus `M00` and `M01`, make the reading-note and experiment-log templates feel routine, then enter the full course and later the extension reproductions.
- Target: first move toward something close to Alibaba-style `P4`, then use the core and extension tracks to enter the `P5/P6` floor and eventually the `P7/P8` path.

### Prepared Runway

- Best for: readers who can already run notebooks, use basic PyTorch, and read common plots, but lack a systematic interpretability roadmap.
- Entry signal: you can already do simple reproductions and keep basic notes, but you do not yet have a coherent research path.
- Recommended path: move quickly through `M00 → M06`, then switch into research-ready mode early, start writing memos plus failure analysis, and continue into the extension reproductions.
- Target: move directly into a `P5/P6` core and use the extension track, proposals, and capstones to keep growing toward `P7/P8`.

## Why Learn This

After the spinning jenny appeared, the center of value in textile work stopped being "who has the most refined hand-spinning technique." It shifted toward:

- who understood the machine
- who could use the machine well
- who could modify the machine
- who could reorganize production around the machine

The large-model era creates the same shift.

When models can already perform a large amount of local cognitive work, the scarce skill is no longer only "manually weaving every sentence, reasoning step, or code block by hand." The scarce skill becomes:

- understanding what the model is representing internally
- understanding why it succeeds and why it fails
- understanding which directions can be read out, intervened on, and controlled safely
- understanding how to turn those judgments into research, tooling, and product decisions

So learning interpretability is not just learning a set of paper summaries. It is learning how to understand and steer machine intelligence once the machine itself becomes the central productive object.

Put more precisely: AI is also just another layer of abstraction over lower-level computation.

- Assembly is a layer of abstraction over machine code.
- High-level languages are another layer over assembly.
- Large models and AI systems are one more layer of abstraction built on top of those computational stacks.

So the right focus is no longer only the fine-grained craft of manually executing the old workflow. The focus shifts toward:

- what capability this abstraction layer exposes
- what mechanism this abstraction layer hides
- how we understand, use, debug, and control this abstraction layer

That is also why this repository is not only about paper summaries. It is about Colab reproductions, experiments, artifacts, steering, tracing, editing, auditing, and research communication.

## Pre-P4 Foundation Pack

If notebooks, plots, attention shapes, or baseline/sweep/ablation discipline still feel unstable, do not rush into the paper core. Repair those four labs first.

<!-- FOUNDATION_TABLE:START -->
| ID | Foundation Lab | Notebook | Colab | Runnable tier | What it repairs |
|---|---|---|---|---|---|
| `F00` | Environment, Plots, and Baseline Discipline | [Open](notebooks/foundations/en/f00_environment_plots_baselines.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/foundations/en/f00_environment_plots_baselines.ipynb) | `cpu-colab` | Set up a local or Colab workflow, read loss curves, and learn the minimum discipline of baselines, variants, and logging. |
| `F01` | Transformer Shapes and Attention Reading | [Open](notebooks/foundations/en/f01_transformer_shapes_attention.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/foundations/en/f01_transformer_shapes_attention.ipynb) | `cpu-colab` | Use a tiny attention example to build intuition for tokens, heads, QK scores, softmax, and residual updates. |
| `F02` | Vector Geometry, Features, and Probes | [Open](notebooks/foundations/en/f02_vector_geometry_features_probes.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/foundations/en/f02_vector_geometry_features_probes.ipynb) | `cpu-colab` | Practice cosine, projection, directional similarity, and linear probes on toy vectors to build the geometric floor under the feature language. |
| `F03` | Sweeps, Ablations, and Failure Analysis | [Open](notebooks/foundations/en/f03_sweeps_ablations_failure_analysis.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/foundations/en/f03_sweeps_ablations_failure_analysis.ipynb) | `cpu-colab` | Use one small experiment to practice sweeps, ablations, stop conditions, and failure analysis so 'I can run notebooks' becomes 'I can design a minimal experiment.' |
<!-- FOUNDATION_TABLE:END -->

## One Article, One Colab

Each row below corresponds to exactly one paper and one notebook. Every paired note and Colab notebook now also includes self-check questions so readers can test whether they actually absorbed the material.

<!-- COURSE_TABLE:START -->
| ID | Paper | Date | Status | Notebook | Colab | Runnable tier | What you will do |
|---|---|---|---|---|---|---|---|
| `M00` | Zoom In: An Introduction to Circuits | `2020-03-10` | `method-lab` | [Open](notebooks/en/m00_zoom_in_circuits.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/en/m00_zoom_in_circuits.ipynb) | `warmup` | Build first-pass intuition for features, circuits, and interventions in a visual model. |
| `M01` | Toy Models of Superposition | `2022-09-14` | `paper-faithful` | [Open](notebooks/en/m01_toy_models_superposition.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/en/m01_toy_models_superposition.ipynb) | `cpu-colab` | Use a minimal toy model to see why neurons can mix multiple semantics. |
| `M02` | Towards Monosemanticity | `2023-10-05` | `method-lab` | [Open](notebooks/en/m02_towards_monosemanticity.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/en/m02_towards_monosemanticity.ipynb) | `cpu-colab` | Use a teaching-scale sparse autoencoder to see why a feature view can be cleaner than a neuron view. |
| `M03` | Mapping the Mind of a Large Language Model | `2024-05-21` | `reading-only` | Reading | - | `reading-only` | Browse a teaching-scale feature catalog to understand what it means to discover many reusable features. |
| `M04` | Using Dictionary Learning Features as Classifiers | `2024-10-16` | `method-lab` | [Open](notebooks/en/m04_features_as_classifiers.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/en/m04_features_as_classifiers.ipynb) | `cpu-colab` | Treat features as classifier inputs and study where readout ability comes from. |
| `M05` | Evaluating Feature Steering | `2024-10-25` | `method-lab` | [Open](notebooks/en/m05_evaluating_feature_steering.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/en/m05_evaluating_feature_steering.ipynb) | `cpu-colab` | Sweep steering strength to inspect target gain, sweet spots, and off-target costs. |
| `M06` | Tracing the Thoughts of a Large Language Model | `2025-03-27` | `reading-only` | Reading | - | `reading-only` | Run a toy tracing reproduction locally, then use a shared attribution graph to read a local computation path. |
| `M07` | Open-sourcing Circuit Tracing Tools | `2025-05-29` | `reading-only` | Reading | - | `reading-only` | Inspect tracing artifacts and workflow stages to understand the tooling layer behind the analysis. |
| `M08` | Persona Vectors | `2025-08-01` | `reading-only` | Reading | - | `reading-only` | Construct a teaching-scale persona direction locally, then use a shared artifact to compare before/after trait shifts. |
| `M09` | Signs of Introspection in Large Language Models | `2025-10-29` | `reading-only` | Reading | - | `reading-only` | Compare self-report and behavior signals in teaching data to discuss what 'signs of introspection' actually mean. |
| `M10` | The Assistant Axis | `2026-01-19` | `reading-only` | Reading | - | `reading-only` | Project multiple assistant styles onto one axis and inspect the problem of stabilizing character. |
<!-- COURSE_TABLE:END -->

## Suggested Paths

- `Pre-P4 foundation pack`: `F00 → F01 → F02 → F03`
- `Live core path`: `M00 → M01 → M02 → M04 → M05`
- `Reading-only papers for now`: `M03`, `M06`, `M07`, `M08`, `M09`, `M10`
- `Extension method labs`: `X01 → X02 → X03 → X04 → X05 → X06 → X07`

If you want the shortest strict live-code path, start with `F00`, then `M00`, `M01`, `M02`, `M05`, and `X01`.

## Research-Ready Path

If your goal is not just understanding but becoming effective as a student researcher or independent researcher, use these files alongside the article notebooks:

- [Research-ready overview](docs/en/program/research-ready.md)
- [Colab-first path](docs/en/program/colab-first-path.md)
- [P8 roadmap](docs/en/program/p8-roadmap.md)
- [12-week bootcamp](docs/en/program/week-by-week.md)
- [Research playbook](docs/en/program/research-playbook.md)
- [Evaluation rubric](docs/en/program/evaluation-rubric.md)
- [Independent research sprints](docs/en/program/independent-sprints.md)
- [Reference-output layer](docs/en/program/reference-outputs.md)
- [Advanced extension track](docs/en/program/advanced-extensions.md)

Templates:

- [Paper reading note](templates/paper_reading_note_en.md)
- [Experiment log](templates/experiment_log_en.md)
- [Research memo](templates/research_memo_en.md)

Internal training stages now use `S0-S4` so they stay clearly separate from the Alibaba-style `P4-P12` capability mapping above. The `S0-S4` bootcamp is the core floor-building segment, not the whole `P8` journey.

Use the research-ready track as an operating system, not as extra reading:

- Every article should leave behind a reading note, an experiment log, a short memo, and a next-question list.
- The weekly path assumes `8-12` focused hours per week.
- You should finish with a real portfolio: notes, logs, memos, an artifact critique, and a two-week capstone proposal.
- The bar is not "I followed the notebooks." The bar is "I can read, reproduce, critique, and propose the next experiment."

## Reference-Output Layer

This layer is not for copying. It is for calibrating what a deliverable looks like when it is ready for a mentor, advisor, collaborator, or peer reviewer, which matters even more once you start the extension reproductions.

<!-- REFERENCE_TABLE:START -->
| ID | Reference Output | File | When to use it |
|---|---|---|---|
| `R01` | Reference Paper Brief | [examples/en/reference_paper_brief.md](examples/en/reference_paper_brief.md) | Use it after independent sprint T1 or any paper reading note that needs to be compressed for a mentor or peer. |
| `R02` | Reference Experiment Log | [examples/en/reference_experiment_log.md](examples/en/reference_experiment_log.md) | Use it after any sweep, ablation, or feature-steering notebook. |
| `R03` | Reference Artifact Critique | [examples/en/reference_artifact_critique.md](examples/en/reference_artifact_critique.md) | Use it for M03, M07, M09, M10, or independent sprint T3. |
| `R04` | Reference Two-Week Proposal | [examples/en/reference_two_week_proposal.md](examples/en/reference_two_week_proposal.md) | Use it before a capstone or independent sprint T4 to calibrate the density of your proposal. |
<!-- REFERENCE_TABLE:END -->

## Extension-Paper Track

The core course is intentionally organized around the Anthropic interpretability arc, but that is still not broad enough for a `P8`-oriented research path. After the core, widen out into transformer circuits, behavior circuits, memory/editing, and auditing-facing work through more Colab reproductions.

Under the strict realtime policy, the status column matters:

- `paper-faithful`: runnable and honest as a paper-shaped reproduction
- `method-lab`: runnable, but explicitly a live method drill rather than a full paper reproduction
- `reading-only`: kept for reading and critique only because this repository would otherwise rely on precomputed artifacts or unavailable stacks

<!-- EXTENSION_TABLE:START -->
| ID | Extension Paper | Link | Status | Notebook | Colab | Runnable tier | Why now | What to ship |
|---|---|---|---|---|---|---|---|---|
| `X01` | A Mathematical Framework for Transformer Circuits | [Source](https://transformer-circuits.pub/2021/framework/index.html) | `method-lab` | [Open](notebooks/extensions/en/x01_transformer_circuits_framework.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/extensions/en/x01_transformer_circuits_framework.ipynb) | `cpu-colab` | After M06, this moves you from 'I can read one graph' to 'I can speak the general framework.' | Reproduce one minimal residual-composition toy in Colab, then write a one-page framework brief that restates one M06 toy trace using residual-stream and composition language. |
| `X02` | In-context Learning and Induction Heads | [Source](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html) | `method-lab` | [Open](notebooks/extensions/en/x02_induction_heads.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/extensions/en/x02_induction_heads.ipynb) | `cpu-colab` | It connects attention reading, circuit language, and a concrete behavioral phenomenon, making it a first stop for classic transformer-circuits work. | Reproduce one minimal copying task in Colab and explain why an induction head is more like a mechanism than a single attention hotspot. |
| `X03` | Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 Small | [Source](https://arxiv.org/abs/2211.00593) | `method-lab` | [Open](notebooks/extensions/en/x03_ioi_circuit.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/extensions/en/x03_ioi_circuit.ipynb) | `cpu-colab` | After the Anthropic core path, this forces you to handle messier behavior definitions, more heads, and a longer evidence chain. | Reproduce a teaching-scale IOI evidence chain in Colab, then write one brief stating which uncertainties appear here that were absent in the M06 toy trace. |
| `X04` | Transformer Feed-Forward Layers Are Key-Value Memories | [Source](https://arxiv.org/abs/2012.14913) | `method-lab` | [Open](notebooks/extensions/en/x04_ffn_key_value_memories.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/extensions/en/x04_ffn_key_value_memories.ipynb) | `cpu-colab` | If you can only read attention circuits but cannot explain what an MLP stores, it is hard to move into factual recall and model editing. | Reproduce a teaching-scale key-value memory toy in Colab, then write one note explaining why some facts look more like MLP retrieval than on-the-fly attention computation. |
| `X05` | Knowledge Neurons in Pretrained Transformers | [Source](https://arxiv.org/abs/2104.08696) | `method-lab` | [Open](notebooks/extensions/en/x05_knowledge_neurons.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/extensions/en/x05_knowledge_neurons.ipynb) | `cpu-colab` | This paper forces you to separate 'some units predict the phenomenon' from 'those units truly carry the phenomenon.' | Reproduce a teaching-scale knowledge-neuron scoring and ablation experiment in Colab, then write one note explaining why a high-scoring neuron still does not automatically yield a causal explanation. |
| `X06` | Locating and Editing Factual Associations in GPT | [Source](https://arxiv.org/abs/2202.05262) | `method-lab` | [Open](notebooks/extensions/en/x06_rome_factual_editing.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/extensions/en/x06_rome_factual_editing.ipynb) | `cpu-colab` | If you want to move from graph reading to intervention judgment, reading graphs is not enough; you also need to discuss whether an edit is stable, local, and worth pursuing. | Reproduce a teaching-scale rank-one factual edit in Colab, then write one edit memo describing how to evaluate edit success, locality, and collateral damage together. |
| `X07` | Auditing Language Models for Hidden Objectives | [Source](https://www.anthropic.com/research/auditing-hidden-objectives) | `method-lab` | [Open](notebooks/extensions/en/x07_auditing_hidden_objectives.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/extensions/en/x07_auditing_hidden_objectives.ipynb) | `cpu-colab` | If you want one coherent frame that connects features, tracing, editing, and auditing, this paper puts them into one view. | Reproduce a teaching-scale auditing toy in Colab, then write one memo describing which behavioral signals, internal evidence, and stop conditions you would inspect first if you suspected a hidden objective. |
<!-- EXTENSION_TABLE:END -->

## Quick Start

```bash
pip install -r requirements.txt

# Refresh derived assets after editing course metadata
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py

# Validate metadata, docs, notebook parity, and links
python3 scripts/validate_course.py
python3 scripts/check_links.py

# Enforce the no-precomputed-artifact rule for live notebooks
python3 scripts/audit_realtime_policy.py

# Execute all generated notebooks as a smoke test
python3 scripts/smoke_notebooks.py
```

If you prefer the lightest workflow, open the Colab links in the tables above directly and skip local setup until you need it.

## Repo Structure

```text
.
├── content/               # Course metadata and glossary
├── docs/                  # Mirrored zh/en article notes + foundations + extension notes + bootcamp docs
├── notebooks/             # Legacy notebook + article notebooks + foundation labs + extension reproductions
├── examples/              # Reference briefs, logs, critiques, and proposals
├── artifacts/             # Reading-only reference data; not allowed in strict live notebooks
├── scripts/               # Notebook generation and validation
├── figures/               # Legacy visual circuit figures reused by M00
└── utils/                 # Shared plotting helpers from the original tutorial
```

## What Stays From the Original Project

The original notebooks remain in place:

- `notebooks/circuits_zoom_in_en.ipynb`
- `notebooks/circuits_zoom_in_zh.ipynb`

They now act as the long-form background material behind `M00`.

## References

The core reading path is anchored in official Anthropic research pages as of `2026-03-25`, with the interpretability team page as the index:

- [Anthropic Interpretability team page](https://www.anthropic.com/research/team/interpretability)
- [Toy Models of Superposition](https://www.anthropic.com/research/toy-models-of-superposition)
- [Towards Monosemanticity](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning)
- [Mapping the Mind of a Large Language Model](https://www.anthropic.com/research/mapping-mind-language-model)
- [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)

## License

[MIT](LICENSE)
