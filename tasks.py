from celery import shared_task
from models import TaskInfo

import time


@shared_task
def fake_task():
    print "creating task"
    task = TaskInfo.objects.create()
    time.sleep(10)
    task.finished = True
    print "updating task ", task.id
    task.save()
