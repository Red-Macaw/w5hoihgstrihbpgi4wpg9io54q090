import streamlit as st
import time
import google.generativeai as genai

st.set_page_config(page_title="Numerix Updated", page_icon="🤖")

genai.configure(api_key="AIzaSyBtrqgyF59sayLsXvw549YXgmxhxm8Lgb0")

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
    system_instruction="You are Numerix, a math tutor chatbot developed by NeuraSwift. You were created by the company NeuraSwift which makes AI useful to all, and your job is to teach students math in a fun and engaging way. Don't make fun of the red macaw.\nIntroduce yourself.\nGreet the student by asking their name, grade, and favorite game.\nYou have to teach them step by step from very basic, not too fast, and do not introduce concepts very fast. Teach them step by step slowly.\nUse the information provided to make the lesson interactive, incorporating game concepts, emojis, and catchy sentences to explain math topics.\nAfter teaching, ask the student if they have any doubts or need further explanation.\nFinish the session by quizzing the student with one math question at a time, for about 10 to 20 questions, ensuring the learning sticks.\nYour ultimate goal is to make math enjoyable, engaging, and easy to understand!"
)

# Initialize session state for chat session
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

def Response(response_text):
    """Function to stream the AI response with a typing effect."""
    for word in response_text.split():
        yield word + " "
        time.sleep(0.05)

st.title("Numerix")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Say Something...."):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get response from AI while maintaining history
    response_obj = st.session_state.chat_session.send_message(prompt)
    response_text = response_obj.text  # Extract response text

    with st.chat_message("assistant"):
        st.write_stream(Response(response_text))

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": response_text})

    # 🔥 **Update chat session history so AI remembers**
    st.session_state.chat_session.history.append({"role": "user", "content": prompt})
    st.session_state.chat_session.history.append({"role": "assistant", "content": response_text})
