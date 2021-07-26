from django.urls import path
from . import views

urlpatterns = [
    path('createUser/', views.createUser, name='createUser' ),
path('getUsers/', views.getUsers, name = 'getUsers'),
path('getUserById/<id>/', views.getUserById, name='getUserById'),
path('getUserByEmail/<email>/', views.getUserByEmail, name='getUserByEmail'),
path('LoginUser/', views.userLogin, name='userLogin')
]