import streamlit as st
import pandas as pd
import numpy as np

st.write('Got lots of data? Streamlit can show [dataframes](https://docs.streamlit.io/develop/api-reference/data) with hundred thousands of rows, images, sparklines - and even supports editing!')
st.title("Data Table Example")
num_rows = st.slider("Number of rows", min_value=1, max_value=10000, value=1000, step=100)
np.random.seed(42)  # For reproducibility
data = []
for i in range(num_rows):
    data.append({
        "Preview": f"https://picsum.photos/seed/{i}/200/300",
        "Views": np.random.randint(0, 1000),
        "Active": np.random.choice([True, False]),
        "Category": np.random.choice(['LLM', 'Data', 'Tools', 'Web']),
        "Progress": np.random.randint(0, 100),
        "Date": pd.to_datetime(f"2023-10-{np.random.randint(1, 31)}"),
        "Text": f"This is a sample text for row {i+1}." 
    })
df = pd.DataFrame(data)
config = {"Preview": st.column_config.ImageColumn(),"Progress": st.column_config.ProgressColumn(), "Views": st.column_config.NumberColumn(), "Active": st.column_config.CheckboxColumn(), "Category": st.column_config.SelectboxColumn(options=['LLM', 'Data', 'Tools', 'Web']), "Date": st.column_config.DateColumn(), "Text": st.column_config.TextColumn()}
if st.toggle('enable editing', key='edit'):
    df = st.data_editor(df, use_container_width=True, column_config=config, num_rows="dynamic", hide_index=True)
else:
    st.write("Editing is disabled. Toggle the switch to enable editing.")
    st.dataframe(df, use_container_width=True, column_config=config)
st.write("This is a simple data table example using Streamlit.")
st.write("You can edit the data, filter it, and even visualize it with charts.")
st.write("Enjoy exploring the data!")