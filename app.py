import streamlit as st
from utils.llm import hf_generate

st.set_page_config(page_title="AI Study Buddy", page_icon="📘")

st.title("📘 AI Study Buddy")
st.write("Explain topics, summarize notes, and generate quizzes")

option = st.sidebar.selectbox(
    "Choose a feature",
    ("Explain Topic", "Summarize Notes", "Generate Quiz")
)

if option == "Explain Topic":
    topic = st.text_input("Enter topic")
    if st.button("Explain"):
        if topic:
            prompt = f"Explain the topic '{topic}' in simple words."
            st.write(hf_generate(prompt))
        else:
            st.warning("Enter a topic")

elif option == "Summarize Notes":
    notes = st.text_area("Paste notes")
    if st.button("Summarize"):
        if notes:
            prompt = f"Summarize the following notes:\n{notes}"
            st.write(hf_generate(prompt))
        else:
            st.warning("Paste some notes")

elif option == "Generate Quiz":
    topic = st.text_input("Enter quiz topic")
    if st.button("Generate Quiz"):
        if topic:
            prompt = f"Create 5 MCQ questions with answers on {topic}"
            st.write(hf_generate(prompt))
        else:
            st.warning("Enter a topic")