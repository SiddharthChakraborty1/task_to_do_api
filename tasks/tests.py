from django.http import response
from django.test import TestCase
from django.test.client import Client
from .models import Tasks
from .models import Users

# Create your tests here.

class TaskDatabaseTestCase(TestCase):
    def setUp(self):
        user1 = Users.objects.create(user_name = "user1", user_email = "user@gmail.com", user_password = "abc123",
        user_phone = "8839980045")
        task = Tasks.objects.create(task_description = "dummy task description",
        task_is_complete = False, user = user1)

    def test_addTask(self):
        user = Users.objects.get(user_name = "user1")
        task = Tasks.objects.create(task_description = "dummy task description",
        task_is_complete = False, user = user)
        tasks = Tasks.objects.all()
        self.assertEqual(tasks.count(),2)

    def test_getTask(self):
        self.assert_(Tasks.objects.filter(user = Users.objects.get(user_name = "user1")).exists() == True)
    
    def test_updateTask(self):
        task = Tasks.objects.filter(user = Users.objects.get(user_name = "user1"))
        task.update(task_is_complete =  True)
        self.assertEqual(Tasks.objects.get(user = Users.objects.get(user_name="user1")).task_is_complete, True)

    
    def test_deleteTask(self):
        task = Tasks.objects.get(user = Users.objects.get(user_name = "user1"))
        task.delete()
        self.assertEqual(Tasks.objects.all().count(),0)

# Testing the api end points
class TestAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = Users.objects.create(user_name = "user1", user_email = "user@gmail.com", user_password = "abc123",
        user_phone = "8839980045")
        self.task = Tasks.objects.create(task_description = "dummy task description",
        task_is_complete = False, user = self.user1)
    
    def test_taskCreate(self):
        data = dict(task_description = "dummy task description", task_is_complete=False, user_id = self.user1.id)
        response = self.client.post("/api/tasks/createTask/", data, content_type='application/json')
        self.assertEqual(Tasks.objects.all().count(), 2)

    def test_taskUpdate(self):
        id = Tasks.objects.get(user = self.user1).id
        data = dict(id= id, task_description = 'updated task description', task_is_complete = True, user_id = self.user1.id)
        print(data)
        response = self.client.put("/api/tasks/updateTask/", data, content_type='application/json')
        print(response.status_code)
        task = Tasks.objects.get(user = self.user1)
        self.assertEqual(task.task_description, "updated task description")


    def test_taskDelete(self):
        task = Tasks.objects.get(user = self.user1)
        response = self.client.delete(f"/api/tasks/deleteTask/{task.id}/")
        print(response.status_code)
        self.assertEqual(Tasks.objects.all().count(),0)

    

    
    

        
