from pydantic import BaseModel, Field


class RequestModel(BaseModel):
    """Pydantic model for FastAPI request payloads."""
    Contract: str = Field(..., min_length=1, max_length=5000, description="Contract type")
    PaymentMethod: str = Field(..., min_length=1, max_length=5000, description="Payment method")
    OnlineSecurity: str = Field(..., min_length=1, max_length=5000, description="Yes/No")
    TechSupport: str = Field(..., min_length=1, max_length=5000, description="Yes/No")

