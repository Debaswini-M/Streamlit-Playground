import pandas as pd
import streamlit as st
import os
st.write("Current working directory:", os.getcwd())
st.write("Files here:", os.listdir())
import joblib


st.set_page_config(page_title="Credit Risk Model",layout="wide")
st.title("Credit Default Prediction System")
model = joblib.load('credit_model_pipeline.pkl')

st.subheader("Customer Financial Details")

Age = st.number_input("Age",min_value=18,max_value=100,step=1,value=18)
Sex = st.radio("Sex",["male","female"])
Job = st.selectbox("Job Level(0-3)",[0,1,2,3])
Housing = st.selectbox("Housing",['own','rent','free'])
Saving_accounts = st.selectbox("Saving Accounts",['little', 'quite rich', 'rich', 'moderate'])
Checking_account = st.selectbox("Checkin Account",['little', 'moderate' ,'rich'])
Credit_amount = st.number_input("Credit Amount",min_value=1000,max_value=20000,step=1,value=1000)
Duration = st.number_input("Duration(months)",min_value=5,max_value=80,step=1,value=10)
Purpose = st.selectbox("Purpose:",['radio/TV','education','furniture/equipment','car','business','domestic appliances','repairs','vacation/others'])

if st.button("Predict Credit Risk:"):
    input_data = pd.DataFrame([{
        'Age':Age,
        'Sex':Sex,
        'Job':Job,
        'Housing':Housing,
        'Saving accounts':Saving_accounts,
        'Checking account':Checking_account,
        'Credit amount':Credit_amount,
        'Duration':Duration,
        'Purpose':Purpose,

    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if probability > 0.5:
        st.error(f"⚠️ High Risk {probability*100:.2f}%")

    elif probability == 0.5:
        st.write(f"🔶 Moderate Risk {probability*100:.2f}%")

    else:
        st.success(f"✅Low Risk {probability * 100:.2f}%")
    st.progress(int(probability*100))
