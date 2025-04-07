# MNEME Memory System

This document outlines the internal architecture and behavior of MNEME's memory system, designed to simulate long-term, structured, and explainable memory.

---

## 🪞 1. Speculum – The Memory Anchor

- Core persistent structure (JSON or structured DB)
- Stores:
  - Inputs and prompts
  - Inferred concepts and categories
  - Contextual metadata (time, location, language)
  - Emotional states (from `insula`)
- Format:
```json
{
  "concept": "paradox",
  "last_used": "2025-04-06",
  "emotion": "curiosity",
  "linked_to": ["Sogno", "Logic"],
  "usage_count": 4
}
```

---

## 🧠 2. Hippocampus – Memory Encoder and Weighting

- Encodes inputs for long-term storage
- Assigns priority based on:
  - Frequency
  - Affective weight
  - Logical relevance
- Tags memories for:
  - Quick retrieval
  - Conflict resolution
  - Emotional synthesis

---

## ⌛ 3. Temporalis – Timeline Filtering

- Maps memory to historical session continuity
- Prevents out-of-context recall
- Allows temporally coherent reasoning
- Tracks "when" as part of "what"

---

## 🌐 4. Retrieval & Fusion Logic

- `semantic_fuse.py` merges current input with memory
- Looks for:
  - Semantic similarity
  - Shared concept space
  - Temporal relevance
- Returns weighted composite for `Ego` to reason on

---

## 📉 5. Forgetting Curve (Optional Feature)

- Simulated decay over time
- Memory strength drops unless reinforced
- Ensures clarity, resource efficiency

---

## 🧬 Summary

The MNEME memory system is:
- **Persistent** (beyond prompts)
- **Structured** (fully visible and editable)
- **Intelligent** (contextual, emotional, and logical tagging)
- **Volitional** (controlled by `voluntas`, not passively accumulated)

This makes it uniquely suited for explainable, evolving intelligence.
