import streamlit as st
import json
from main import final

#Set title of the Streamlit app
st.title("Conversation Evaluator")

#Display evaluation results in a JSON format
st.json(final)