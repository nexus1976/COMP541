from pydantic import BaseModel, Field

class ResponseModel(BaseModel):
    """Pydantic model for FastAPI response payloads."""
    prediction: str = Field(..., description='Churn prediction')
    probability: list = Field(..., description='Churn probability')
