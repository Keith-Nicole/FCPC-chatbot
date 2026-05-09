import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Force load the new vault since I updated the .env file with the new key and I don't know if this is the reason why the old key is still being used.
load_dotenv(override=True)

# Grab the key
my_secret_key = os.environ.get("GEMINI_API_KEY")

# 3. Authenticate
genai.configure(api_key=my_secret_key)

# 4. Read the Knowledge Base from the text file
# Using utf-8 encoding ensures it reads symbols and quotes perfectly
with open("knowledge_base.txt", "r", encoding="utf-8") as file:
    school_context = file.read()

# 5. Initialize the AI Model
model = genai.GenerativeModel(
    'gemini-2.5-flash',
    system_instruction=school_context
)

# 6. Streamlit UI Setup
st.title("Ask ProviBot, your FCPC Campus Buddy!🏫")

# Initialize chat history in Streamlit's session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Display previous chat messages
for message in st.session_state.chat.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# 7. Handle User Input
if prompt := st.chat_input("Ask me anything about FCPC..."):
    # 1. Show the user's message on screen
    st.chat_message("user").markdown(prompt)
    
    # 2. Try to get a response from Gemini
    try:
        # --> The Spinner goes here! <--
        with st.spinner("ProviBot thinking..."):
            response = st.session_state.chat.send_message(prompt)
        
        # If successful, show AI response
        with st.chat_message("assistant"):
            st.markdown(response.text)
            
    # 3. If Gemini crashes (like hitting the speed limit), catch the error!
    except Exception as e:
        error_message = str(e).lower()
        
        # Check if it is a 429 Quota Error
        if "429" in error_message or "quota" in error_message:
            with st.chat_message("assistant"):
                st.error("🏫 **Whoa there!** I am receiving too many questions at once. Please give me about 60 seconds to catch my breath, then try asking again!")
        
        # Catch any other random errors just in case
        else:
            with st.chat_message("assistant"):
                st.error("Oops! My system encountered a minor glitch. Please try again.")