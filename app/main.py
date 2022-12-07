from fastapi import FastAPI

from app.api.router import routes
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    openapi_url=f"{settings.SERVER_CONTEXT_PATH}/openapi.json",
)

app.include_router(routes, prefix=settings.SERVER_CONTEXT_PATH)
