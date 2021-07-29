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
from drf_tutorial.models import Singer, Song
from drf_tutorial.Serializer import SingerSerializer

# Create your tests here.

## checking if a new singer is being added to the database using the post method
class APITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.singer= Singer.objects.create(name = "Siddharth", label="Berklee college of music")
        self.song = Song.objects.create(title = "dummy song 1", duration = 5, singer = self.singer)


#Test cases for Singers

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
    
# Test cases for Songs

    def test_songCreate(self):
        data = dict(title = "dummy song title 2", duration = 4, singer = self.singer.id)
        response = self.client.post("/song/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Song.objects.all().count(), 2)
    
    def test_songGet(self):
        response = self.client.get("/song/")
        self.assertEqual(len(response.data),1)

    def test_songGetById(self):
        response = self.client.get(f"/song/{self.song.id}/")
        self.assertEqual(response.data['title'], self.song.title)

    def test_songUpdate(self):
        data = dict(
        title = "updated title", duration = 90,
        singer = self.singer.id)
        response = self.client.put(f"/song/{self.song.id}/", data)
        dummy_song = Song.objects.get(id = self.song.id)
        self.assertEqual(dummy_song.title, "updated title")
        print("Printing song update")
        print(response.status_code)

        # Note: the json object structure for creating or updating a song in this
        # model representation will be as follows:
        # {
            # "title": "Updated title",
            # "duration": 8,
            # "singer": <id of singer>
        # }
    
    def test_songDelete(self):
        no_of_songs = Song.objects.all().count()
        response = self.client.delete(f"/song/{self.song.id}/")
        self.assertEqual(Song.objects.all().count(), no_of_songs - 1)
