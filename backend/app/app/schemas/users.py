from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    id: Optional[int] = None
    email: EmailStr
    password: str
    nick: Optional[str] = None


class UserInLogin(BaseModel):
    email: EmailStr
    password: str


class UserInRegister(BaseModel):
    email: EmailStr
    password: str


class UserInLoginResponse(BaseModel):
    token: str
    email: EmailStr

    class Config:
        orm_mode = True
