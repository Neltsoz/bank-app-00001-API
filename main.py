from fastapi import FastAPI

from app.api.v1 import (
    users,
    admin,
    payments,
    auth
)


app = FastAPI()

app.include_router(users.router, prefix='/api/v1/users')
app.include_router(admin.router, prefix='/api/v1/admin')
app.include_router(payments.router, prefix='/api/v1/payments')
app.include_router(auth.router, prefix='/api/v1/auth')
