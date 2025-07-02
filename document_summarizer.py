import streamlit as st
from huggingface_hub import InferenceClient

def show_summarizer():
    st.header("📝 Document Summarizer")
    uploaded_file = st.file_uploader("Upload document", type=["txt"])
    
    if uploaded_file and st.button("Summarize"):
        text = uploaded_file.read().decode("utf-8")
        client = InferenceClient(
            model="ibm-granite/granite-3.3-2b-instruct",
            token=st.secrets["HF_TOKEN"]
        )
        summary = client.text_generation(
            f"Summarize this: {text[:2000]}",
            max_new_tokens=200
        )
        st.text_area("Summary", summary)