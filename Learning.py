import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#generate some random data
x = np.random.rand(100, 1) * 10  # 100 random numbers between 0 and 10
y = 2.5 * x + np.random.randn(100, 1) * 2  # linear relation with some noise
# Create a linear regression model
model = LinearRegression()
# Fit the model
model.fit(x, y)
# Predict using the model
y_pred = model.predict(x)
# Create a scatter plot of the data
st.title("Linear Regression Example")
st.write("This is a simple linear regression example using Streamlit.")
st.write("Here is the data:")   
st.dataframe(pd.DataFrame({'x': x.flatten(), 'y': y.flatten()}))
# Create a scatter plot
st.write("Here is a scatter plot of the data:")
st.scatter_chart(pd.DataFrame({'x': x.flatten(), 'y': y.flatten()}))
# Create a line plot of the regression line
st.write("Here is the regression line:")
st.line_chart(pd.DataFrame({'x': x.flatten(), 'y': y_pred.flatten()}))
st.write("The regression line is shown in the plot above.") 
# Display the coefficients of the model
st.write("Model coefficients:")
st.write(f"Coefficient: {model.coef_[0][0]:.2f}, Intercept: {model.intercept_[0]:.2f}")
st.write("This is a simple linear regression example using Streamlit.")

user_input = st.number_input("Enter a value for x to predict y:", min_value=0.0, max_value=10.0, value=5.0)
if user_input is not None:
    user_input = np.array([[user_input]])
    prediction = model.predict(user_input)
    st.write(f"Predicted value of y for x={user_input[0][0]}: {prediction[0][0]:.2f}")
