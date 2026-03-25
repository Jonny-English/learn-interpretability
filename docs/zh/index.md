# From Circuits to Claude

这门课把 `Zoom In` 的视觉电路直觉，接到 Anthropic 的 interpretability 主线：superposition、字典学习、feature intervention、circuit tracing，以及 character control。

## 阅读顺序

1. [M00 视觉电路热身](modules/m00-vision-circuits.md)
2. [M01 Superposition](modules/m01-superposition.md)
3. [M02 单语义特征与字典学习](modules/m02-monosemantic-features.md)
4. [M03 特征探针与 Steering](modules/m03-feature-probes-steering.md)
5. [M04 Circuit Tracing](modules/m04-circuit-tracing.md)
6. [M05 Character and Control](modules/m05-character-control.md)

## 推荐使用方式

- 先读对应模块讲义。
- 再运行 `notebooks/zh` 中对应的 notebook。
- 然后查看 `artifacts/` 里的共享 JSON artifact。
- 想看时间线、概念图、术语卡片和进度时，再打开 `web/`。

## 使用约束

- `M00-M03` 设计目标是 CPU 或免费 Colab 可跑。
- `M04-M05` 是围绕预计算 artifact 的教学复现，不是完整论文级实验。
- 中英内容必须结构镜像。如果一边新增小节，另一边也要新增。
