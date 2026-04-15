def preprocess_conversation(conversation):
    processed = []

    for turn in conversation:
        if isinstance(turn, dict):
            text = turn.get("text", "").strip()
        else:
            text = str(turn).strip()

        if text:
            processed.append({"text": text})

    return processed