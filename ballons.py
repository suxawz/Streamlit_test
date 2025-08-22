import streamlit as st

st.title("Balloon Counter")
st.write("This application allows you to count balloons.")

st.markdown("""
### Instructions:This is a simple balloon counter application.
**There's: rainbow[so much fun]** in counting balloons!
1. Click the **Add Balloon** button to increase the count.
2. Click the **Remove Balloon** button to decrease the count.
3. The count will update automatically.
""")
if st.button("Add Balloon"):
    if 'balloon_count' not in st.session_state:
        st.session_state.balloon_count = 0
    st.session_state.balloon_count += 1
if st.button("Remove Balloon"):
    if 'balloon_count' in st.session_state and st.session_state.balloon_count > 0:
        st.session_state.balloon_count -= 1
st.write(f"Current Balloon Count: {st.session_state.get('balloon_count', 0)}")  
st.write("This is a simple balloon counter application.")
st.write("Click the buttons to add or remove balloons.")
st.balloons()  # This will trigger the balloon animation in Streamlit
st.write("Enjoy counting balloons!")    
