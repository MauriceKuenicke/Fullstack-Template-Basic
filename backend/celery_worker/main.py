from celery import Celery

celery_app = Celery(
    "main",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=['celery_worker.tasks']
)
