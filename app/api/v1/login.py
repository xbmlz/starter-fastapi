from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.core.security import create_access_token, verify_password

router = APIRouter()


@router.post("/login")
def login(
    db: Session = Depends(deps.get_db), form: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    用户登录
    """
    user = crud.sys_user.get_by_username(db, username=form.username)
    if not user:
        return deps.result_fail()(msg="用户不存在")
    if not user.is_active:
        return deps.result_fail(msg="用户已被禁用")
    if not verify_password(form.password, user.password):
        return deps.result_fail(msg="密码错误")
    access_token = create_access_token(user.id)
    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
