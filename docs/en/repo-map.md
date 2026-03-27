# Repo Map

## Top Level

- [`content/`](../../content): course metadata and only the Distill article manifest
- [`docs/`](../../docs): mirrored English and Chinese notes
- [`notebooks/`](../../notebooks): generated live notebooks
- [`utils/`](../../utils): shared Distill runtime helpers
- [`scripts/`](../../scripts): generators, validation, audit, smoke tests, and link checks

## Maintenance Commands

```bash
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py
python3 scripts/validate_course.py
python3 scripts/audit_realtime_policy.py
python3 scripts/check_links.py
python3 scripts/smoke_notebooks.py
```
