# 💬 Conversation Evaluator

## 📌 Overview
This project implements a scalable conversation evaluation system that scores conversations across 300+ facets covering:

- Language Quality  
- Safety  
- Emotion  
- Helpfulness  

The system is designed to be production-ready, modular, and scalable up to 5000+ facets without changing the architecture.

---

## 🎯 Objective
To design a benchmark system that:
- Evaluates each conversation turn
- Uses 300+ distinct facets
- Produces structured scores with confidence values
- Scales efficiently to large datasets

---

## ⚙️ Key Features

### ✅ Scalable Architecture
- Dynamically loads facets from CSV
- No hardcoding → supports 300–5000 facets

### ✅ Modular Design
- Preprocessing
- Evaluation
- Aggregation
- Facet loading

### ✅ Facet-Level Scoring
- Each facet is scored between 1–5
- Covers multiple aspects of conversation quality

### ✅ Category-Level Aggregation
- Facets grouped into:
  - Language
  - Safety
  - Emotion
  - Helpfulness
- Scores computed using averages

### ✅ Confidence Score
- Outputs a confidence value for each evaluation

### ✅ Streamlit UI
- Allows user input
- Displays evaluation results interactively

---

## 🧠 Methodology

### 1. Data Preprocessing
- Cleans conversation text
- Standardizes format
- Removes empty or invalid entries

### 2. Facet Loading
- Loads facets from CSV file
- Cleans facet names (removes numbering and symbols)
- Filters invalid or corrupted entries

### 3. Evaluation Engine
- Rule-based scoring logic:
  - Language → clarity, fluency
  - Safety → harmful content detection
  - Emotion → sentiment indicators
  - Helpfulness → assistance-related words
- Adds slight randomness for variation

### 4. Aggregation
- Groups facet scores into categories
- Computes:
  - Category scores
  - Overall score
  - Confidence

---

## 📊 Output Format

```json
{
  "conversation_id": "1",
  "num_facets_used": 399,
  "facet_scores": {
    "Clarity": 4,
    "Empathy": 5
  },
  "scores": {
    "language": 4,
    "safety": 4,
    "emotion": 3,
    "helpfulness": 4
  },
  "overall_score": 4,
  "confidence": 0.85
}

conversation_evaluator/
│
├── data/
│   ├── sample_conversations.json
│   └── Facets Assignment.csv
│
├── src/
│   ├── preprocess.py
│   ├── evaluator.py
│   ├── aggregator.py
│   └── facet_loader.py
│
├── app.py
├── main.py
├── model.py
├── requirements.txt
└── results.json
🚀 How to Run
1. Install dependencies

pip install -r requirements.txt

2. Run evaluation

py main.py

3. Run UI

streamlit run app.py

🧪 Dataset
Contains 300+ conversations
Each conversation has multiple turns
Easily extendable
🔒 Constraints Satisfied
No one-shot prompt solution
Modular architecture
Supports ≥5000 facets
Compatible with open-weight models
🎁 Bonus Features
Confidence scoring
Streamlit UI
Scalable design
🧠 Future Improvements
Replace rule-based scoring with LLM-based evaluation
Add visual dashboards (charts)
Improve sentiment analysis
Support multi-turn deep reasoning
👨‍💻 Author

Rejoy Besra
