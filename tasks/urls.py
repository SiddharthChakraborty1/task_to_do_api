from django.urls import path
from . import views

urlpatterns=[
    path('getTasksByUserId/<userId>/', views.getTasksByUserId, name='getTasksByUserId'),
    path('createTask/', views.createTask, name = 'createTask'),
    path('getTaskById/<id>/', views.getTaskById, name = 'getTaskbyId'),
    path('updateTask/', views.updateTask, name='updateTask'),
    path('deleteTask/<taskId>/', views.deleteTask, name='deleteTask')
]