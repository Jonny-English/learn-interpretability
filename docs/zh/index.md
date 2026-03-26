# Learn Interpretability

这门课现在是带严格诚实规则的 Colab 优先结构：只有在运行时实时产生输出的 notebook，才算可运行内容；凡是仍然依赖预计算 artifact 的部分，一律按阅读材料处理。

如果你是第一次打开这个仓库，不要一上来把所有文档都读完；先证明给自己看，至少有 1 个 Colab 能跑通。

## 第一轮先做什么

- [F00 Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/foundations/zh/f00_environment_plots_baselines.ipynb)：修好环境和 baseline 纪律
- [M00 Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/m00_zoom_in_circuits.ipynb)：建立 feature 和 circuit 的第一层直觉
- [M01 Colab](https://colab.research.google.com/github/Jonny-English/learn-interpretability/blob/main/notebooks/zh/m01_toy_models_superposition.ipynb)：跑第一篇带论文形状的复现

当前仓库快照：

- `4` 个基础 lab
- `5` 个 live 主线 notebook
- `7` 个可运行扩展方法练习
- `32` 本 notebook 通过 smoke test
- 完整 `P6-ready` 路径建议投入 `180-250` 小时

## Pre-P4 基础包

- [基础包总览](foundations/index.md)
- 建议在文章主线之前先做 `F00-F03`，尤其当你还不稳定地运行 notebook、读 attention 图或写实验日志时。

## 阅读顺序

1. [M00 Zoom In：电路入门](modules/m00-zoom-in-circuits.md)
2. [M01 Toy Models of Superposition](modules/m01-toy-models-superposition.md)
3. [M02 Towards Monosemanticity](modules/m02-towards-monosemanticity.md)
4. [M03 Mapping the Mind](modules/m03-mapping-the-mind.md)
5. [M04 Features as Classifiers](modules/m04-features-as-classifiers.md)
6. [M05 Evaluating Feature Steering](modules/m05-evaluating-feature-steering.md)
7. [M06 Tracing the Thoughts](modules/m06-tracing-thoughts.md)
8. [M07 Circuit Tracing Tools](modules/m07-circuit-tracing-tools.md)
9. [M08 Persona Vectors](modules/m08-persona-vectors.md)
10. [M09 Signs of Introspection](modules/m09-signs-of-introspection.md)
11. [M10 The Assistant Axis](modules/m10-assistant-axis.md)

## 扩展复现轨道

- [扩展论文总览](extensions/index.md)
- 当你做完主线后，不要停在“看过 Anthropic 主线”，继续把经典 transformer circuits、memory/editing 和 auditing 论文也做成 Colab 复现。

## 推荐使用方式

- 先读对应文章讲义。
- 如果状态是 `paper-faithful` 或 `method-lab`，再运行匹配 notebook，或者直接用 Colab。
- 如果状态是 `reading-only`，就把它当阅读与批判入口，不再把它算成复现。
- 做完后回答讲义和 notebook 末尾的验收题，而不是只看完图就结束。
- 把每一次复现都写成 reading note、experiment log 和短 memo，而不是只保留在脑子里。

## 研究就绪路径

- [研究就绪总览](program/research-ready.md)
- [Colab 优先路径](program/colab-first-path.md)
- [能力成长弧线与 P6 证据门槛](program/capability-arc.md)
- [P6 毕业清单](program/p6-graduation-checklist.md)
- [12 周训练营](program/week-by-week.md)
- [研究工作流](program/research-playbook.md)
- [评估 rubric](program/evaluation-rubric.md)
- [独立研究冲刺](program/independent-sprints.md)
- [参考答案层](program/reference-outputs.md)
- [扩展论文轨道](program/advanced-extensions.md)

建议按这个顺序使用：

1. 先看总览，确认目标和门槛。
2. 再把 12 周训练营当成核心学徒阶段推进，而不是全部终点。
3. 一边做文章，一边使用 playbook 和模板。
4. 在第 7 周和第 12 周用 rubric 自评。
5. 训练营结束后，再通过 P6 毕业清单。
6. 最后完成一个独立研究冲刺任务和一个 capstone proposal。

## 使用约束

- 在严格实时规则下，当前可跑主线是 `M00`、`M01`、`M02`、`M04`、`M05`；`M03` 和 `M06-M10` 因为会依赖预计算 artifact，所以目前降级为阅读材料。
- `X01-X07` 仍然可跑，但它们属于方法练习，不再宣称是原论文级全文复现。
- 生成 notebook 后可运行 `python3 scripts/audit_realtime_policy.py`，用脚本强制检查“不得依赖预计算 artifact”。
- 中英内容必须结构镜像。如果一边新增文章讲义，另一边也要新增。
- 如果目标是严肃地进入研究状态，最重要的是输出质量，而不是完成数量。
- 如果这个仓库确实帮你省了时间、给了清晰路径，请给它一个 star，让更多小白能找到它。
