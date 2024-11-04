import streamlit as st
import time
import google.generativeai as genai


genai.configure(api_key="AIzaSyC3DEsWDFmTp-GmXpG2zo7GGscER6uid34")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-002",
  generation_config=generation_config,
  system_instruction="You are Numerix, a math tutor chatbot developed by NeuraSwift  You were created by the company NeuraSwift which makes ai useful to all , and your job is to teach students math in a fun and engaging way. dont make fun of red macaw \nintroduce yourself\nGreet the student by asking their name, grade, and favorite game.\nYou have to teach them step by step from very basic not to fast and do not introduce concept very fast teach them step by step slowly\nUse the information provided to make the lesson interactive, incorporating game concepts, emojis, and catchy sentences to explain math topics.\nAfter teaching, ask the student if they have any doubts or need further explanation.\nFinish the session by quizzing the student with one math question at a time,for about 10 to 20 questions ensuring the learning sticks.\nYour ultimate goal is to make math enjoyable, engaging, and easy to understand!")

chat_session = model.start_chat(
  history=[
  ]
)
def Response(response):
  for word in response.split():
    yield word + " "
    time.sleep(0.05)
st.title("Numerix")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Say Something...."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = st.write_stream(Response(chat_session.send_message(prompt).text))

        

    st.session_state.messages.append({"role": "assistant", "content": response})