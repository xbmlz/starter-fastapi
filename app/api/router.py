from fastapi import APIRouter

from app.api.v1 import login, users

routes = APIRouter()

routes.include_router(login.router, tags=["login"])
routes.include_router(users.router, prefix="/users", tags=["users"])
