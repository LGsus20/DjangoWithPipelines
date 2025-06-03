from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("users/", views.users, name="Users"),
    path("users_create/", views.create_user, name="Create_user"),
]