from typing import Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    id: Optional[int] = None
    nickname: str
    password: str
    nick: Optional[str] = None


class UserInLogin(BaseModel):
    nickname: str
    password: str


class UserInRegister(BaseModel):
    nickname: str
    password: str


class UserInLoginResponse(BaseModel):
    token: str
    nickname: str

    class Config:
        orm_mode = True
