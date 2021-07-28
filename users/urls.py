from django.urls import path
from . import views

urlpatterns = [
    path('createUser/', views.createUser, name='createUser' ),
path('getUsers/', views.getUsers, name = 'getUsers'),
path('getUserById/<id>/', views.getUserById, name='getUserById'),
path('getUserByEmail/<email>/', views.getUserByEmail, name='getUserByEmail'),
path('UserView/<id>/', views.UserView.as_view(), name='userViewById'),
path('UserView/', views.UserView.as_view(), name='userViewCreate'),
path('LoginUser/', views.userLogin, name='userLogin')
]