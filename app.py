import streamlit as st
import pandas as pd
import joblib

model = joblib.load('fraud_model.pkl')

st.title("Fraud detection project V1.0")
st.write("Enter transaction details to check for fraud risk !")
col1, col2 = st.columns(2)
with col1:
    amount = st.number_input("transaction amount in $", min_value=0.0)
    old_balance = st.number_input("Sender old balance in $", min_value=0.0)
    new_balance = st.number_input("Receiver new balanace in $", min_value=0.0)

with col2:
    transaction_type= st.selectbox("Transaction type", ["TRANSFER", "CASH_OUT", "PAYMENT", "CASH_IN", "DEBIT"])
    step= st.number_input("Hour of day", min_value=0, max_value=744)

if st.button("Analyze transaction"):
    if(new_balance==0 and old_balance>0):
        is_emptied=1
    else:
        is_emptied=0    
    input_data = pd.DataFrame({
        'step': [step],
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [old_balance],
        'newbalanceOrig': [new_balance],
        'oldbalanceDest': [0], 
        'newbalanceDest': [0],
        'is_emptied': [is_emptied]
    })
    prob = model.predict_proba(input_data)[0, 1]
    
    if prob > 0.99:
        st.error(f"HIGH RISK: {prob*100:.2f}% Probability of Fraud")
    else:
        st.success(f"Low Risk: {prob*100:.2f}% Probability of Fraud")