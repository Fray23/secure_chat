from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import usecases
from app.api import dependencies
from app.core.security import create_access_token
from app.schemas.users import UserInLoginResponse, UserInRegister, UserInLogin

router = APIRouter()


@router.post('/login', response_model=UserInLoginResponse)
async def login(user_login: UserInLogin, session: Session = Depends(dependencies.get_db)):
    user = usecases.user.authenticate(session, email=user_login.email, password=user_login.password)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email does not exists or password invalid.",
        )
    token = create_access_token(subject={'email': user.email})
    return UserInLoginResponse(email=user.email, token=token)


@router.post('/register', response_model=UserInLoginResponse)
async def register(user_register: UserInRegister, session: Session = Depends(dependencies.get_db)):
    if usecases.user.get_by_email(session, email=user_register.email):
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = usecases.user.create(session, user_register)
    token = create_access_token(subject={'email': user.email})
    return UserInLoginResponse(email=user.email, token=token)
