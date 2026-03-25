# Contributing

This project is now a bilingual interpretability course with three synced layers:

1. `content/course.json` as the source of truth
2. mirrored `docs/zh` and `docs/en`
3. mirrored `notebooks/zh` and `notebooks/en`, plus a static `web/` explorer

If you touch one layer, make sure the others still line up.

## High-value contributions

**Fix conceptual mistakes.** If a claim about superposition, dictionary learning, circuit tracing, or persona control is wrong or too hand-wavy, open an issue or patch it directly.

**Improve bilingual parity.** Chinese and English should stay structurally identical. Better wording is welcome; mismatched structure is not.

**Strengthen runnable labs.** `M00-M03` should stay CPU-friendly and Colab-friendly. Better toy datasets, clearer plots, and faster smoke execution are especially useful.

**Improve artifacts and visualizations.** `M04-M05` rely on precomputed artifacts. Clearer attribution-graph views, better glossary cards, and more readable persona plots are good contributions.

## Development workflow

1. Create a branch from `main`.
2. Make your changes.
3. Regenerate derived content if you changed metadata:
   `python3 scripts/render_readmes.py`
   `python3 scripts/generate_course_notebooks.py`
4. Run validation:
   `python3 scripts/validate_course.py`
   `python3 scripts/smoke_notebooks.py`
   `python3 scripts/check_links.py`
5. If you changed the web app, also run:
   `cd web && npm install && npm run build`

## Structural rules

**Treat `content/course.json` as authoritative.** Module IDs, order, titles, prerequisites, paper links, and artifact references should be edited there first.

**Keep docs mirrored.** `docs/zh` and `docs/en` must expose the same modules and the same section structure.

**Keep notebooks mirrored.** `notebooks/zh` and `notebooks/en` must keep the same module IDs and execution shape. Language can differ; structure should not.

**Do not turn the course into a heavy compute project.** Core labs should remain runnable on CPU or free Colab. Heavy model tracing belongs in optional extensions, not in the required path.

## Questions

Open an issue or PR with the specific module ID you are changing. That makes review much faster.
