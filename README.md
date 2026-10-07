Fraud Detection Using Machine Learning

This project uses Machine Learning to detect potentially fraudulent financial transactions.

The project was developed using Python and includes data analysis, feature engineering, model training and a Streamlit application for making predictions.

About the Project

The goal of this project is to train a Machine Learning model that can classify financial transactions as fraudulent or legitimate.

The model uses information such as:

Transaction type
Transaction amount
Origin account balance
Destination account balance

Dataset

The dataset contains financial transaction records with information about transactions and account balances.

Some of the main columns used in the project are:

type
amount
oldbalanceOrg
newbalanceOrig
oldbalanceDest
newbalanceDest
isFraud

The isFraud column is the target used to identify fraudulent transactions.

Feature Engineering

Two new features were created during the data preparation:

balanceDiffOrig: difference between the origin account balance before and after the transaction
balanceDiffDest: difference between the destination account balance after and before the transaction

These features are also calculated in the Streamlit application before making a prediction.

Model

After preparing the data, a Machine Learning model was trained and saved as fraud_detection_model.pkl.

The application loads this model and uses it to make predictions on new transactions.

Results

The model achieved approximately 94% accuracy during the evaluation.

Accuracy was used as one of the evaluation metrics. Other metrics such as precision, recall and F1-score can also be useful when evaluating a fraud detection model.

Streamlit Application

The project includes a Streamlit application where the user can enter information about a transaction.

The application asks for:

Transaction type
Transaction amount
Origin account balance before the transaction
Origin account balance after the transaction
Destination account balance before the transaction
Destination account balance after the transaction

After entering the information, the application uses the trained model to predict whether the transaction is fraudulent or legitimate.

How to Run

First, install the required libraries:

pip install -r requirements.txt

Then run the Streamlit application:

streamlit run fraud_detection.py

The Jupyter Notebook used during the project is also included in the repository.

Possible Improvements

Some things that could be improved in the future:

Test other Machine Learning models
Tune the model parameters
Add more evaluation metrics
Improve the Streamlit interface
Deploy the application online
