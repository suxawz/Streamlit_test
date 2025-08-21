import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

st.header("Welcome to Streamlit")
st.title("Streamlit E2ample")
st.write("Hello, Streamlit!")   

st.markdown('### This is a markdown title')
#create a simple plot
x = np.linspace(0, 10, 100) 
y = np.sin(x)
fig, ax = plt.subplots()    
ax.plot(x, y)
st.pyplot(fig)      
st.write("This is a simple line plot of y = sin(x)")   
# Create a simple DataFrame
data = pd.DataFrame({'A': np.random.randn(100), 'B': np.random.randn(100)})
st.write("Here is a simple DataFrame:")     
# Display the DataFrame
st.dataframe(data)  
# Create a simple seaborn plot
fig2, ax2 = plt.subplots()
sns.scatterplot(x='A', y='B', data=data, ax=ax2)
st.pyplot(fig2)
st.write("This is a scatter plot of the DataFrame using seaborn")
st.write("Streamlit application is running!")
st.write("Enjoy using Streamlit for your web applications!")
st.write("This is a simple line plot of y = sin(x)")   
st.write("Here is a simple DataFrame:") 