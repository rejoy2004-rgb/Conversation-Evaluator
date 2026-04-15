import random

def evaluate_group(conversation, facets):
    facet_scores = {}

    # combine all text
    text = " ".join([turn.get("text", "") for turn in conversation]).lower()

    for facet in facets:
        score = 3
        f = facet.lower()

        # LANGUAGE
        if any(k in f for k in ["grammar", "clarity", "fluency"]):
            if len(text) > 50:
                score += 1

        # SAFETY
        elif any(k in f for k in ["harm", "bias", "safety"]):
            if any(word in text for word in ["hate", "kill", "bad"]):
                score -= 1
            else:
                score += 1

        # EMOTION
        elif any(k in f for k in ["emotion", "empathy", "tone"]):
            if any(word in text for word in ["sad", "stress", "sorry"]):
                score += 1

        # HELPFULNESS
        else:
            if any(word in text for word in ["help", "suggest", "try"]):
                score += 1

        # variation
        score += random.choice([-1, 0, 1])

        # clamp 1–5
        score = max(1, min(5, score))

        facet_scores[facet] = score

    return facet_scores