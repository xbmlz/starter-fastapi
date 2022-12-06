from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db import base  # noqa: F401


def init_db(db: Session) -> None:
    user = crud.sys_user.get_by_username(db, username="root")
    if not user:
        user_in = schemas.SysUserCreate(
            username=settings.SUPERUSER_USERNAME,
            password=settings.SUPERUSER_PASSWORD,
            is_superuser=True,
        )
    user = crud.sys_user.create(db, obj_in=user_in)  # noqa: F841
