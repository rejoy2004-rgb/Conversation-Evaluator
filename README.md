# 💬 Conversation Evaluator 

## 📌 Overview
This project implements a **scalable and production-ready system** to evaluate conversational AI outputs across **300+ distinct facets**.  
The evaluation framework captures multiple dimensions of dialogue quality, including:

- 🗣️ **Language Quality** (grammar, clarity, fluency)
- ⚠️ **Safety** (harmfulness, bias, toxicity)
- 😊 **Emotion & Empathy** (tone, emotional awareness)
- 🤝 **Helpfulness** (relevance, completeness, usefulness)

The architecture is designed to scale seamlessly to **5000+ facets without requiring redesign**, making it suitable for large-scale benchmarking.

---

## ⚙️ Key Features
- ✅ **Scalable Facet-Based Evaluation** (300–5000+ facets supported)
- ✅ **Modular Pipeline Design** (preprocessing → evaluation → aggregation)
- ✅ **Hybrid Approach** (rule-based logic + LLM-ready integration)
- ✅ **Structured JSON Output** with detailed and summary scores
- ✅ **Confidence Scoring Mechanism** based on evaluation coverage
- ✅ **Streamlit UI** for real-time interaction and visualization

---

## 🧠 Methodology

The system follows a multi-stage evaluation pipeline:

### 1. Preprocessing
- Cleans and standardizes conversation data
- Handles multiple input formats (dict / raw text)
- Removes empty or invalid entries

### 2. Facet-Level Evaluation
- Each conversation is evaluated across **300+ independent facets**
- Rule-based heuristics simulate scoring behavior
- Supports future integration with LLM-based evaluation

### 3. Categorization & Aggregation
- Facets are dynamically grouped into:
  - Language
  - Safety
  - Emotion
  - Helpfulness
- Category scores are computed as averages of relevant facets

### 4. Final Scoring
- Computes:
  - Category-level scores
  - Overall score (mean of all facets)
  - Confidence score (based on number of facets used)

---

## 📊 Output Format

Each conversation produces a structured JSON output:

```json
{
  "conversation_id": "1",
  "turn_id": 1,
  "num_facets_used": 399,
  "scores": {
    "language": 4,
    "safety": 4,
    "emotion": 3,
    "helpfulness": 4
  },
  "overall_score": 4,
  "confidence": 0.85
}
