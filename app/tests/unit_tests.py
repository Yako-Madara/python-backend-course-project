import pytest
from fastapi import HTTPException, status
from pydantic.error_wrappers import ValidationError

from app.database.db import db
from app.models.post import Post, PostCreate
from app.models.user import User, UserCreate
from app.posts.post_logic import create_post, delete_post, get_all_posts, get_post
from app.users.user_logic import create_user, delete_user, get_all_users, get_user


@pytest.fixture(autouse=True)
def fill_db():
    db.users = {
        1: User(id=1, email="user1@example.com"),
        2: User(id=2, email="user2@example.com"),
        3: User(id=3, email="user3@example.com"),
    }
    db.posts = {
        1: Post(id=1, user=1, title="Post 1"),
        2: Post(id=2, user=2, title="Post 2"),
        3: Post(id=3, user=3, title="Post 3"),
    }


def test_get_all_posts():
    assert len(get_all_posts()) == 3


def test_get_post_correct():
    assert len(get_post(1).dict()) == 3
    assert get_post(2) == {"id": 2, "user": 2, "title": "Post 2"}


def test_get_post_uncorrect():
    with pytest.raises(HTTPException) as exc_info:
        get_post(0)
    assert isinstance(exc_info.value, HTTPException)
    assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND


def test_create_post_valid():
    post = PostCreate(user=2, title="New Post")
    new_post = create_post(post)
    assert new_post.dict() == {"id": 4, "user": 2, "title": "New Post"}
    assert 4 in db.posts


def test_create_post_invalid():
    with pytest.raises(ValidationError) as exc_info:
        PostCreate(title="New Post")
    assert isinstance(exc_info.value, ValidationError)


def test_create_post_non_existing_user():
    post = PostCreate(user=5, title="New Post")
    with pytest.raises(HTTPException) as exc_info:
        create_post(post)
    assert isinstance(exc_info.value, HTTPException)
    assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
    assert exc_info.value.detail == "User with id 5 doesn't exist."


def test_delete_post_found():
    delete_post(1)
    assert 1 not in db.posts


def test_delete_post_not_found():
    with pytest.raises(HTTPException) as exc_info:
        delete_post(10)
    assert isinstance(exc_info.value, HTTPException)
    assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_all_users():
    assert len(get_all_users()) == 3


def test_get_user_valid():
    assert len(get_user(1).dict()) == 2
    assert get_user(1) == {"id": 1, "email": "user1@example.com"}


def test_get_user_invalid():
    with pytest.raises(HTTPException) as exc_info:
        get_user(4)
    assert isinstance(exc_info.value, HTTPException)
    assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND


def test_create_user_valid():
    new_user = UserCreate(email="user4@example.com")
    user = create_user(new_user)
    assert user.dict() == {"id": 4, "email": "user4@example.com"}
    assert 4 in db.users


def test_create_user_invalid():
    with pytest.raises(ValidationError) as exc_info:
        UserCreate(foo="bar")
    assert isinstance(exc_info.value, ValidationError)


def test_delete_user_found():
    delete_user(3)
    assert 3 not in db.users


def test_delete_user_not_found():
    with pytest.raises(HTTPException) as exc_info:
        delete_user(0)
    assert isinstance(exc_info.value, HTTPException)
    assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND
