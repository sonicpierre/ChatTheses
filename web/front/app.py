import streamlit as st
from htmlTemplate import css, user_template, bot_template

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 ==0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)


st.set_page_config(page_title="Chat with Theses.fr",
                   page_icon=":books:")

st.write(css, unsafe_allow_html=True)

if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = None

st.header("Chat with multiple Theses.fr :book:")
user_question = st.text_input("Ask your question about documents")

if user_question:
    handle_userinput(user_question)


st.write(user_template.replace("{{MSG}}", "Hello I'm the user"), unsafe_allow_html=True)
st.write(bot_template.replace("{{MSG}}", "Hello I'm the bot"), unsafe_allow_html=True)