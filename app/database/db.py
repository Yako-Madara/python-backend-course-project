from typing import Dict

from models.post import Post
from models.user import User


class Database:
    users: Dict[int, User] = {}
    posts: Dict[int, Post] = {}


db = Database()
