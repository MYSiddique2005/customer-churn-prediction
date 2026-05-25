import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('models/churn_model.pkl')

st.title("Customer Churn Prediction App")

st.write("Enter customer details to predict churn.")

# User Inputs
tenure = st.slider("Tenure (Months)", 0, 72, 12)

MonthlyCharges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    max_value=200.0,
    value=70.0
)

TotalCharges = st.number_input(
    "Total Charges",
    min_value=0.0,
    max_value=10000.0,
    value=1000.0
)

Contract_Two_year = st.selectbox(
    "Two Year Contract?",
    [0, 1]
)

InternetService_Fiber_optic = st.selectbox(
    "Fiber Optic Internet?",
    [0, 1]
)

PaymentMethod_Electronic_check = st.selectbox(
    "Electronic Check Payment?",
    [0, 1]
)

# Create input dataframe
input_data = pd.DataFrame({
    'tenure': [tenure],
    'MonthlyCharges': [MonthlyCharges],
    'TotalCharges': [TotalCharges],
    'Contract_Two year': [Contract_Two_year],
    'InternetService_Fiber optic': [InternetService_Fiber_optic],
    'PaymentMethod_Electronic check': [PaymentMethod_Electronic_check]
})

# Fill missing columns
model_features = model.feature_names_in_

for col in model_features:
    if col not in input_data.columns:
        input_data[col] = 0

input_data = input_data[model_features]

# Prediction
if st.button("Predict Churn"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer is likely to churn.")
    else:
        st.success("Customer is likely to stay.")