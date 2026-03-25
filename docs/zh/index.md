# From Circuits to Claude

这门课现在是 Colab 优先的论文复现结构：核心路径里的每一篇论文，都有自己独立的讲义、notebook 和验收题。

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
- 再运行匹配 notebook，或者直接用 Colab。
- 如果这一篇是 artifact-guided，就顺手看 `artifacts/` 中对应的 JSON。
- 做完后回答讲义和 notebook 末尾的验收题，而不是只看完图就结束。
- 把每一次复现都写成 reading note、experiment log 和短 memo，而不是只保留在脑子里。

## 研究就绪路径

- [研究就绪总览](program/research-ready.md)
- [Colab 优先路径](program/colab-first-path.md)
- [P8 路线图](program/p8-roadmap.md)
- [12 周训练营](program/week-by-week.md)
- [研究工作流](program/research-playbook.md)
- [评估 rubric](program/evaluation-rubric.md)
- [公司入职模拟](program/company-onramp.md)
- [参考答案层](program/reference-outputs.md)
- [扩展论文轨道](program/advanced-extensions.md)

建议按这个顺序使用：

1. 先看总览，确认目标和门槛。
2. 再按 12 周计划推进。
3. 一边做文章，一边使用 playbook 和模板。
4. 在第 7 周和第 12 周用 rubric 自评。
5. 最后完成一个公司模拟任务和一个 capstone proposal。

## 使用约束

- `M00-M05` 设计目标是 CPU 或免费 Colab 可跑。
- `M06` 和 `M08` 现在包含轻量本地复现；`M03`、`M07`、`M09`、`M10` 仍然主要是 artifact-guided 教学复现。
- `X01-X07` 是更长的 Colab 复现轨道，用来把主线能力继续往 P7/P8 所需的广度和 rigor 上推进。
- 中英内容必须结构镜像。如果一边新增文章讲义，另一边也要新增。
- 如果目标是进入公司研究环境，最重要的是输出质量，而不是完成数量。
