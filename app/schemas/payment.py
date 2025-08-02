from pydantic import BaseModel
from uuid import UUID


class WebhookPayload(BaseModel):
    transaction_id: UUID
    account_id: int
    user_id: int
    amount: float
    signature: str


class PaymentResponse(BaseModel):
    transaction_id: UUID
    account_id: int
    user_id: int
    amount: float

    class Config:
        from_attributes = True
