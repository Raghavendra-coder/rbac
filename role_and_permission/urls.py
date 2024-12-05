from django.urls import path
from . import views

urlpatterns = [
    path("create_permission/", views.create_permission, name="create_permission"),
    path("view_permission/", views.view_permission, name="view_permission"),
    path("delete_permission/", views.delete_permission, name="delete_permission"),
    ]