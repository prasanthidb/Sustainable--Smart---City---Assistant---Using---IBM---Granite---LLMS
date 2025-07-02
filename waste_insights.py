import streamlit as st
import pandas as pd
import plotly.express as px

def run_waste_insights():
    st.title("📦 Waste Insights")
    
    data = {
        "Zone": ["North", "South", "East", "West"],
        "Recycling": [45, 32, 28, 39],
        "Landfill": [30, 45, 52, 41]
    }
    df = pd.DataFrame(data)
    
    fig = px.bar(df, x="Zone", y=["Recycling", "Landfill"], 
                 title="Waste by Zone")
    st.plotly_chart(fig)