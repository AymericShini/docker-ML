import streamlit as st
import pickle
import sklearn
import joblib

joblib_file = "model.pkl"
model = joblib.load(joblib_file)

user_input = st.text_input("Enter text :", "")

if (user_input) :
    Y_pred = model.predict_proba([user_input])[0]
    response = {
    			"The algorithm predicted the next amount of % of hate speech": Y_pred[0]*100,
    			"Offensive": Y_pred[1]*100,
    			"neither": Y_pred[2]*100
    			}
    st.text("Voici le résultat : ")
    st.text(response)

    if Y_pred[0] > Y_pred[1] and Y_pred[0]> Y_pred[2]:
        st.text("hate_speech")
    elif Y_pred[1] > Y_pred[0] and Y_pred[1]> Y_pred[2] :
        st.text("offensive_language")
    else :
        st.text("neither")

