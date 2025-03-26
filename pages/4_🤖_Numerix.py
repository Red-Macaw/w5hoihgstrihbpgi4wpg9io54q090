import streamlit as st
import time
import google.generativeai as genai

st.set_page_config(page_title="Numerix", page_icon="🤖")

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
    system_instruction = "You are Numerix, a friendly AI math tutor by NeuraSwift, created by Muthu Nilavan (Red Macaw), an 8th-grade coder. Teach math step-by-step, one step per chat. Greet the student by asking their name, grade, and favorite game. Use simple, fun explanations, relatable examples, and interactive questions. Confirm understanding before moving forward. Encourage with positive words. Summarize concepts and quiz students with 1-2 questions after each topic. If stuck, break steps further. Make math easy, engaging, and fun!"

)

# Initialize chat session in session state with correct format
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

    # 🔥 **Update chat session history in correct format**
    st.session_state.chat_session.history.append(
        {"role": "user", "parts": [{"text": prompt}]}
    )
    st.session_state.chat_session.history.append(
        {"role": "assistant", "parts": [{"text": response_text}]}
    )
