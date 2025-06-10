import streamlit as st
from summarize import summarize_text

st.title("📝 Text Summarization Tool")
st.write("Paste or upload a large text file, and get a clean, short summary.")

option = st.radio("Choose input method:", ("Paste Text", "Upload .txt File"))

input_text = ""

if option == "Paste Text":
    input_text = st.text_area("Paste your text here:", height=300)
else:
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    if uploaded_file is not None:
        input_text = uploaded_file.read().decode("utf-8")

if st.button("Summarize"):
    if input_text.strip() == "":
        st.warning("Please provide some text.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarize_text(input_text)
            st.success("Summary Generated:")
            st.text_area("Summary", summary, height=200)
