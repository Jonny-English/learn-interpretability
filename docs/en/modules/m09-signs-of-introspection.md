# M09 Signs of Introspection in Large Language Models

## Goal

Inspect the gap between what a model says about itself and what its behavior reveals, without pretending that this repository has the full live experiment stack behind the paper.

## Core reference

- [Signs of introspection in large language models](https://www.anthropic.com/research/introspection)

## What to look for

- Self-report and observable behavior can align, but not perfectly.
- The interesting cases are the mismatches, not only the agreements.
- “Signs of introspection” should raise questions, not settle them.

## Status

- `reading-only` under the strict realtime policy
- This repository does not currently present a live notebook here because it would depend on precomputed introspection-signal artifacts.
- Shared reference artifact: `artifacts/m09_introspection_signals.json`

## Self-check questions

- Why can self-report not be treated as direct evidence of internal state?
- Among the mismatch cases, which one is most worth following up, and what alternative explanations should you worry about?
- If you wanted to make the introspection claim stronger, which key class of evidence is still missing?

## Takeaway

This paper is best read as a frontier probe into self-modeling, not as proof of robust introspection.
