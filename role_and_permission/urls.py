from django.urls import path
from . import views

urlpatterns = [
    path("create_permission/", views.create_permission, name="create_permission")
    ]