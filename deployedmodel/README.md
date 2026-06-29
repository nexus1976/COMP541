# COMP541 Deployed Model

This is a FastAPI web service that takes the model that was produced by Group 2 and allow it to be deployed in such a way that predictions can be tested.

## Running locally
If you want to debug this service locally, ensure you have Python environment and at the base of the `deployedmodel` folder run the following command: `pip install -r requirement.txt`

## Testing Endpoint
This service has a single endpoint that is the following:
`POST /predict`

This endpoint needs a payload that's structured in the following manner:
```
{
  "Contract": "Month-to-month",
  "PaymentMethod": "Electronic check",
  "OnlineSecurity": "No",
  "TechSupport": "No"
}
```

For the `Contract` property, the following values are valid: `Month-to-month`, `Two year`, `One year`
For the `PaymentMethod` property, the following values are valid: `Electronic check`, `Mailed check`, `Bank transfer (automatic)`, `Credit card (automatic)`
For the `OnlineSecurity` property, the following values are valid: `Yes`, `No`
For the `TechSupport` property, the following values are valid: `Yes`, `No`