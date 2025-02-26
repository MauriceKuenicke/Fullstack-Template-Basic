from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.common import deps
from app.domains.user.models import (UserRead, UserCreate)
from app.domains.user.service import UserService

router = APIRouter()


@router.post("/create",
             response_model=UserRead,
             summary="Create a new user.")
def create_new_sf_persona(data: UserCreate,
                          db: Session = Depends(deps.get_main_db)):
    user_service = UserService(db)
    new_user = user_service.create_new_user(data)
    return new_user

@router.get("/list",
            response_model=list[UserRead],
            summary="List available Snowflake personas.")
def list_available_sf_personas(db: Session = Depends(deps.get_main_db)):
    user_service = UserService(db)
    user_list = user_service.list_available_users()
    return user_list

@router.get("/{user_uuid}/read",
            response_model=UserRead,
            summary="Read a user by UUID.")
def read_sf_persona(user_uuid: str,
                    db: Session = Depends(deps.get_main_db)):
    user_service = UserService(db)
    selected_user = user_service.get_user_by_uuid(user_uuid)
    return selected_user

@router.delete("/{user_uuid}/delete", summary="Remove a user by UUID.")
def delete_sf_persona(user_uuid: str,
                      db: Session = Depends(deps.get_main_db)) -> JSONResponse:
    user_service = UserService(db)
    user_service.delete_user(user_uuid)
    return JSONResponse(status_code=200, content="User deleted successfully.")
