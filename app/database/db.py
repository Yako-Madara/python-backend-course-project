from typing import Dict

from app.models.post import Post
from app.models.user import User


class Database:
    users: Dict[int, User] = {}
    posts: Dict[int, Post] = {}


db = Database()
