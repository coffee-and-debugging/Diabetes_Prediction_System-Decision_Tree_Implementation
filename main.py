import streamlit as st
import numpy
import pickle
import pandas as pd

with open('diabetes_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)

feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
def predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, pedigree, age):
    features = pd.DataFrame(
        [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, pedigree, age]],
        columns=feature_names
    )
    array_value= features.to_numpy()
    prediction = model.predict(array_value)
    return prediction[0]

st.title("Diabetes Prediction App")
st.write("Use this app to predict whether you have diabetes based on your input data.")
st.image("images/diabetes.png", width=700)

pregnancies = st.number_input("Pregnancies (max: 17)", min_value=0, max_value=17, value=0)
glucose = st.number_input("Glucose (max: 250)", min_value=0, max_value=250, value=0)
blood_pressure = st.number_input("Blood Pressure (max: 150)", min_value=0, max_value=150, value=0)
skin_thickness = st.number_input("Skin Thickness (max: 100)", min_value=0, max_value=100, value=0)
insulin = st.number_input("Insulin (max: 900)", min_value=0, max_value=900, value=0)
bmi = st.number_input("Body Mass Index (BMI) (max: 70)", min_value=0, max_value=70, value=0)
pedigree = st.number_input("Pedigree (max: 3)", min_value=0.0, max_value=3.0, value=0.0)
age = st.number_input("Age (max: 100)", min_value=0, max_value=100, value=0)

if st.button('Predict'):
    try:
        result = predict_diabetes(
            float(pregnancies),
            float(glucose),
            float(blood_pressure),
            float(skin_thickness),
            float(insulin),
            float(bmi),
            float(pedigree),
            float(age)
        )
        if result == 0:
            st.success("Congratulation, you are free from **Diabetes** :)")
        else:
            st.success("Sorry but you may have **Diabetes** :(")
    except ValueError as e:
        st.error(f'Error: {e}')
