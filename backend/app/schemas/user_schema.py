from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    username: str
    full_name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    full_name: str
    email: EmailStr
    role: str

    model_config = ConfigDict(from_attributes=True)