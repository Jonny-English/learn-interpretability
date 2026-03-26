# X05 Knowledge Neurons

## Goal

Practice localizing "knowledge" into a more intervention-friendly set of units and separate correlation clues from causal storage sites.

## Core reference

- [Knowledge Neurons in Pretrained Transformers](https://arxiv.org/abs/2104.08696)

## Why it matters for robust P6 growth

- This paper forces a sharper distinction between readout, localization, and causality.
- If you later want to do stronger editing or auditing work, you cannot treat high-scoring units as causal conclusions by default.

## Notebook and deliverable

- Notebook: `notebooks/extensions/en/x05_knowledge_neurons.ipynb`
- Deliverable: one neuron-scoring and ablation log plus one paragraph on why a high-scoring neuron still does not automatically imply causality.

## Self-check

- Why can a neuron score highly and still be only a correlation clue?
- In your toy ablation, what result most supports a local-carrier interpretation?
- What is the biggest difference in explanatory strength between knowledge neurons and feature probes?

## Extension conclusion

The value of this paper is not "now we found where knowledge is." The value is training a stricter standard for localization claims.
