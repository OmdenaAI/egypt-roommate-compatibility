import streamlit as st

# Create a section for extrovert questions
st.header("Introvert/Extrovert Questions")

extrovert1 = st.text_input("Introvert 1")
extrovert2 = st.text_input("Introvert 2")
extrovert3 = st.text_input("Extrovert 1")
extrovert4 = st.text_input("Extrovert 2")

# Create a section for Lifrstyle Questions
st.header("Lifestyle Questions")

stress = st.text_input("How often do you get stressed up?")
sleep = st.text_input("How many hours do you sleep?")
fruits = st.text_input("How often do you take fruits?")

# Create a submit button to check for Introvert/Extrovert
predict = st.button("Find Match")