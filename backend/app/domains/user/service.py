from fastapi import HTTPException

from sqlalchemy import text
from sqlalchemy.orm import Session
from app.domains.user.models import (UserRead, UserCreate)
from uuid import uuid4
from app.common.secrets_utility import encrypt_password
from app.common.datetime_utility import get_current_ts_string


class UserService:
    def __init__(self, db_session: Session):
        self._db_session = db_session

    def get_user_by_uuid(self, uuid: str) -> UserRead:
        selected_user_sql = text("SELECT * FROM users WHERE user_uuid = :user_uuid")
        selected_user = self._db_session.execute(selected_user_sql,{"user_uuid": uuid}).fetchone()
        if not selected_user:
            raise HTTPException(status_code=404)
        return UserRead(
            user_uuid=selected_user.user_uuid,
            username=selected_user.username,
            created_at=selected_user.created_at,
            updated_at=selected_user.updated_at
        )

    def user_exists_by_uuid(self, uuid: str) -> bool:
        selected_user_sql = text("SELECT user_uuid FROM users WHERE user_uuid = :user_uuid")
        selected_user = self._db_session.execute(selected_user_sql,{"user_uuid": uuid}).fetchone()
        if selected_user:
            return True
        return False

    def user_exists_by_name(self, name: str) -> bool:
        selected_user_sql = text("SELECT user_uuid FROM users WHERE username = :username")
        selected_user = self._db_session.execute(selected_user_sql,{"username": name}).fetchone()
        if selected_user:
            return True
        return False

    def user_exists_by_name_and_is_not_self(self, name: str, user_uuid: str) -> bool:
        selected_user_sql = text("SELECT user_uuid FROM users WHERE username = :username AND NOT user_uuid = :user_uuid")
        selected_user = self._db_session.execute(selected_user_sql,{"username": user_uuid,
                                                                          "user_uuid": user_uuid}).fetchone()
        if selected_user:
            return True
        return False

    def create_new_user(self, data: UserCreate) -> UserRead:
        new_user_uuid = str(uuid4())
        if self.user_exists_by_name(data.username):
            raise HTTPException(
                status_code=409,
                detail="User with this name already exists."
            )
        insert_new_user_sql = """
        INSERT INTO users (user_uuid, username, password, created_at, updated_at)
        VALUES (:user_uuid, :username, :password, :created_at, :updated_at)
        """
        current_ts = get_current_ts_string()
        self._db_session.execute(text(insert_new_user_sql),{"user_uuid": new_user_uuid,
                                                               "username": data.username,
                                                               "password": encrypt_password(data.password),
                                                               "created_at": current_ts,
                                                               "updated_at": current_ts
                                                               })
        self._db_session.commit()

        selected_user = self.get_user_by_uuid(new_user_uuid)
        return selected_user

    def delete_user(self, uuid: str) -> None:
        if not self.user_exists_by_uuid(uuid):
            raise HTTPException(status_code=404)
        delete_user_sql = text("DELETE FROM users WHERE user_uuid = :user_uuid")
        self._db_session.execute(delete_user_sql,{"user_uuid": uuid})
        self._db_session.commit()

    def list_available_users(self) -> list[UserRead]:
        sql = """
        SELECT * FROM users
        """
        result = self._db_session.execute(text(sql)).fetchall()
        return [
            UserRead(
                user_uuid=x.user_uuid,
                username=x.username,
                created_at=x.created_at,
                updated_at=x.updated_at
            ) for x in result
        ]