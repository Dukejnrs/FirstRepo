import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("life_expectancy_rf_model.pkl")

# App title and intro
st.title("🌍 Life Expectancy Predictor")
st.write(
    """
    Predict the life expectancy of a country based on key health, economic, and demographic indicators.
    """
)

# Sidebar inputs
st.sidebar.header("Input Features")

schooling = st.sidebar.slider("Average Schooling Years", 0.0, 20.0, 12.0)
income_comp = st.sidebar.slider("Income Composition of Resources (0-1)", 0.0, 1.0, 0.65)
bmi = st.sidebar.slider("BMI", 10.0, 50.0, 25.0)
diphtheria = st.sidebar.slider("Diphtheria Immunization (%)", 0.0, 100.0, 85.0)
polio = st.sidebar.slider("Polio Immunization (%)", 0.0, 100.0, 85.0)
adult_mortality = st.sidebar.slider("Adult Mortality", 0, 600, 150)
hiv_aids = st.sidebar.slider("HIV/AIDS Prevalence", 0.0, 30.0, 0.5)
thinness_1_19 = st.sidebar.slider("Thinness (10-19 years)", 0.0, 25.0, 3.0)
thinness_5_9 = st.sidebar.slider("Thinness (5-9 years)", 0.0, 25.0, 3.0)
status = st.sidebar.selectbox("Country Status", ["Developed", "Developing"])

# Convert status to one-hot encoded form
status_developing = 1 if status == "Developing" else 0

# Manually set feature names to match training
input_data = pd.DataFrame([[
    schooling,
    income_comp,
    bmi,
    diphtheria,
    polio,
    adult_mortality,
    hiv_aids,
    thinness_1_19,
    thinness_5_9,
    status_developing
]], columns=[
    "Schooling",
    "Income composition of resources",
    "BMI",
    "Diphtheria",
    "Polio",
    "Adult Mortality",
    "HIV/AIDS",
    "Thinness 1-19 years",
    "Thinness 5-9 years",
    "Status_Developing"
])

# Predict
if st.button("Predict Life Expectancy"):
    prediction = model.predict(input_data)
    st.success(f"✅ Predicted Life Expectancy: {prediction[0]:.2f} years")
