# X04 Key-Value Memories

## Goal

Treat the MLP layer as a key-value memory and understand why factual recall is not only an attention-routing problem.

## Core reference

- [Transformer Feed-Forward Layers Are Key-Value Memories](https://arxiv.org/abs/2012.14913)

## Why it matters for the P8 path

- If you cannot explain what an MLP stores, it is hard to move into factual recall, editing, and memory localization.
- This expands your research language from "attention circuits" into "internal storage."

## Notebook and deliverable

- Notebook: `notebooks/extensions/en/x04_ffn_key_value_memories.ipynb`
- Deliverable: one key-value memory toy reproduction plus one paragraph explaining why some facts look more like MLP retrieval.

## Self-check

- In your toy, what plays the key and what plays the value?
- Why does explaining a recall behavior as MLP retrieval change the next experiment you would design?
- When explaining factual recall, what is MLP memory better at and what is attention routing better at?

## Extension conclusion

Once the MLP becomes legible as a memory layer, questions about knowledge, editing, and localization become much easier to discuss clearly.
