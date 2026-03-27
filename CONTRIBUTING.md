# Contributing

This repository serves one scope only: the Distill 2020 Circuits thread.

The synced layers are:

1. `content/course.json`
2. mirrored `docs/en` and `docs/zh`
3. mirrored `notebooks/en` and `notebooks/zh`
4. `utils/distill_circuits.py` plus the scripts that generate and validate the public surface

If you change one layer, make sure the others still line up.

## High-value contributions

**Strengthen live notebooks.** The highest-value work is improving the `D01-D09` live notebooks without breaking the live-only contract.

**Improve bilingual parity.** English and Chinese should stay structurally aligned even when the wording changes.

**Tighten runtime honesty.** If a notebook looks like a static walkthrough, downgrade it or replace it with real runtime analysis.

**Improve public reproducibility.** Better Colab behavior, faster CPU execution, clearer plots, and better smoke-test coverage are all useful.

## Structural rules

**Treat `content/course.json` as authoritative.** IDs, order, titles, prerequisites, paper links, and notebook availability should be edited there first.

**Keep docs mirrored.** `docs/en` and `docs/zh` must expose the same article set and structure.

**Keep notebooks mirrored.** `notebooks/en` and `notebooks/zh` must keep the same `D01-D09` execution shape.

**Do not add precomputed artifacts back into the required path.** Live notebooks must not read bundled `figures/`, `artifacts/`, or other repository-side result files.

## Development workflow

1. Create a branch from `main`.
2. Make your changes.
3. Regenerate derived content:
   `python3 scripts/render_readmes.py`
   `python3 scripts/generate_course_notebooks.py`
4. Run validation:
   `python3 scripts/validate_course.py`
   `python3 scripts/audit_realtime_policy.py`
   `python3 scripts/check_links.py`
   `python3 scripts/smoke_notebooks.py`
