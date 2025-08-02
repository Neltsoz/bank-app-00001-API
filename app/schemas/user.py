from pydantic import BaseModel


class UserCreate(BaseModel):
    id: int
    email: str
    password: str
    full_name: str
    is_admin: bool


class UserResponse(BaseModel):
    id: int
    email: str
    hashed_password: str
    full_name: str
    is_admin: bool

    class Config:
        from_attributes = True
