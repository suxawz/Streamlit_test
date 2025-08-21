import streamlit as st
import plotly.express as px
import altair as alt
import numpy as np
import pandas as pd
# Set the title of the Streamlit app
st.title("Plotly Example in Streamlit")
# Create a simple DataFrame
data = pd.DataFrame({'A': ['A','B','C','D'], 'B': [25,40,15,30]})
# Display the DataFrame
st.write("Here is a simple DataFrame:") 
st.dataframe(data)
# Create a simple bar chart using Plotly    
fig = px.line(data, x='A', y='B', title='Simple Bar Chart')
# Display the Plotly figure in Streamlit
st.plotly_chart(fig)
st.write("This is a simple bar chart created with Plotly")
# Create a simple scatter plot using Plotly
x = np.random.rand(100)
y = np.random.rand(100)
fig2 = px.scatter(x=x, y=y, title='Simple Scatter Plot')
# Display the scatter plot
st.plotly_chart(fig2)
st.write("This is a simple scatter plot created with Plotly")
st.write("Enjoy using Streamlit for your web applications!")
# Display a simple Altair chart
alt_data = pd.DataFrame({'x': np.random.rand(100), 'y': np.random.rand(100)})
alt_chart = alt.Chart(alt_data).mark_circle(size=60).encode(x='x', y='y', tooltip=['x', 'y']).interactive()
st.altair_chart(alt_chart, use_container_width=True)