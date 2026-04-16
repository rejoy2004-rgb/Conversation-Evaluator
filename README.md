# 💬 Conversation Evaluator

---

## 📌 Overview
This project implements a scalable conversation evaluation system that scores conversations across **300+ facets** covering:

- Language Quality  
- Safety  
- Emotion  
- Helpfulness  

The system is designed to be **production-ready, modular, and scalable up to 5000+ facets** without changing the architecture.

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
- No hardcoding → supports **300–5000 facets**  

### ✅ Modular Design
- Preprocessing  
- Evaluation  
- Aggregation  
- Facet loading  

### ✅ Facet-Level Scoring
- Each facet is scored between **1–5**  
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
## Live Demo
Streamlit App: https://conversation-evaluator-rejoy2004rgb.streamlit.app

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

