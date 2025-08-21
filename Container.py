import streamlit as st
#create a container for the Streamlit app
st.title("Streamlit Container Example")
st.write("This is a simple example of using a container in Streamlit.")
# Create a container
with st.container():
    st.write("This is inside the container.")
    st.write("You can add multiple elements here.")
    st.markdown("### Markdown inside container")
    st.text("This is a text element inside the container.")
    st.button("Click me!")
    st.write("You can also add interactive elements like buttons inside the container.")
# Create another container
with st.container():
    st.write("This is another container.")
    st.write("You can have multiple containers in your Streamlit app.")
    st.markdown("### Another Markdown inside container")
    st.text("This is another text element inside a different container.")
    st.button("Click me too!")
    st.write("Each container can have its own set of elements and interactivity.")
# Display a message outside the containers
st.write("This is outside the containers.")
# You can use containers to organize your Streamlit app layout
st.write("Containers help in grouping related elements together for better organization.")
# You can also use containers to create sections in your app
st.write("You can create sections in your app using containers for better readability.")
# Display a final message
st.write("This is the end of the Streamlit Container Example.")
st.sidebar.title("Sidebar")
st.sidebar.write("This is a sidebar in the Streamlit app.")
st.sidebar.write("You can add elements to the sidebar as well.")
st.sidebar.button("Click me in the sidebar!")
option = st.sidebar.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", option)
st.sidebar.write("This is a sidebar in the Streamlit app.")
st.write("You can also add interactive elements in the sidebar.")
st.write("Enjoy using Streamlit for your web applications!")
