import streamlit as st
import google.generativeai as genai


st.title("✨Gemini AI Bot✨")

f = open("keys\.gem_api.txt")
key = f.read()

genai.configure(api_key=key)

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              system_instruction="""You are a  AI Data Science Tutor. 
                                                  Given a tasked to resolve only the 
                                                  data science doubts of the user.""")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

st.chat_message("ai").write("Hi❕, How may I help you?")
chat = model.start_chat(history=st.session_state['chat_history'])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

user_prompt = st.chat_input()

if user_prompt:
    st.chat_message("user").write(user_prompt)
    response = chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    st.session_state['chat_history'] = chat.history

