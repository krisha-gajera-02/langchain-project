import streamlit as st
from chains.solution_chain import get_solution_chain

st.set_page_config(page_title="AI Solution Consultant", layout="centered")

st.title("🤖 AI Solution Consultant")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous messages (Chat UI)
for user_msg, ai_msg in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(user_msg)
    with st.chat_message("assistant"):
        st.write(ai_msg)

# Chat input box (modern Streamlit)
user_input = st.chat_input("Describe your business problem...")

if user_input:
    # Show user message instantly
    with st.chat_message("user"):
        st.write(user_input)

    with st.spinner("Thinking..."):
        chain = get_solution_chain()

        # 🔑 IMPORTANT FIX: correct input keys
        response = chain.invoke({
            "question": user_input,
            "chat_history": st.session_state.chat_history
        })

        answer = response["answer"]

    # Show AI response
    with st.chat_message("assistant"):
        st.write(answer)

    # Save conversation
    st.session_state.chat_history.append((user_input, answer))
#
