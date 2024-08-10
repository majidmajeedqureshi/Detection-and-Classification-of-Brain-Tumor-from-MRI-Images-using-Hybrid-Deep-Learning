import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('best_model.h5')

# Define diseases and details
diseases = {
    "Glioma Tumor": "A type of tumor that occurs in the brain and spinal cord.",
    "Meningioma Tumor": "A tumor that arises from the meninges, the membranes that surround your brain and spinal cord.",
    "Pituitary Tumor": "A growth of abnormal cells in the tissues of the pituitary gland.",
    "No Tumor": "Indicates no presence of tumor in the brain MRI image."
}

# Function to preprocess the image
def preprocess_image(image):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize((150, 150))
    image = np.array(image)
    image = image / 255.0  # Normalize the image to [0, 1] range
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Function to predict the disease
def predict_disease(image):
    preprocessed_image = preprocess_image(image)
    predictions = model.predict([preprocessed_image, preprocessed_image])
    predicted_class = np.argmax(predictions, axis=1)[0]
    return predicted_class

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
    st.title("Predict Brain Tumor")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        if st.button("Predict"):
            predicted_class = predict_disease(image)
            disease_name = list(diseases.keys())[predicted_class]
            st.write(f"**Predicted Disease:** {disease_name}")
