from django.db.models.fields import DateField
from django.shortcuts import render
from .models import Tasks, Users
import json
from django.http import HttpResponse
import datetime

# Create your views here.

def getTasksByUserId(request, userId):
    if request.method == 'GET':
        userId = int(userId)
        if Users.objects.filter(id = userId).exists():
            taskList = []
            user = Users.objects.get(id=userId)
            tasks = user.tasks_set.all()
            for task in tasks:
                taskDict = dict(id = task.id, task_description = task.task_description,
                task_is_complete = task.task_is_complete, task_upload_date = task.task_upload_date)
                taskList.append(taskDict)
            return HttpResponse(json.dumps(taskList, default=myConverter), content_type='application/json')


def createTask(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode("utf-8"))
        userId = int(received_data['user_id'])
        if Users.objects.filter(id = userId).exists():
            user = Users.objects.get(id = userId)
            
            task = Tasks.objects.create(task_description = received_data['task_description'],
            task_is_complete = received_data['task_is_complete'],
            user = user)
            task.save()
            taskDict = dict(id = task.id,
            task_description = task.task_description,
            task_is_complete = task.task_is_complete,
            task_upload_date = task.task_upload_date)
            return HttpResponse(json.dumps(taskDict, default=myConverter), content_type = 'application/json')
        else:
            taskDict = dict(id = None)
            return HttpResponse(json.dumps(taskDict), content_type = 'application/json')



def getTaskById(request, id):
    if request.method == 'GET':
        taskDict = {}
        id = int(id)
        if Tasks.objects.filter(id = id).exists():
            task = Tasks.objects.get(id=id)
            taskDict = dict(id = task.id,
            task_description = task.task_description,
            task_is_complete = task.task_is_complete,
            task_upload_date = task.task_upload_date,
            user_id = task.user_id)
        else:
            taskDict = dict(id = None)
        return HttpResponse(json.dumps(taskDict, default=myConverter), content_type='application/json')

def updateTask(request):
    if request.method == 'PUT':
        received_data = json.loads(request.body.decode("utf-8"))
        if Users.objects.filter(id = received_data['user_id']).exists():
            task = Tasks.objects.get(id = int(received_data['id']))
            if 'task_description' in received_data.keys():
                task.task_description = received_data['task_description']
            if 'task_is_complete' in received_data.keys():
                task.task_is_complete = received_data['task_is_complete']
            task.save()
            received_data = dict(id = task.id,
            task_description = task.task_description,
            task_is_complete = task.task_is_complete,
            task_upload_date = task.task_upload_date,
            user_id = task.user_id)
            return HttpResponse(json.dumps(received_data, default=myConverter), content_type='application/json')

        
def deleteTask(request, taskId):
    if request.method == 'DELETE':
        taskId = int(taskId)
        print(taskId)
        if Tasks.objects.filter(id = taskId).exists():
            print("Task with id found")
            task = Tasks.objects.get(id = taskId)
            task.delete()
            return HttpResponse(status = 204)
        else:
            print("Task with id not found")
            return HttpResponse(status = 404)




def myConverter(o):
    if isinstance(o, datetime.date):
        return o.__str__()

