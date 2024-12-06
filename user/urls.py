from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("create_user/", views.create_user, name="create_user")
    ]