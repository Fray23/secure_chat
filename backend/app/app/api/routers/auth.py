from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api import dependencies
from app.core.security import create_access_token
from app.schemas.users import UserInLoginResponse, UserInRegister

router = APIRouter()


@router.post('/register', response_model=UserInLoginResponse)
async def register(user_register: UserInRegister, session: Session = Depends(dependencies.get_db)):
    if crud.user.get_by_email(session, email=user_register.email):
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = crud.user.create(session, user_register)
    token = create_access_token(subject={'email': user.email})
    return UserInLoginResponse(email=user.email, token=token)
