# 1st Assignment ( Streamlit Chatbot )
# UI design for the phoneix_ds.ipynb basic conversational chatbot 
# Using streamlit and groq API

import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("API_KEY")
)


# Page config
st.set_page_config(page_title="My Chatbot")
st.title("MY Chatbot")

system_prompt ={
    "role": "system",
    "content": "You are a hlepful AI, Your name is Rosey. You respond to the user query in helpful way."
}

# chat history

chat_history = [system_prompt]

if "chat_history" not in st.session_state:
    st.session_state.chat_history =[system_prompt]

for msg in st.session_state.chat_history[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Hi, How can i help you ?")

if user_input :
    user_query = {
        "role": "user",
        "content": user_input
    }
    st.session_state.chat_history.append(user_query)

    with st.chat_message("user"):
        st.write(user_input)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.chat_history,
        max_tokens=1500,
        temperature=0.7
    )
    result = response.choices[0].message.content
    print(f"AI: {result}")

    
    ai_response_context = {
        "role": "assistant",
        "content": result
    }
    st.session_state.chat_history.append(ai_response_context)

    with st.chat_message("assistant"):
        st.write(result)