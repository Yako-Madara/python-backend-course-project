from fastapi import APIRouter, status
from models.user import User, UserCreate
from users.user_logic import create_user, delete_user, get_all, get_user

router = APIRouter()


@router.get("/")
async def all():
    return get_all()


@router.get("/{id}")
async def get(id: int):
    return get_user(id)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(user_create: UserCreate) -> User:
    return create_user(user_create)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int) -> None:
    delete_user(id)
