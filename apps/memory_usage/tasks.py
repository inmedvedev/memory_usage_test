from app import celery_app
import psutil
import requests


@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5, check_memory_usage.s(), name="Check memory usage")


@celery_app.task
def check_memory_usage(alarm_percent_value=0):
    mem_percent = psutil.virtual_memory().percent
    if mem_percent > alarm_percent_value:
        requests.post(
            "http://flask:8080/api/memory_usage/create",
            json={"percent": mem_percent},
        )
