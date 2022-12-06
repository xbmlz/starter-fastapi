from fastapi import APIRouter

from app.api.v1.endpoints import sys_login

routes = APIRouter()

routes.include_router(sys_login.router, tags=["login"])
