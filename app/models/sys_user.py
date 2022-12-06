from sqlalchemy import Boolean, Column, Integer, String

from app.db.base_class import Base


class SysUser(Base):
    __tablename__ = "sys_user"

    id = Column(Integer(), primary_key=True, index=True)
    username = Column(String(255))
    password = Column(String(255))
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
