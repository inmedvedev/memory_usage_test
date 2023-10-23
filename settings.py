import os

from dotenv import load_dotenv

load_dotenv(".env")

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

MONGODB_URL = os.environ.get("MONGODB_URL")
