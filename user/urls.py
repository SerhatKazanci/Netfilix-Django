from django.urls import path
from .views import *
urlpatterns = [
    path('login/', userLogin, name="login"),
    path('register/', userRegister, name="register"),
    path('logout/', userLogout, name='logout'),
    path('create-profile/', createProfile, name='create-profile'),
    path('profile/', userProfile, name="profile"),
    path('delete/', userDelete, name="delete")
]