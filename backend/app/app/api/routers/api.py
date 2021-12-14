from fastapi import APIRouter
from app.api.routers import auth

router = APIRouter()
router.include_router(auth.router,  prefix='/users')
