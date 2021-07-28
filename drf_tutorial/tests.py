import json
from unittest import signals
from django.contrib.auth.models import User
from django.db import reset_queries
from django.http import response
from django.urls import reverse
import rest_framework
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from drf_tutorial.models import Singer
from drf_tutorial.Serializer import SingerSerializer

# Create your tests here.

## checking if a new singer is being added to the database using the post method
class SingerTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.singer= Singer.objects.create(name = "Siddharth", label="Berklee college of music")


    def test_singerCreate(self):
        data = dict(name="singer1", label="DnH")

        response = self.client.post("/singer/", data)
        print('printing post singer response data')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Singer.objects.filter(name="singer1").exists(), True)

    def test_singerGetById(self):
        response = self.client.get(f"/singer/{self.singer.id}/")
        self.assertEqual(self.singer.name, response.data['name'] )

    def test_singersGet(self):
        singer = dict(name="singer 2", label = "label 2")
        response = self.client.post("/singer/", singer)
        response = self.client.get("/singer/")
        self.assertEqual(len(response.data), 2)

    def test_singerUpdate(self):
        data = dict(id = self.singer.id,
        name='singer updated',
        label = 'label updated')

        response = self.client.put(f"/singer/{self.singer.id}/", data)
        print('printing singer udpate')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_singerDelete(self):
        nos = Singer.objects.all().count()
        response = self.client.delete(f"/singer/{self.singer.id}/")
        self.assertEqual(Singer.objects.all().count(), nos-1)