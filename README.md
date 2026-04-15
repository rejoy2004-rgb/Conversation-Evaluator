# 💬 Conversation Evaluator (AI & ML Assignment)

## 📌 Overview
This project builds a scalable system to evaluate conversations using 300+ facets across:
- Language quality
- Safety
- Emotion
- Helpfulness

## ⚙️ Features
- Supports 300–5000 facets without redesign
- Modular architecture
- Rule-based + LLM-ready design
- JSON output with scores + confidence
- Streamlit UI for interaction

## 🧠 Methodology
1. Preprocess conversation
2. Evaluate across all facets
3. Aggregate into categories
4. Compute overall score + confidence

## 📊 Output Format
```json
{
  "conversation_id": "1",
  "scores": {
    "language": 4,
    "safety": 4,
    "emotion": 3,
    "helpfulness": 4
  },
  "overall_score": 4,
  "confidence": 0.85
}
