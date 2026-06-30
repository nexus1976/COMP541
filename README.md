# COMP541 Group 2
## Data Mining Group Project

### Team Members
Cedric Tong
Daniel Graham
Justin Gourneau
Tyler Barton
Yashin Rodriguez

### Artifacts
Our dataset is located in this repo at `WA_Fn-UseC_-Telco-Customer-Churn.csv` and the Jupyter notebook that processes this dataset and trains our selected model is located in this repo at `Group2Project.ipynb`.

### Deployment
The deployed microservice that serves up this model is located in the subfolder of this repo under `/deployedmodel`. You can either debug this FastAPI project directly, or at the root of this repo you can issues the following command (requires Docker):

`docker compose up -d`

### Testing
If you're running the deployed container, you can issue the following cURL to test:
```
curl --location 'http://localhost:8000/predict' \
--header 'Content-Type: application/json' \
--data '{
  "Contract": "Month-to-month",
  "PaymentMethod": "Mailed check",
  "OnlineSecurity": "No",
  "TechSupport": "No"
}'
```

The debugging project runs the same, but on port `8003`.

We've also deployed the model to a microservice running on Azure.
```
curl --location 'http://comp541-churn-api-aci.eastus.azurecontainer.io:8000/predict' \
--header 'Content-Type: application/json' \
--data '{
  "Contract": "One year",
  "PaymentMethod": "Credit card (automatic)",
  "OnlineSecurity": "No",
  "TechSupport": "No"
}'
```