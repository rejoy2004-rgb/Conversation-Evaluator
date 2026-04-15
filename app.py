import streamlit as st
from src.preprocess import preprocess_conversation
from src.evaluator import evaluate_group
from src.aggregator import aggregate
from src.facet_loader import load_facets

# Load facets once
facets = load_facets("data/Facets Assignment.csv")

st.title("Conversation Evaluator")

# User input
user_input = st.text_area("Enter conversation:")

# Button
if st.button("Evaluate"):
    if user_input.strip():

        # Convert input into conversation format
        conversation = [
            {"text": user_input}
        ]

        # Preprocess
        processed = preprocess_conversation(conversation)

        # Evaluate
        facet_scores = evaluate_group(processed, facets)

        # Aggregate
        final = aggregate(facet_scores)

        # Show results
        st.subheader("Category Scores")
        st.json(final["scores"])

        st.subheader("Overall Score")
        st.write(final["overall_score"])

        st.subheader("Confidence")
        st.write(final["confidence"])

    else:
        st.warning("Please enter some text!")