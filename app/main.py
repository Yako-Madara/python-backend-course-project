from fastapi import FastAPI
from routers import router

api = FastAPI()

api.include_router(router)
