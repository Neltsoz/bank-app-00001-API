from hashlib import sha256

from app.config import SECRET_KEY
from app.schemas.payment import WebhookPayload


def verify_webhook_signature(webhook_data: WebhookPayload) -> bool:
    transaction_id = webhook_data.transaction_id
    account_id = webhook_data.account_id
    user_id = webhook_data.user_id
    amount = webhook_data.amount
    signature = webhook_data.signature

    if amount - int(amount) == 0:
        amount = int(amount)

    string = f"{account_id}{amount}{transaction_id}{user_id}{SECRET_KEY}"
    print(string)
    print(sha256(string.encode()).hexdigest())
    return signature == sha256(string.encode()).hexdigest()
