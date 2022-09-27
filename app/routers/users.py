from typing import List

from fastapi import APIRouter, HTTPException, status
from app.models.user import User, UserCreate

from app.database.db import db

router = APIRouter()


@router.get("/")
async def all() -> List[User]:
    """Return list of all users.

    Returns:
        List[User]: list of all users
    """
    return list(db.users.values())


@router.get("/{id}")
async def get(id: int) -> User:
    """Return user by requested id.

    Args:
        id (int): user id

    Raises:
        HTTPException: accessing a non-existent user

    Returns:
        User: user by requested id
    """
    try:
        return db.users[id]
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(user_create: UserCreate) -> User:
    """Creates a new user.

    Args:
        user_create (UserCreate): form a new user

    Returns:
        User: a new user
    """
    new_id = max(db.users.keys() or (0,)) + 1
    user = User(id=new_id, **user_create.dict())
    db.users[new_id] = user
    return user


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int) -> None:
    """Deleting a user.

    Args:
        id (int): user id

    Raises:
        HTTPException: deleting a non-existing user
    """
    try:
        db.users.pop(id)
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
