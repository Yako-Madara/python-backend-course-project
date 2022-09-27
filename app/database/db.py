from typing import Dict

from app.models.user import User
from app.models.post import Post


class Database:
    users: Dict[int, User] = {}
    posts: Dict[int, Post] = {}


db = Database()
