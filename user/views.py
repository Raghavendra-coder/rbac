from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import services
from main_utils import *
from rbac.custom_decorators.auth import authorize

# Create your views here.

@api_view(["POST"])
def login(request):
    try:
        data = request.data
        login, data = services.login_service(data)
        if login:
            create_response = create_success_response("login success", data)
        else:
            create_response = create_error_response(data)
    except Exception as e:
        create_response = create_error_response(f"{e}")
    return create_response


@api_view(["POST"])
@authorize([PermissionsEnum.CREATE_USERS.name])
def create_user(request):
    try:
        data = request.data
        user = services.create_user_service(data)
        response = create_success_response("user created successfully", user)
    except Exception as e:
        response = create_error_response(f"user creation failed --> {e}")
    return response