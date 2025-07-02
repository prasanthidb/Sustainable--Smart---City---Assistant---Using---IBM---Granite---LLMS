from huggingface_hub import InferenceClient
import streamlit as st

def show_city_chat():
    st.header("💬 City Chat Assistant (IBM Granite)")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{
            "role": "assistant", 
            "content": "Hello! I'm your Smart City Assistant powered by IBM Granite. How can I help?"
        }]
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Ask about city services"):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Consulting city knowledge..."):
                try:
                    client = InferenceClient(
                        model="ibm-granite/granite-3.3-2b-instruct",
                        token=st.secrets["HF_TOKEN"]  # Must have IBM model access
                    )
                    
                    # IBM Granite specific prompt formatting
                    granite_prompt = f"""Instruction: As a smart city assistant, provide a helpful response to this query.
                    
                    Query: {prompt}
                    
                    Response:"""
                    
                    response = client.text_generation(
                        granite_prompt,
                        max_new_tokens=200,
                        temperature=0.7
                    )
                    
                    # Clean up response
                    response = response.split("Response:")[-1].strip()
                    
                except Exception as e:
                    response = f"""I'm experiencing technical difficulties. 
                    (Error: {str(e)})
                    \n\nTry simpler questions or check back later."""
            
            st.markdown(response)
        
        st.session_state.messages.append({"role": "assistant", "content": response})