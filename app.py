import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("diabetes_model.sav",'rb'))

# streamlit UI
st.title("Diabetes Prediction App")
st.image("Diabetes.png",caption="Diabetes Prediction",use_column_width=True)
st.markdown("Enter the details below to check the risk of Prediction")

# Input details
Pregnancies = st.number_input("Pregnancies",min_value= 0,max_value=20)
Glucose = st.text_input("Glucose")
BloodPressure = st.text_input("BloodPressure")
SkinThickness = st.text_input("SkinThickness")
Insulin = st.text_input("Insulin")
BMI = st.text_input("BMI")
DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
Age = st.text_input("Age")

# Predict button
if st.button("Predict"):
    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display result
    if prediction == 1:
        st.error("High Risk of Diabetes")
    else:
        st.success("Low Risk of Heart Disease!")