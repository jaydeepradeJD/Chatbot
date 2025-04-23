import streamlit as st
from chat_logic import chatbot, HumanMessage, AIMessage

st.set_page_config(page_title="LangGraph Chatbot", layout="centered")

st.title("🧠 LangGraph Multi-turn Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_state" not in st.session_state:
    st.session_state.chat_state = {
        "messages": [],
        "user_input": ""
    }

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message("user" if isinstance(msg, HumanMessage) else "assistant"):
        st.markdown(msg.content)

# Input form
if prompt := st.chat_input("Ask me anything..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.chat_state["user_input"] = prompt
    result = chatbot.invoke(st.session_state.chat_state)

    # Append new messages
    st.session_state.messages.append(HumanMessage(content=prompt))
    st.session_state.messages.append(result["messages"][-1])
    st.session_state.chat_state["messages"] = result["messages"]

    # Display bot reply
    with st.chat_message("assistant"):
        st.markdown(result["messages"][-1].content)
