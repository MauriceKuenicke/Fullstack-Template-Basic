from fastapi import APIRouter
from app.domains.user.api import router as user_router
from app.domains.worker.api import router as worker_router

api_router = APIRouter()

api_router.include_router(user_router, include_in_schema=True, prefix="/user", tags=["User Management"])
api_router.include_router(worker_router, include_in_schema=True, prefix="/worker", tags=["Background Worker Tasks"])
