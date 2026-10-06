import streamlit as st
import pandas as pd
import joblib

# Carregar o modelo
model = joblib.load("fraud_detection_model.pkl")

st.title("Fraud Detection Model")

st.markdown(
    "This app uses a pre-trained machine learning model to predict "
    "whether a transaction is fraudulent or not based on the input features."
)

st.divider()

transaction_type = st.selectbox(
    "Transaction Type",
    ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"]
)

amount = st.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=1000.0
)

oldbalanceOrg = st.number_input(
    "Old Balance of Origin Account",
    min_value=0.0,
    value=10000.0
)

newbalanceOrig = st.number_input(
    "New Balance of Origin Account",
    min_value=0.0,
    value=9000.0
)

oldbalanceDest = st.number_input(
    "Old Balance of Destination Account",
    min_value=0.0,
    value=5000.0
)

newbalanceDest = st.number_input(
    "New Balance of Destination Account",
    min_value=0.0,
    value=6000.0
)

if st.button("Predict"):

    # Criar os dados usando os valores digitados pelo usuário
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    # Criar as mesmas variáveis usadas no treinamento
    input_data["balanceDiffOrig"] = (
        input_data["oldbalanceOrg"] - input_data["newbalanceOrig"]
    )

    input_data["balanceDiffDest"] = (
        input_data["newbalanceDest"] - input_data["oldbalanceDest"]
    )

    # Fazer a previsão
    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: {prediction}")

    if prediction == 1:
        st.error("The transaction is predicted to be fraudulent.")
    else:
        st.success("The transaction is predicted to be legitimate.")
