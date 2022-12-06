from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api import deps

router = APIRouter()


@router.post("/login")
def login(
    db: Session = Depends(deps.get_db()), form: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    用户登录
    """

    return {"message": "login"}
