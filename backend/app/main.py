from fastapi import FastAPI, Request
from typing import List
from pydantic import BaseModel
import joblib
import numpy as np
import os
from fastapi.middleware.cors import CORSMiddleware

# Define the request schema
class Transaction(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount_scaled: float

# Path to the trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../../model/models/best_model.pkl')

# Load the model at startup
model = joblib.load(MODEL_PATH)

app = FastAPI(title="Fraud Detection API")
predictions = []

class Prediction(BaseModel):
    transaction_id: int
    prediction: int
    probability: float

@app.post("/predict")
def predict(transaction: Transaction):
    # Convert input to numpy array for prediction
    input_data = np.array([list(transaction.dict().values())])
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1] if hasattr(model, 'predict_proba') else None
    return {
        "prediction": int(prediction),
        "fraud_probability": float(proba) if proba is not None else None
    }

@app.post("/predictions")
def add_prediction(prediction: Prediction):
    predictions.append(prediction)
    return {"status": "success"}

@app.get("/predictions", response_model=List[Prediction])
def get_predictions():
    return predictions[-100:]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 