from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.common import deps
from uuid import uuid4
from celery_worker.main import celery_app
from fastapi import HTTPException

router = APIRouter()


@router.get("/background-task/{user_uuid}/run",
            summary="Trigger the example background task.")
def trigger_sql_test_case_run(user_uuid: str,
                              db: Session = Depends(deps.get_main_db)) -> JSONResponse:
    execution_uuid = str(uuid4())
    task_result = celery_app.send_task(
        'celery_worker.tasks.execute_single_sql_test',
        args=[user_uuid],
        task_id=execution_uuid
    )
    if task_result.id != execution_uuid:
        raise HTTPException(status_code=500, detail="Something went wrong with the task execution identifiers.")

    return JSONResponse({
        "message": "Test successfully started.",
        "execution_uuid": task_result.id
    }, status_code=200)