import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye') 

name = st.text_input('Enter your name', 'Type here...')
st.write('Hello, ', name)

age = st.number_input('Select your age', 0, 130, 25)
st.write("I'm ", age, 'years old')

frequency = st.slider('Select frequency', 0, 100, 25)
st.write('Frequency is set to', frequency)
x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x*frequency)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Sine Wave with Frequency {}'.format(frequency))
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
st.pyplot(fig)

# create file uploader
uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt","json"])
if uploaded_file is not None:
    try:
        # Read the file into a DataFrame
        data = pd.read_json(uploaded_file)
        st.write("Here is the uploaded data:")
        st.dataframe(data)
    except Exception as e:
        st.error(f"Error reading file: {e}")
