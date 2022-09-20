from fastapi import FastAPI
from app.routers import router

api = FastAPI()

api.include_router(router)
