# Colab-First Path

## Why the project is organized around Colab first

- The most common beginner failure is not total conceptual ignorance. It is unstable environments, broken reproductions, and unwritten conclusions.
- Colab lets readers focus first on paper reproduction, plot reading, and experimental judgment instead of getting stuck on local engineering details.
- In interpretability, the real skill is being able to turn a paper into a smallest runnable, critiqueable, reviewable experiment.

## Core operating principles

- One paper maps to one note, and every honest live item gets its own Colab notebook.
- Every live run or reproduction leaves behind at least a reading note, an experiment log, and a short memo.
- Start with a smallest teaching-scale reproduction before discussing scale gaps and external validity.
- Only introduce heavier local stacks when they are truly needed; by default, build research feel on CPU or free Colab first.

## Three-step usage pattern

1. Use `F00-F03` to stabilize environment setup, plot reading, geometry, and experiment discipline.
2. Use the runnable `M00-M05` modules to build the live core, and use `M03` plus `M06-M10` as reading-and-critique modules.
3. Use `X01-X07` to run method labs around transformer circuits, memory/editing, and auditing in Colab too.

## What shows you are actually using the path correctly

- You do not only open notebooks; you write a prediction before running and label observation, inference, and speculation afterward.
- You record baselines, variants, failure points, and stop conditions.
- You explicitly write what the reproduction still does not prove.
- You can restate a core paper through an extension paper and vice versa, rather than treating them as isolated reads.

## What not to misunderstand

- Colab-first does not mean static figures or precomputed screenshots.
- Teaching-scale reproduction does not mean giving up rigor.
- The purpose of a lightweight notebook is to teach you to ask better questions and build a smallest evidence chain before you move into a heavier research stack.
