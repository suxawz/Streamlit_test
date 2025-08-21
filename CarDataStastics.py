import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Car Data Statistics")
st.write("This application provides statistics on car data.")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
if uploaded_file is not None:
    try:
        # Read the CSV file into a DataFrame
        car_data = pd.read_csv(uploaded_file)
        st.write("Here is the uploaded car data:")
        st.dataframe(car_data)

        # Display basic statistics
        st.write("Basic Statistics:")
        st.write(car_data.describe())

        # Create a histogram for a selected column
        column = st.selectbox("Select a column to plot", car_data.columns)
        if column:
            fig, ax = plt.subplots()
            car_data[column].hist(bins=30, ax=ax)
            ax.set_title(f"Histogram of {column}")
            ax.set_xlabel(column)
            ax.set_ylabel("Frequency")
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.write("Please upload a CSV file to see the car data statistics.")
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv")  # Example file for initial load

if st.checkbox("Show raw data"):
    st.write(car_data if 'car_data' in locals() else df)
    st.dataframe(df)
else:
    st.write("Raw data is hidden. Check the box to show it.")
st.subheader("select data")
manufactures = st.multiselect("Select manufacturers", options=car_data['origin'].unique(), default=car_data['origin'].unique())
if manufactures:
    filtered_data = car_data[car_data['origin'].isin(manufactures)]
    st.write(f"Filtered data for manufacturers: {manufactures}")
    st.dataframe(filtered_data)
st.write(f"data count: {len(car_data)}")
st.write("This is a simple car data statistics application using Streamlit.")
st.write(car_data.describe())

st.subheader("Cyliders VS MPG")
fig, ax = plt.subplots()
scatter = ax.scatter(car_data['cylinders'], car_data['mpg'], c=car_data['origin'].astype('category').cat.codes, cmap='viridis')
ax.set_xlabel('Cylinders')
ax.set_ylabel('Miles Per Gallon (MPG)')
ax.set_title('Cylinders vs MPG')
#st.color_picker(scatter, ax=ax, label='Origin')
ax.grid(True)
st.pyplot(fig)

st.subheader("model year")
select_year = st.slider("Select model year", min_value=int(car_data['model_year'].min()), max_value=int(car_data['model_year'].max()), value=int(car_data['model_year'].mean()))
filtered_year_data = car_data[car_data['model_year'] == select_year]
st.bar_chart(filtered_year_data['mpg'].value_counts(), use_container_width=True)
st.write(f"Data for model year {select_year}:")
st.dataframe(filtered_year_data)
st.write("Enjoy exploring car data statistics with Streamlit!")