from django.http import response
from django.http.response import HttpResponse
from django.test import TestCase, Client
import rest_framework
from .models import Users
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
import json


# Testing CRUD with django ORM and unittest framework

class UserDatabaseTests(TestCase):
    def setUp(self):
        user1 = Users.objects.create(user_name = "user1", user_email = "user@gmail.com", user_password = "abc123",
        user_phone = "8839980045")
        user2 = Users.objects.create(user_name = "user2", user_email = "user@gmail.com", user_password = "abc123",
        user_phone = "8839980046")

    def test_addUsers(self):
        users = Users.objects.all()
        self.assertEqual(users.count(),2)

    def test_userCalues(self):
        self.assert_(Users.objects.filter(user_name = "user1").exists() == True)

    def test_userDeletion(self):
        user1 = Users.objects.get(user_name = "user1")
        user1.delete()
        self.assertEqual(Users.objects.all().count(),1)

    def test_userUpdate(self):
        user2 = Users.objects.filter(user_name = "user2")
        user2.update(user_name = "userTwo")
        self.assertEqual(Users.objects.filter(user_name = "userTwo").exists(), True)



# Testing CRUD with the help of django rest framework api testcase

class UserAPITestCase(TestCase):
    client = Client()

    def setUp(self):
        user1 = Users.objects.create(user_name = "user1", user_email = "user@gmail.com", user_password = "abc123",
        user_phone = "8839980045")

    
    def test_userCreate(self):
        data = dict(user_name = "user2", user_email = "user2@gmail.com",
        user_password = "abc123", user_phone = "8839980045")

        response = self.client.post("/api/users/createUser/", data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_userGet(self):
        
        response = self.client.get("/api/users/getUsers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_userById(self):
        response = self.client.get("/api/users/getUserById/90/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        

        
        