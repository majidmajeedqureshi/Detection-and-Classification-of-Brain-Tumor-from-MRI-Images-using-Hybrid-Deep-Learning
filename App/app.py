import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# Define diseases and details
diseases = {
    "Glioma Tumor": "A type of tumor that occurs in the brain and spinal cord.",
    "Meningioma Tumor": "A tumor that arises from the meninges, the membranes that surround your brain and spinal cord.",
    "Pituitary Tumor": "A growth of abnormal cells in the tissues of the pituitary gland.",
    "No Tumor": "Indicates no presence of tumor in the brain MRI image."
}



# Streamlit application
st.set_page_config(page_title="Brain Tumor Classification", layout="centered")

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("", ["Home", "Predict"])

if page == "Home":
    st.title("Brain Tumor Classification")
    st.write("""
    This application can classify brain MRI images into the following categories:
    """)
    for disease, detail in diseases.items():
        st.write(f"**{disease}**: {detail}")

    st.write("\n\nModel Accuracy: **86%**")

    st.write("\n**Sample Prediction Image:**")
    sample_image = Image.open('model_predictions.png')
    st.image(sample_image, caption='Sample Prediction Image', use_column_width=True)

elif page == "Predict":
    pass
