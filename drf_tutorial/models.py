from django.db import models
from django.db.models import fields, indexes

from django.db.models.base import Model

# Create your models here.

class Singer(models.Model):
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['name',]),
        ]

    def __str__(self) -> str:
        return self.name
    

class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE,
    related_name="sung_by")
    duration = models.IntegerField()

    def __str__(self) -> str:
        return self.title
