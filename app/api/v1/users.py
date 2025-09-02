from fastapi import APIRouter
from app.schemas.user import CreateUser
from app.repositories import user_repo


router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/")
async def create_user(user: CreateUser):
    return user_repo.create_user(user_in=user)
