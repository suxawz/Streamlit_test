import streamlit as st
import cv2
import numpy as np
from PIL import Image
import requests

st.title("Image Processing Application")
st.write("This application allows you to upload an image and apply various processing techniques.") 
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Read the image file
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert the image to a NumPy array for OpenCV processing
    image_np = np.array(image)

    # Convert RGB to BGR (OpenCV uses BGR format)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image_bgr, (15, 15), 0)
    st.image(blurred_image, caption="Blurred Image", use_column_width=True)

    # Convert back to RGB for display in Streamlit
    blurred_image_rgb = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)
    
    # Display the processed image
    st.image(blurred_image_rgb, caption="Processed Image", use_column_width=True)

    edges = cv2.Canny(image_bgr, 100, 200)
    st.image(edges, caption="Edge Detection", use_column_width=True)