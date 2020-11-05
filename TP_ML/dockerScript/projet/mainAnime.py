import streamlit as st
import pickle
import sklearn
import joblib
import pandas as pd

joblib_file = "modelAnime.pkl"
model = joblib.load(joblib_file)

Type = st.text_input("Type :", "")
Episodes = st.text_input("Episodes :", "")
StartingSeason = st.text_input("StartingSeason :", "")
BroadcastTime = st.text_input("BroadcastTime :", "")
Sources = st.text_input("Sources :", "")
Duration = st.text_input("Duration :", "")
Rating = st.text_input("Rating :", "")
Score = st.text_input("Score :", "")
ScoredBy = st.text_input("ScoredBy :", "")
Members = st.text_input("Members :", "")
Favorites = st.text_input("Favorites :", "")
StartingDate_year = st.text_input("StartingDate_year :", "")
StartingDate_month = st.text_input("StartingDate_month :", "")
StartingDate_day = st.text_input("StartingDate_day :", "")
EndingDate_year = st.text_input("EndingDate_year :", "")
EndingDate_month = st.text_input("EndingDate_month :", "")
EndingDate_day = st.text_input("EndingDate_day :", "")




if (Type and Episodes and StartingSeason and BroadcastTime) :
    anime = pd.DataFrame({
    'Type': [float(Type)],
    'Episodes': [float(Episodes)],
    'StartingSeason': [float(StartingSeason)],
    'BroadcastTime': [float(BroadcastTime)]
    'Sources': [float(Sources)]
    'Duration': [float(Duration)]
    'Rating': [float(Rating)]
    'Score': [float(Score)]
    'ScoredBy': [float(ScoredBy)]
    'Members': [float(Members)]
    'Favorites': [float(Favorites)]
    'StartingDate_year': [float(StartingDate_year)]
    'StartingDate_month': [float(StartingDate_month)]
    'StartingDate_day': [float(StartingDate_day)]
    'EndingDate_year': [float(EndingDate_year)]
    'EndingDate_month': [float(EndingDate_month)]
    'EndingDate_day': [float(EndingDate_day)]

    })
    Y_pred = model.predict_proba(anime)[0]
    st.text("Voici le résultat : ")
    st.text(Y_pred*100)
    
    
    
else :
    st.text("Remplis tous les champs")