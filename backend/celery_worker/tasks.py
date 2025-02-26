from sqlalchemy.orm import Session
from celery import shared_task
from app.domains.user.service import UserService
from app.common.database import get_backend_db_engine
import time


@shared_task(name='celery_worker.tasks.execute_something', bind=True)
def execute_something(self,
                      user_uuid: str) -> bool:

    engine = get_backend_db_engine()
    sess = Session(autocommit=False, autoflush=False, twophase=False, bind=engine)
    user_service = UserService(sess)
    print(self.request.id)
    selected_user = user_service.get_user_by_uuid(user_uuid)
    print(selected_user)
    time.sleep(60)
    return True
