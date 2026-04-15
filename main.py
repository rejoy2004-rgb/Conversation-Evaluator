import json
from src.preprocess import preprocess_conversation
from src.evaluator import evaluate_group
from src.aggregator import aggregate
from src.facet_loader import load_facets

# load conversations
with open("data/sample_conversations.json", "r", encoding="utf-8") as f:
    conversations = json.load(f)

# load facets
facets = load_facets("data/Facets Assignment.csv")
num_facets = len(facets)

all_results = []

for idx, conv in enumerate(conversations, start=1):

    raw_conv = conv.get("conversation", [])
    conv_id = conv.get("conversation_id", str(idx))

    processed = preprocess_conversation(raw_conv)

    if not processed:
        continue

    facet_scores = evaluate_group(processed, facets)
    final = aggregate(facet_scores)

    result = {
        "conversation_id": conv_id,
        "turn_id": 1,
        "num_facets_used": num_facets,
        "facet_scores": final["facet_scores"],
        "scores": final["scores"],
        "overall_score": final["overall_score"],
        "confidence": final["confidence"]
    }

    all_results.append(result)

# save
with open("results.json", "w", encoding="utf-8") as f:
    json.dump(all_results, f, indent=2)

# print
print(json.dumps(all_results, indent=2))