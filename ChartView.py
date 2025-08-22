import streamlit as st
import random
import time

st.write("This is a simple chart view application using Streamlit.")
st.write('Streamlit loves LLMs! [Build your own xhat app](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-app) with Streamlit.that make it powerful by adding images, dataframe, or even imput widgests to the chat interface.')
st.caption('Note that this demo app is for demonstration purposes only and may not be suitable for production use.')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]

#display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
# if user_input := st.chat_input("Type your message here"):
if user_input := st.text_input("Type your message here"):
    # Display user message in chat message container
    st.chat_message("user").markdown(user_input)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        # Simulate a streaming response from an LLM
        for response_chunk in ["Sure! ", "Here is ", "a simple ", "chart view ", "application ", "using Streamlit."]:
            full_response += response_chunk
            time.sleep(random.uniform(0.1, 0.5))  # Simulate delay
            message_placeholder.markdown(full_response + "▌")  # Display partial response with cursor
        message_placeholder.markdown(full_response)  # Display full response

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
st.write("This is a simple chart view application using Streamlit.")
st.write("You can interact with the chat interface to get responses from the assistant.")    