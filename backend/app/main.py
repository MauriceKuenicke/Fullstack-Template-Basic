from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from typing import Callable, Awaitable
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.api import api_router
from app.common.database import get_backend_db_engine


app = FastAPI(title="Template Backend API",
              swagger_ui_parameters={"defaultModelsExpandDepth": -1})

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.middleware("http")
async def log_request(request: Request, call_next: Callable[..., Awaitable[JSONResponse]]):
    try:
        engine = get_backend_db_engine()
        request.state.db = Session(autocommit=False, autoflush=False, twophase=False, bind=engine)
        response = await call_next(request)
    except Exception as excp:
        response = JSONResponse("Internal server error", status_code=500)
        print(excp)

    request.state.db.close()
    return response
