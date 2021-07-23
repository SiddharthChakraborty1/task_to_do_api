from django.db import models
from users.models import Users

# Create your models here.


class Tasks(models.Model):
    task_description = models.TextField()
    task_is_complete = models.BooleanField(default=False)
    task_upload_date = models.DateField(auto_now_add=True, auto_now=False)

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
