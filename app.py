from fastapi import FastAPI
import pickle
from Model.customer_churn_pydantic_model import ChurnInput
import pandas as pd
import numpy as np
from fastapi.responses import JSONResponse

app = FastAPI(title="Customer Churn Prediction")

try:
    #load Pikle Model First
    with open("Model/customer_churn_pikle_model.pkl","rb") as f:
        model = pickle.load(f)
    
    encode = model["encoder"]
    lb = model["label_encoder"]
    std = model["standard_scaler"]
    best_model = model["final_model"]
    best_accuracy = model["model_accuracy"]
    temp_3 = model["column_name"]
    best_model_name=model["Model_name"]

except FileNotFoundError as e:
    print(f"error {e}.")
except Exception as g:
    print(f"Error {g}.")

@app.get("/")
def default():
    return {"message":"This is my customer churn prediction.",
            "Best Model":f"Our Best model for this Prediction is {best_model}.",
            f"Accuracy of {best_model}:":f"{best_accuracy}"}

@app.post("/churn_prediction")
def churn_pred(customer:ChurnInput):

    data = pd.DataFrame([{
    'gender': customer.gender,
    'SeniorCitizen':customer.SeniorCitizen,
    'Partner': customer.Partner,
    'Dependents': customer.Dependents,
    'tenure': customer.tenure,
    'PhoneService': customer.PhoneService,
    'MultipleLines': customer.MultipleLines,
    'InternetService': customer.InternetService,
    'OnlineSecurity': customer.OnlineSecurity,
    'OnlineBackup': customer.OnlineBackup,
    'DeviceProtection': customer.DeviceProtection,
    'TechSupport': customer.TechSupport,
    'StreamingTV': customer.StreamingTV,
    'StreamingMovies': customer.StreamingMovies,
    'Contract': customer.Contract,
    'PaperlessBilling': customer.PaperlessBilling,
    'PaymentMethod': customer.PaymentMethod,
    'MonthlyCharges': customer.MonthlyCharges,
    'TotalCharges':customer.TotalCharges
    }])

    #Lets encode the Categorical columns.
    for i in temp_3:
        data[i] = encode[i].transform(data[i])
    
    #Lets scal down all the data.
    data = std.transform(data)

    prediction = best_model.predict(data)

    ans = "Customer will NOT churn" if prediction[0] == 0 else "Customer WILL churn"

    return JSONResponse(status_code=200,content={
        "Predicted Answer":f"{ans}",
        "Model_Name":best_model_name,
        "Accuracy of Model":best_accuracy,
    })