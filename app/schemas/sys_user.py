from typing import Optional

from pydantic import BaseModel


# Shared properties
class SysUserBase(BaseModel):
    username: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False


# Properties to receive via API on creation
class SysUserCreate(SysUserBase):
    username: str
    password: str


# Properties to receive via API on update
class SysUserUpdate(SysUserBase):
    password: Optional[str] = None


class SysUserInDBBase(SysUserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class SysUser(SysUserInDBBase):
    pass


# Additional properties stored in DB
class SysUserInDB(SysUserInDBBase):
    password: str
