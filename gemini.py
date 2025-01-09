# to run this program, type the following command in the terminal:
# streamlit run gemini.py
# for installing streamlit, type the following command in the terminal:
# pip install streamlit
# for installing generativeai, type the following command in the terminal:
# pip install google-generativeai

import google.generativeai as genai
import streamlit as st
# getting the environment variables
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# **1. Configure the API Key**
# This line sets the API key for accessing the Google Generative AI services. 
# Get the API key from the environment variable
api_key = os.environ.get("GENAI_API_KEY")

# Configure the Google Generative AI client
genai.configure(api_key=api_key)

# **2. Load the Gemini Model**
# This line specifies the language model to be used for generating responses. 
# "gemini-1.5-flash" is a powerful and versatile model.
model = genai.GenerativeModel("gemini-1.5-flash")

def main():
    # **3. Set up the Streamlit App**
    st.title("Gemini Chatbot (Powered by Gemini-1.5-Flash)") 

    # **4. Initialize Conversation History**
    # This checks if a "conversation_history" key exists in the Streamlit session state. 
    # If not, it creates an empty list to store the conversation history.
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []

    # **5. Get User Input**
    # This creates a form for the user to enter their message.
    with st.form("my_form"):
        user_input = st.text_input("You:", key="user_input")
        submitted = st.form_submit_button("Send")

    # **6. Process User Input**
    if submitted:
        # **7. Input Validation**
        if not user_input:
            st.error("Please enter a message.")
        elif len(user_input) > 100:
            st.error("Character limit exceeded. Please keep your message under 100 characters.")
        else:
            # **8. Add User Message to History**
            st.session_state.conversation_history.append({"role": "user", "content": user_input})

            # **9. Generate Response**
            response = model.generate_content(user_input) 

            # **10. Add Assistant Response to History**
            st.session_state.conversation_history.append({"role": "assistant", "content": response.text})

    # **11. Display Conversation History**
    for message in st.session_state.conversation_history:
        if message["role"] == "user":
            # **12. Style User Messages**
            # This creates a visually distinct style for user messages 
            # (red background for readability).
            st.markdown(
                f"<div style='background-color:#e26161;color:white;float:right;padding:10px;border-radius:5px;margin-top:10px;'>{message['content']}</div><div style='clear:both;'></div>",
                unsafe_allow_html=True,
            )
        else:
            # **13. Style Assistant Messages**
            # This creates a visually distinct style for assistant messages 
            # (gray background for readability).
            st.markdown(
                f"<div style='background-color:#3b3b3b;color:white;padding:10px;border-radius:5px;margin-top:10px;'>{message['content']}</div>",
                unsafe_allow_html=True,
            )

if __name__ == "__main__":
    main()