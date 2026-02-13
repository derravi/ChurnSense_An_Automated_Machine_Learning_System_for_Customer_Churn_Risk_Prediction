from fastapi import FastAPI
import pickle
from Model.customer_churn_pydantic_model import ChurnInput
import pandas as pd
import numpy as np


app = FastAPI(title="Customer Churn Prediction")

#load Pikle Model First
with open("Model/customer_churn_pikle_model.pkl","rb") as f:
    model = pickle.load(f)
    
    encode = model["encoder"]
    lb = model["label_encoder"]
    std = model["standard_scaler"]
    best_model = model["final_model"]
    best_accuracy = model["model_accuracy"]
    temp_3 = model["column_name"]

@app.get("/")
def default():
    return {"message":"This is my customer churn prediction.",
            "Best Model":f"Our Best model for this Prediction is {best_model}.",
            f"Accuracy of {best_model}:":f"{best_accuracy}"}

