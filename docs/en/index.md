# Learn Interpretability

This course is now Colab-first under a strict honesty rule: only notebooks that generate outputs live at runtime count as runnable work. Anything that still depends on precomputed artifacts is treated as reading-only.

## Pre-P4 foundation pack

- [Foundation pack overview](foundations/index.md)
- If notebook execution, attention reading, or experiment logging still feel unstable, do `F00-F03` before the article core.

## Reading order

1. [M00 Zoom In: An Introduction to Circuits](modules/m00-zoom-in-circuits.md)
2. [M01 Toy Models of Superposition](modules/m01-toy-models-superposition.md)
3. [M02 Towards Monosemanticity](modules/m02-towards-monosemanticity.md)
4. [M03 Mapping the Mind of a Large Language Model](modules/m03-mapping-the-mind.md)
5. [M04 Using Dictionary Learning Features as Classifiers](modules/m04-features-as-classifiers.md)
6. [M05 Evaluating Feature Steering](modules/m05-evaluating-feature-steering.md)
7. [M06 Tracing the Thoughts of a Large Language Model](modules/m06-tracing-thoughts.md)
8. [M07 Open-sourcing Circuit Tracing Tools](modules/m07-circuit-tracing-tools.md)
9. [M08 Persona Vectors](modules/m08-persona-vectors.md)
10. [M09 Signs of Introspection in Large Language Models](modules/m09-signs-of-introspection.md)
11. [M10 The Assistant Axis](modules/m10-assistant-axis.md)

## Extension reproduction track

- [Extension-paper overview](extensions/index.md)
- After the core, do not stop at "I finished the Anthropic arc." Continue with classic transformer-circuits, memory/editing, and auditing papers as Colab reproductions.

## How to use the repo

- Read the note first.
- If the item is marked `paper-faithful` or `method-lab`, open the paired notebook locally or in Colab.
- If the item is marked `reading-only`, treat it as a paper note rather than a runnable reproduction.
- Answer the self-check questions at the end of the note and notebook rather than stopping at the plots.
- Turn each reproduction into a reading note, an experiment log, and a short memo rather than keeping it only in your head.

## Research-ready track

- [Research-ready overview](program/research-ready.md)
- [Colab-first path](program/colab-first-path.md)
- [Capability arc and P6 evidence gates](program/capability-arc.md)
- [P6 graduation checklist](program/p6-graduation-checklist.md)
- [12-week bootcamp](program/week-by-week.md)
- [Research playbook](program/research-playbook.md)
- [Evaluation rubric](program/evaluation-rubric.md)
- [Independent research sprints](program/independent-sprints.md)
- [Reference-output layer](program/reference-outputs.md)
- [Advanced extension track](program/advanced-extensions.md)

Use the track in this order:

1. Read the overview.
2. Commit to the 12-week schedule as the core apprenticeship stage, not the whole finish line.
3. Use the playbook and templates while you work through the articles.
4. Score yourself with the rubric at Week 7 and Week 12.
5. Clear the P6 graduation checklist after the bootcamp.
6. Finish one independent research sprint and one capstone proposal.

## Ground rules

- Under the strict realtime policy, the live core path is `M00`, `M01`, `M02`, `M04`, and `M05`; `M03` and `M06-M10` are currently reading-only because this repo would otherwise rely on precomputed artifacts.
- `X01-X07` stay runnable, but they are method labs rather than claims of full paper-faithful reproduction.
- Use `python3 scripts/audit_realtime_policy.py` after notebook generation if you want the repo to enforce the no-precomputed-artifact rule.
- Chinese and English stay structurally mirrored. If you add an article note in one language, add it in the other.
- If your goal is serious research growth, output quality matters more than completion counts.
