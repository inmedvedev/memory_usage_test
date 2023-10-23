from flask import Flask
from celery_app import celery_init_app
from settings import CELERY_RESULT_BACKEND, CELERY_BROKER_URL
from settings import MONGODB_URL
from mongoengine import connect

from apps.memory_usage.views import memory_usage_blueprint

app = Flask(__name__)
app.config.from_mapping(
    CELERY=dict(
        broker_url=CELERY_BROKER_URL,
        result_backend=CELERY_RESULT_BACKEND,
        task_ignore_result=True,
    ),
)

celery_app = celery_init_app(app)
celery_app.autodiscover_tasks(["apps.memory_usage"], force=True)

connect(host=MONGODB_URL, alias="default", uuidRepresentation="standard")

app.register_blueprint(memory_usage_blueprint)
