from celery import Celery
from config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND
celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task
def add(x, y):
    return x + y
