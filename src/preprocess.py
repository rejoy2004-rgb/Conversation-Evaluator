def preprocess_conversation(conversation):

    """
    Preprocess raw conversation data into a clean format.

    Steps:
    1. Extract text from each turn
    2. Handle both dict and string formats
    3. Remove empty or invalid entries
    4. Return standardized structure for evaluation
    """

    #Initialize list to store processed turns
    processed = []

    #Loop through each turn in the conversation

    for turn in conversation:

        #If turn is a dictionary, extract text safely
        if isinstance(turn, dict):
            text = turn.get("text", "").strip()
        #If turn is not a dict convert it to string
        else:
            text = str(turn).strip()
        #Skip empty or blank messages
        if text:

            #Store in standardized format
            processed.append({"text": text})

    return processed