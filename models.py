from django.db import models


class TaskInfo(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    started = models.BooleanField(default=True)
    finished = models.BooleanField(default=False)
