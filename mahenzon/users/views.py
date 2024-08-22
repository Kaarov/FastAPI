from fastapi import APIRouter
from .schemas import CreateUser
from users import crud


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user)
