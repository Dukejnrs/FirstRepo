import streamlit as st 
import pandas as pd 
import numpy as np 
import joblib

#Load the trained model

model = joblib.load("models/life_expectancy_rf_model.pkl")

#Define the app title

st.title("🌍 Life Expectancy Predictor") 
st.markdown(""" This app predicts Life Expectancy based on health, economic, and demographic indicators.

Upload your input or manually enter values to get predictions. """)

#Input form

with st.form("prediction_form"): 
    st.subheader("Enter the input values:")

    schooling = st.number_input("Schooling (years)", min_value=0.0, max_value=20.0, value=12.0)
    income_comp = st.slider("Income Composition of Resources", 0.0, 1.0, 0.7)
    bmi = st.number_input("BMI", min_value=0.0, max_value=60.0, value=22.0)
    diphtheria = st.slider("Diphtheria Immunization (%)", 0, 100, 85)
    polio = st.slider("Polio Immunization (%)", 0, 100, 90)
    adult_mortality = st.number_input("Adult Mortality Rate", min_value=0.0, max_value=1000.0, value=150.0)
    hiv_aids = st.number_input("HIV/AIDS (% of population)", min_value=0.0, max_value=20.0, value=0.5)
    thinness_1_19 = st.number_input("Thinness 1-19 years (%)", min_value=0.0, max_value=50.0, value=5.0)
    thinness_5_9 = st.number_input("Thinness 5-9 years (%)", min_value=0.0, max_value=50.0, value=4.0)
    status = st.selectbox("Development Status", ["Developing", "Developed"])

    submitted = st.form_submit_button("Predict")

    if submitted:
        input_data = pd.DataFrame({
            "Schooling": [schooling],
            "Income composition of resources": [income_comp],
            "BMI": [bmi],
            "Diphtheria": [diphtheria],
            "Polio": [polio],
            "Adult Mortality": [adult_mortality],
            "HIV/AIDS": [hiv_aids],
            "thinness 1-19 years": [thinness_1_19],
            "thinness 5-9 years": [thinness_5_9],
            "Status_Developing": [1 if status == "Developing" else 0]
    })

    prediction = model.predict(input_data)
    st.success(f"Predicted Life Expectancy: {prediction[0]:.2f} years")

#Footer

st.markdown("""

App created by Duke Jnrs
Data from WHO & UN Health Statistics """)

