from django.db import models

# Create your models here.


class Users(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    user_password = models.CharField(max_length=10)
    user_phone = models.CharField(max_length=12)

