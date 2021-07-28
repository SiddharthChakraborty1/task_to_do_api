import json
from django.contrib.auth.models import User
from django.db import reset_queries
from django.http import response
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from drf_tutorial.models import Singer
from drf_tutorial.Serializer import SingerSerializer

# Create your tests here.

## checking if a new singer is being added to the database using the post method
class SingerTestCase(APITestCase):
    def test_singer(self):
        data = dict(name="Siddharth", label="berklee college of music")

        response = self.client.post("/singer/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

