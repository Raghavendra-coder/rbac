from django.urls import path
from . import views

urlpatterns = [
    path("create_permission/", views.create_permission, name="create_permission"),
    path("view_permission/", views.view_permission, name="view_permission"),
    path("delete_permission/", views.delete_permission, name="delete_permission"),
    path("create_custom_role/", views.create_custom_role, name="create_custom_role"),
    path("get_all_roles/", views.get_all_roles, name="get_all_roles"),
    path("get_my_role/", views.get_my_role, name="get_my_role"),
    path("update_role/", views.update_role, name="update_role"),
    path("delete_role/", views.delete_role, name="delete_role"),
    ]