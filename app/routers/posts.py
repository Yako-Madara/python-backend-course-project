from typing import List

from database.db import db
from fastapi import APIRouter, HTTPException, status
from models.post import Post, PostCreate

router = APIRouter()


@router.get("/")
async def all() -> List[Post]:
    """Return list of all posts.

    Returns:
        List[Post]: list of all posts
    """
    return list(db.posts.values())


@router.get("/{id}")
async def get(id: int) -> Post:
    """Return post by requested id.

    Args:
        id (int): post id

    Raises:
        HTTPException: accessing a non-existent post

    Returns:
        Post: post by requested id
    """
    try:
        return db.posts[id]
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(post_create: PostCreate) -> Post:
    """Create a new post.

    Args:
        post_create (PostCreate): form a new post

    Raises:
        HTTPException: creating a post from a non-existent user

    Returns:
        Post: a new post
    """
    try:
        db.users[post_create.user]
    except KeyError:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail=f"User with id {post_create.user} doesn't exist.",
        )

    new_id = max(db.posts.keys() or (0,)) + 1
    post = Post(id=new_id, **post_create.dict())
    db.posts[new_id] = post
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int) -> None:
    """Deleting a post.

    Args:
        id (int): post id

    Raises:
        HTTPException: deleting a non-existent post
    """
    try:
        db.posts.pop(id)
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
