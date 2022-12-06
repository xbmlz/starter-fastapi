from typing import Optional

from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.crud.base import CRUDBase
from app.models.sys_user import SysUser
from app.schemas.sys_user import SysUserCreate, SysUserUpdate


class CRUDSysUser(CRUDBase[SysUser, SysUserCreate, SysUserUpdate]):
    def get_by_username(self, db: Session, *, username: str) -> Optional[SysUser]:
        return db.query(SysUser).filter(SysUser.username == username).first()

    def create(self, db: Session, *, obj_in: SysUserCreate) -> SysUser:
        db_obj = SysUser(
            username=obj_in.username,
            password=get_password_hash(obj_in.password),
            is_superuser=obj_in.is_superuser,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


sys_user = CRUDSysUser(SysUser)
