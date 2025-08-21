import streamlit as st
# create distribution page
st.title("Distribution Page")
st.write("This page is dedicated to displaying various distributions.")
st.markdown("## Normal Distribution")
col1,col2 = st.columns(2)
with col1:
    st.write("### Normal Distribution Plot")
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Generate data
    data = np.random.normal(loc=0, scale=1, size=1000)

    # Create a seaborn distribution plot
    sns.histplot(data, kde=True)
    plt.title("Normal Distribution")
    plt.xlabel("Value")
    plt.ylabel("Frequency")

    # Display the plot in Streamlit
    st.pyplot(plt)
with col2:
    st.write("### Normal Distribution Statistics")
    mean = np.mean(data)
    std_dev = np.std(data)
    st.write(f"Mean: {mean:.2f}")
    st.write(f"Standard Deviation: {std_dev:.2f}")
st.write("This is a simple normal distribution plot with statistics.")
st.markdown("## Uniform Distribution")
