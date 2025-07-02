import streamlit as st
from huggingface_hub import InferenceClient

def show_eco_advice():
    st.header("🌱 Eco Advice")
    question = st.text_area("Ask for sustainability advice:")
    
    if question and st.button("Get Advice"):
        client = InferenceClient(
            model="ibm-granite/granite-3.3-2b-instruct",
            token=st.secrets["HF_TOKEN"]
        )
        advice = client.text_generation(
            f"Give eco-friendly advice about: {question}",
            max_new_tokens=200
        )
        st.success(advice)