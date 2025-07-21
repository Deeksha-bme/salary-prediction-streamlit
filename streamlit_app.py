
import streamlit as st
import joblib

# Load the model
model = joblib.load("salary_model.pkl")

st.title("Employee Salary Prediction")

age = st.number_input("Age", min_value=18, max_value=100)
education = st.selectbox("Education Level", ['Bachelors', 'Masters', 'PhD'])
experience = st.slider("Years of Experience", 0, 40, 1)
gender = st.selectbox("Gender", ['Male', 'Female'])

if st.button("Predict Salary"):
    # Replace with your model input order
    input_data = [[age, experience, 1 if gender == 'Male' else 0, 0]]  
    prediction = model.predict(input_data)
    st.success(f"Predicted Salary: ₹{prediction[0]:,.2f}")
