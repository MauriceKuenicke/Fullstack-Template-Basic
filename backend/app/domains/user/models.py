from app.common.base_dataclass import BaseDataClass
from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserCreate(BaseDataClass):
    username: str
    password: str


@dataclass
class UserRead(BaseDataClass):
    user_uuid: str
    username: str
    created_at: datetime
    updated_at: datetime

@dataclass
class UserUsernameUpdate(BaseDataClass):
    username: str

@dataclass
class UserPasswordUpdate(BaseDataClass):
    password: str