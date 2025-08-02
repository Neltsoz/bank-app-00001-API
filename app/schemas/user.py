from pydantic import BaseModel


class UserCreate(BaseModel):
    id: int
    email: str
    password: str
    full_name: str
    is_admin: bool
