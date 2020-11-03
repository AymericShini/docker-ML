#Demange Aymeric
#Afin de lancer ce code il faut run la commande : python3 mainIris.py

import pandas as pd
import uvicorn
import sklearn
import joblib
from fastapi import FastAPI

app = FastAPI()
model = joblib.load("modelIris.pkl")


#if you go to http://localhost:8000 the message hello world should appear
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Using Post method
@app.get('/predict/{sepal_length}/{sepal_width}/{petal_length}/{petal_width}')
async def predict(sepal_length,sepal_width,petal_length,petal_width):
    irisX = pd.DataFrame({
    'sepal_length': [float(sepal_length)],
    'sepal_width': [float(sepal_width)],
    'petal_length': [float(petal_length)],
    'petal_width': [float(petal_width)]
    })
    Y_pred = model.predict_proba(irisX)[0]
    
    infoAlgorithm = "The algorithm found that the origin's name is"
    infoPrediction = "The prediction in % is "

    if Y_pred[0] > Y_pred[1] and Y_pred[0]> Y_pred[2]:
        return {infoAlgorithm :'setosa', infoPrediction:Y_pred[0]*100}
    elif Y_pred[1] > Y_pred[0] and Y_pred[1]> Y_pred[2] :
        return {infoAlgorithm:'versicolor', infoPrediction:Y_pred[1]*100}
    else :
        return {infoAlgorithm:'virginica', infoPrediction:Y_pred[2]*100}
        
if __name__ == '__main__' :
    uvicorn.run(app,host="127.0.0.1",port="8000")