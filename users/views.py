from django.shortcuts import render
from .models import Users
import json
from django.http import HttpResponse
from django.core import serializers
from django.views.generic import  View

# Create your views here.

def getUsers(request):
    if request.method == 'GET':
        userList = []
        users = Users.objects.all()
        for user in users:
            userDict = dict(id=user.id,
            user_name=user.user_name,
            user_email=user.user_email,
            user_phone=user.user_phone)
            userList.append(userDict)
        data = json.dumps(userList)
        return HttpResponse(data, content_type='application/json')


class UserView(View):
    def get(self, request, **kwargs):
        id = int(kwargs['id'])
        if Users.objects.filter(id = id).exists():
            user = Users.objects.get(id = id)
            userDict = dict(id = user.id,
                            user_name = user.user_name)

            return HttpResponse(json.dumps(userDict), content_type='application/json')
    
    def post(self, request,**kwargs):
        received_data = json.loads(request.body.decode("utf-8"))
        email = received_data['user_email']
        if Users.objects.filter(user_email = email).exists():
            userDict = dict(id = None)
            return HttpResponse(json.dumps(userDict), content_type= 'application/json')
        else:
            received_data = json.loads(request.body.decode("utf-8"))
            user = Users.objects.create(user_name = received_data['user_name'],
            user_password = received_data['user_password'],
            user_email = received_data['user_email'],
            user_phone = received_data['user_phone'])
            user.save()
            userDict = dict(id = user.id,
            user_name = user.user_name)
            return HttpResponse(json.dumps(userDict), content_type = 'application/json')
        

def getUserById(request, id):
    if request.method == 'GET':
        id = int(id)
        
        if Users.objects.filter(id = id).exists():
            user = Users.objects.get(id=id)
            userDict = dict(id=user.id, user_name = user.user_name, user_email=user.user_email,
            user_password = user.user_password, user_phone = user.user_phone)
            return HttpResponse(json.dumps(userDict),content_type='application/json')
        else:
            userDict = dict(id = None)
            return HttpResponse(json.dumps(userDict), content_type = 'application/json')

def userLogin(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode("utf-8"))
        if Users.objects.filter(user_email = received_data['user_email']).exists():
            user = Users.objects.get(user_email = received_data['user_email'])
            if user.user_password == received_data['user_password']:
                userDict = dict(result = True)
            else: userDict = dict(result = False)
        else:
            userDict = dict(result = None)
        return HttpResponse(json.dumps(userDict), content_type = 'application/json')

def getUserByEmail(request, email):
    if request.method == 'GET':
        
        
        if Users.objects.filter(user_email = email).exists():
            user = Users.objects.get(user_email = email)
            userDict = dict(id=user.id, user_name = user.user_name, user_email=user.user_email,
            user_password = user.user_password, user_phone = user.user_phone)
            return HttpResponse(json.dumps(userDict), content_type='application/json')
        else:
            userDict = dict(id = None)
            return HttpResponse(json.dumps(userDict), content_type = 'application/json')

def createUser(request):
    if request.method == 'POST':
        rececived_data = json.loads(request.body.decode("utf-8"))
        print(rececived_data)
        print(type(rececived_data))
        if(Users.objects.filter(user_email = rececived_data['user_email']).exists()):
            userDict = dict(id = None)
            return HttpResponse(json.dumps(userDict), content_type='application/json')
        else:
            user = Users.objects.create(user_name=rececived_data['user_name'], user_password = rececived_data['user_password'],
            user_email = rececived_data['user_email'], user_phone = rececived_data['user_phone'])
            print(user)
            user.save()
            data = dict(id = user.id)
            return HttpResponse(json.dumps(data), content_type='application/json')

