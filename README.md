# Detection and Classification of Brain Tumor from MRI Images using Hybrid Deep Learning

## Overview
This project aims to enhance the accuracy of brain tumor detection and classification from MRI images by using a hybrid deep learning model that incorporates multiple Convolutional Neural Networks (CNNs). The hybrid model is designed to leverage the strengths of different CNN architectures to improve the precision and accuracy of detecting and classifying brain tumors.

## Research Question
Is it possible to enhance the accuracy of brain tumor detection and classification from MRI images by using a deep learning model that incorporates several CNNs?

## Project Objectives
1. **Develop a Hybrid Model:** Create a hybrid deep learning model by combining multiple CNN architectures to increase the precision and accuracy of brain tumor detection and classification from MRI images.
2. **Model Training and Evaluation:** Train the hybrid model on the provided dataset, ensuring rigorous testing and validation to achieve high performance.
3. **User Interface Development:** Design a user-friendly UI using Streamlit, integrating the developed model to allow end-users to easily upload MRI images and receive classification results.

## Project Timeline
- **May 15, 2024:** Project start date
- **May 15 - May 31, 2024:** Literature review and dataset collection
- **June 1 - June 30, 2024:** Model development and initial testing
- **July 1 - July 31, 2024:** Model refinement and user interface development
- **August 1 - August 15, 2024:** Final testing, validation, and documentation
- **August 25, 2024:** Project submission

## Data Management Plan
### Data Collection
The dataset used for this project is publicly available on Kaggle: [Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset?select=Testing).

### Dataset Overview
- **Training Data:** 5712 images
- **Testing Data:** 1311 images
- **Categories:** No Tumor, Glioma, Pituitary, Meningioma
- **Format:** JPG
- **Size:** Approximately 160 MB

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/majidmajeedqureshi/Detection-and-Classification-of-Brain-Tumor-from-MRI-Images-using-Hybrid-Deep-Learning
   cd brain-tumor-detection
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
