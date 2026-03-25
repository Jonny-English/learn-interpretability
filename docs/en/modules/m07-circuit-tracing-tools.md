# M07 Open-sourcing Circuit Tracing Tools

## Goal

Expose the workflow and artifact structure behind circuit tracing without pretending to reproduce a production stack.

## Core reference

- [Open-sourcing circuit tracing tools](https://www.anthropic.com/research/open-source-circuit-tracing)

## What to look for

- Tracing requires a pipeline, not just a visualization.
- Intermediate files and scoring stages shape what you can eventually inspect.
- Tooling decisions affect the fidelity and usability of every downstream graph.

## Status

- `reading-only` under the strict realtime policy
- This repository does not currently present a live notebook here because the workflow explanation depends on precomputed tool artifacts.
- Shared reference artifacts: `artifacts/m06_attribution_graph.json` and `artifacts/m07_tracing_tool_workflow.json`

## Self-check questions

- Which stage in the tracing workflow looks most like the bottleneck, and why?
- If you could request one tooling improvement from a research engineer, what would it be and how would you justify it?
- Why does the tooling layer shape not only efficiency, but also the research questions a team can realistically ask?

## Takeaway

Good interpretability results depend on good tooling, not only good ideas.
