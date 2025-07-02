import streamlit as st
import pandas as pd
import altair as alt

def show_city_health_dashboard():
    st.title("🏙️ City Health Dashboard")
    
    data = {
        'Metric': ['Air Quality', 'Water Purity', 'Noise Levels', 'Waste Management'],
        'Value': [72, 88, 65, 80]
    }
    df = pd.DataFrame(data)
    
    chart = alt.Chart(df).mark_bar().encode(
        x='Metric',
        y='Value',
        color='Metric'
    )
    st.altair_chart(chart, use_container_width=True)