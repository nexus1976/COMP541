from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, Response, status

from deployedmodel.request_model import RequestModel
from deployedmodel.response_model import ResponseModel

app = FastAPI(
    title='Churn Prediction API',
    description='An API for predicting customer churn',
    version='1.0.0'
)
MODEL_PATH = Path(__file__).resolve().with_name('churn_model.pkl')
model = joblib.load(MODEL_PATH)

@app.get("/")
def read_root():
    return {'status': 'healthy', 'message': f'Welcome to the Churn Prediction API version {app.version}'}

@app.post('/predict', response_model=ResponseModel, status_code=status.HTTP_200_OK)
def predict_churn(request: RequestModel, response: Response):
    try:
        # Convert the request data to a pandas DataFrame
        feature_columns = [
            'Contract',
            'PaymentMethod',
            'OnlineSecurity',
            'TechSupport'
        ]
        df = pd.DataFrame([request.model_dump()], columns=feature_columns)

        # Make a prediction
        prediction = model.predict(df)
        probability = model.predict_proba(df)
        prediction_response = 'YES' if prediction[0] == 1 else 'NO'
        return ResponseModel(
            prediction=prediction_response,
            probability=probability[0].tolist()
        )
    except Exception as exc:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            'detail': f'Prediction failed: {exc}'
        }