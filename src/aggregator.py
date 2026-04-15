def aggregate(facet_scores):
    categories = {
        "language": [],
        "safety": [],
        "emotion": [],
        "helpfulness": []
    }

    for facet, value in facet_scores.items():
        f = facet.lower()

        if any(k in f for k in ["grammar", "language", "fluency", "clarity"]):
            categories["language"].append(value)

        elif any(k in f for k in ["harm", "bias", "safety"]):
            categories["safety"].append(value)

        elif any(k in f for k in ["emotion", "empathy", "tone"]):
            categories["emotion"].append(value)

        else:
            categories["helpfulness"].append(value)

    # category averages
    category_scores = {
        cat: round(sum(vals)/len(vals), 2) if vals else 0
        for cat, vals in categories.items()
    }

    # overall score
    all_vals = list(facet_scores.values())
    overall = round(sum(all_vals) / len(all_vals))

    return {
        "facet_scores": facet_scores,
        "scores": category_scores,
        "overall_score": overall,
        "confidence": 0.85
    }