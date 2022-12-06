from typing import Generator

from app.db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
    finally:
        db.close()


def rsp_success(data=None, msg="success"):
    return {"code": 0, "msg": msg, "data": data}


def rsp_error(msg="error", code=1):
    return {"code": code, "msg": msg, "data": None}
