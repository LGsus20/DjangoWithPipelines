from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("users/", views.users, name="Users"),
    path("users_create/", views.create_user, name="Create_user"),
    path("users_delete/<int:user_id>/", views.delete_user, name="Delete_user"),
]