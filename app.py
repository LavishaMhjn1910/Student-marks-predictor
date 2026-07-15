import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("student_marks_model.pkl")

# Title
st.title("🎓 Student Marks Predictor")

st.write("Enter the number of study hours to predict marks.")

# Input from user
hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=1.0,
    step=0.5
)

# Prediction
if st.button("Predict Marks"):
    prediction = model.predict(np.array([[hours]]))
    st.success(f"Predicted Marks: {prediction[0]:.2f}")