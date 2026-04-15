def aggregate(facet_scores):
    #Initialize category which will store values of facets
    categories = {
        "language": [],
        "safety": [],
        "emotion": [],
        "helpfulness": []
    }

    #Classify facets into a category based on keyword matching

    for facet, value in facet_scores.items():
        f = facet.lower()

        # Language category
        if any(k in f for k in [
            "grammar", "language", "fluency", "clarity",
            "sentence", "spelling", "brevity"
        ]):
            categories["language"].append(value)

        # Safety category
        elif any(k in f for k in [
            "harm", "bias", "safety", "violence",
            "risk", "toxicity"
        ]):
            categories["safety"].append(value)

        # Emotion category
        elif any(k in f for k in [
            "emotion", "empathy", "feeling",
            "tone", "mood", "compassion"
        ]):
            categories["emotion"].append(value)

        # default: Helpfulness category
        else:
            categories["helpfulness"].append(value)

    # compute average score
    category_scores = {}
    for cat, vals in categories.items():
        if len(vals) > 0:
            category_scores[cat] = round(sum(vals) / len(vals))
        else:
            category_scores[cat] = 0

    # overall score for all facets
    all_vals = list(facet_scores.values())
    overall = round(sum(all_vals) / len(all_vals))

    # Return structured Output
    return {
        "facet_scores": facet_scores,   # Full 300+ facets
        "scores": category_scores,      # aggregated category scores
        "overall_score": overall,       #final overall score
        "confidence": round(0.7 + 0.3 * (len(facet_scores) / 500), 2)   #Confidence of evaluation
    }