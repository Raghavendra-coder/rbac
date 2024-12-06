from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("create_resource/", views.create_resource, name="create_resource"),
    path("get_resource/", views.get_resource, name="get_resource"),
    path("update_resource/", views.update_resource, name="update_resource"),
    path("delete_resource/", views.delete_resource, name="delete_resource"),
    ]