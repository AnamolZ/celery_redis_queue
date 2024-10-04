# app/celery_worker.py
from celery import Celery

celery_app = Celery(
    "notification_worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True
)

# Ensure tasks are discovered
celery_app.autodiscover_tasks(['app.main'])