import joblib
import pandas as pd
from fastapi import FastAPI

from deployedmodel.request_model import RequestModel

app = FastAPI()
model = joblib.load('churn_model.pkl')

@app.patch("/predict")
def predict_churn(request: RequestModel):
    # Convert the request data to a pandas DataFrame
    feature_columns = [
        "Contract",
        "PaymentMethod",
        "OnlineSecurity",
        "TechSupport"
    ]
    df = pd.DataFrame([request.model_dump()], columns=feature_columns)

    # Make a prediction
    prediction = model.predict(df)
    probability = model.predict_proba(df)

    return {
        "prediction": prediction[0], 
        "probability": probability[0].tolist()
    }