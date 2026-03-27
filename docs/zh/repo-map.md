# 仓库地图

## 顶层结构

- [`content/`](../../content)：课程元数据和 Distill 文章清单
- [`docs/`](../../docs)：中英镜像讲义
- [`notebooks/`](../../notebooks)：生成出来的 live notebooks
- [`utils/`](../../utils)：共享 Distill runtime 工具
- [`scripts/`](../../scripts)：README/docs 渲染、生成、校验、审计、smoke 和链接检查

## 维护命令

```bash
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py
python3 scripts/validate_course.py
python3 scripts/audit_realtime_policy.py
python3 scripts/check_links.py
python3 scripts/smoke_notebooks.py
```
