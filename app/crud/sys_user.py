from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.sys_user import SysUser
from app.schemas.sys_user import SysUserCreate, SysUserUpdate


class CRUDSysUser(CRUDBase[SysUser, SysUserCreate, SysUserUpdate]):
    def get_by_username(self, db: Session, username: str) -> Optional[SysUser]:
        return db.query(SysUser).filter(SysUser.username == username).first()


sys_user = CRUDSysUser(SysUser)
