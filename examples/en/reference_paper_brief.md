# Reference Paper Brief

## Task context

Write a one-page brief for a mentor, advisor, or peer who has not read the paper, explaining the question, strongest evidence, biggest weakness, and next experiment for `M05 Evaluating Feature Steering`.

## Summary

The core value of this work is not proving that steering always works. It is reframing the question as: at what intervention range do benefit and collateral cost stay best balanced? The strongest evidence comes from the sweep rather than from one attractive demo.

## Strongest evidence

- The target metric rises and then plateaus as steering strength increases, which implies an operable range.
- The off-target metric degrades more sharply at higher strengths, showing that "stronger" is not the same as "better."
- The most valuable result is not the peak itself but the existence of a sweet spot.

## Biggest weakness

- The evaluation still depends on the current task setup and may not transfer to other prompt distributions.
- If the feature itself is entangled, the sweet spot may only be a local optimum under the current measurement frame.
- One sweep is still insufficient to say much about longer or multi-turn side effects.

## Next experiment

Hold the feature fixed and expand the evaluation from one prompt distribution to three: the original distribution, an adversarial distribution, and a long-context distribution. The goal is to see whether the sweet spot shifts and whether off-target cost amplifies on the new distributions.

## Why this is a strong example

This brief does not restate the whole paper. It compresses the research judgment into the strongest evidence, the biggest weakness, and the smallest useful next experiment.
