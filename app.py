import streamlit as st
# App configuration
st.set_page_config(page_title="Smart City Assistant", layout="wide")
st.title("🌇 Sustainable Smart City Assistant")


from dotenv import load_dotenv

# Import all modules
from city_dashboard import show_city_health_dashboard
from waste_insights import run_waste_insights
from feedback import show_feedback_system
from eco_advice import show_eco_advice
from document_summarizer import show_summarizer
from city_chat import show_city_chat

# Load environment variables
load_dotenv()

# App configuration


# Navigation
menu_options = [
    "🏙️ City Health Dashboard",
    "📦 Waste Management Insights",
    "📣 Citizen Feedback System",
    "🌱 Eco Advice Assistant",
    "📝 Document Summarizer",
    "💬 City Chat Assistant"
]

selected = st.sidebar.selectbox("Menu", menu_options)

# Route to features
if selected == menu_options[0]:
    show_city_health_dashboard()
elif selected == menu_options[1]:
    run_waste_insights()
elif selected == menu_options[2]:
    show_feedback_system()
elif selected == menu_options[3]:
    show_eco_advice()
elif selected == menu_options[4]:
    show_summarizer()
elif selected == menu_options[5]:
    show_city_chat()