import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model1.pkl")

st.title("🏦 Loan Prediction App")
st.write("Enter the applicant details below to predict if the loan will be approved or not.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
applicant_income = st.number_input("Applicant Income", min_value=0, value=5000)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0.0, value=0.0)
loan_amount = st.number_input("Loan Amount", min_value=0.0, value=150.0)
loan_amount_term = st.number_input("Loan Amount Term", min_value=0.0, value=360.0)
credit_history = st.selectbox("Credit History", ["0", "1"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])


# Function to encode input features
def encode_features(gender, married, dependents, education, self_employed, credit_history, property_area):
    gender_encoded = 1 if gender == "Male" else 0
    married_encoded = 1 if married == "Yes" else 0
    dependents_encoded = 3 if dependents == "3+" else int(dependents)
    education_encoded = 0 if education == "Graduate" else 1
    self_employed_encoded = 1 if self_employed == "Yes" else 0
    credit_history_encoded = int(credit_history)
    property_area_mapping = {"Urban": 2, "Semiurban": 1, "Rural": 0}
    property_area_encoded = property_area_mapping[property_area]

    return [gender_encoded, married_encoded, dependents_encoded, education_encoded,
            self_employed_encoded, applicant_income, coapplicant_income, loan_amount,
            loan_amount_term, credit_history_encoded, property_area_encoded]
