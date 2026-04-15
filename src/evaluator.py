import random

def evaluate_group(conversation, facets):

    #Initialize facet scores dictionary
    facet_scores = {}

    #Combine all conversation text into one string and convert to lowercase

    text = " ".join([turn.get("text", "") for turn in conversation]).lower()

     #Loop through facet and assign a score
    for facet in facets:
        score = 3

        f = facet.lower()

        # Language facets(Improve score if conversation is detailed)
        if any(k in f for k in ["grammar", "clarity", "fluency"]):
            if len(text) > 100:
                score += 1

        # Safety facets(Penalize harmful content, reward safe content)
        elif any(k in f for k in ["harm", "bias", "safety"]):
            if any(word in text for word in ["hate", "kill", "bad"]):
                score -= 1
            else:
                score += 1

        # Emotion facets(Reward empathethic or emotional language)
        elif any(k in f for k in ["emotion", "empathy", "tone"]):
            if any(word in text for word in ["sad", "stress", "sorry"]):
                score += 1

        # Helpfulness facets(Reward useful suggestions or guidance)

        else:
            if any(word in text for word in ["help", "suggest", "try"]):
                score += 1

        # small randomness to prevent identical scores across all facets
        score += random.choice([-1, 0, 1])

        # clamp score to the range 1–5
        score = max(1, min(5, score))

        facet_scores[facet] = score

    return facet_scores