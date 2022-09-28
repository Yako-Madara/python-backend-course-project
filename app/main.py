from fastapi import FastAPI
from routers.posts_router import router as posts_routers
from routers.users_router import router as users_routers

app = FastAPI()

app.include_router(posts_routers, prefix="/posts", tags=["posts"])
app.include_router(users_routers, prefix="/users", tags=["users"])
