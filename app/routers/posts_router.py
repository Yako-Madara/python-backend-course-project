from fastapi import APIRouter, status
from models.post import PostCreate
from posts.post_logic import create_post, delete_post, get_all_posts, get_post

router = APIRouter()


@router.get("/")
async def all():
    return get_all_posts()


@router.get("/{id}")
async def get(id: int):
    return get_post(id)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(post_create: PostCreate):
    return create_post(post_create)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int):
    delete_post(id)
