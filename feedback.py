import streamlit as st
import pandas as pd
from datetime import datetime

def show_feedback_system():
    st.header("📣 Citizen Feedback")
    
    with st.form("feedback_form"):
        name = st.text_input("Name")
        issue = st.selectbox("Issue Type", 
                           ["Potholes", "Garbage", "Streetlights"])
        details = st.text_area("Details")
        
        if st.form_submit_button("Submit"):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            st.success(f"Thank you {name}! Your {issue} report was submitted.")