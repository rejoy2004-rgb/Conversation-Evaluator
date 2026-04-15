import json
from src.preprocess import preprocess_conversation
from src.evaluator import evaluate_group
from src.aggregator import aggregate
from src.facet_loader import load_facets


# Load conversations from JSON file
# Each item contains-conversation_id, list of conversation turns

with open("data/sample_conversations.json", "r", encoding="utf-8") as f:
    conversations = json.load(f)

# Load ALL facets from CSV file (supports 300–5000 facets)

facets = load_facets("data/Facets Assignment.csv")

#total facets used
num_facets = len(facets)
print(f"Using {num_facets} facets for evaluation")

#Store final results for all conversations
all_results = []

#Process each conversation one by one
for idx, conv in enumerate(conversations, start=1):

    # handle different input formats safely
    if isinstance(conv, dict):
        raw_conv = conv.get("conversation", [])
        conv_id = conv.get("conversation_id", str(idx))
    else:
        raw_conv = conv
        conv_id = str(idx)

    # preprocess conversation:
    #extract text, remove empty entries, standardized format
    conversation = preprocess_conversation(raw_conv)

    if not conversation:
        continue

    #evaluate all facets (no grouping)
    scores = evaluate_group(conversation, facets)

    # aggregate results
    final = aggregate(scores)

    # build structuredoutput
    result = {
        "conversation_id": conv_id,
        "turn_id": 1,
        "num_facets_used": num_facets,  # 🔥 important
        "facet_scores": final["facet_scores"],   # ⭐ ADD THIS
        "scores": final["scores"],
        "overall_score": final["overall_score"],
        "confidence": final["confidence"]
    }

    #add to final results list

    all_results.append(result)

#Save results to JSON file
with open("results.json", "w", encoding="utf-8") as f:
    json.dump(all_results, f, indent=2)

#Print results to console 
print(json.dumps(all_results, indent=2))