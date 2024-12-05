from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from rbac.custom_decorators.auth import authorize
from enums import PermissionsEnum
from . import services
from main_utils import create_error_response, create_success_response

# Create your views here.

@api_view(["POST"])
@authorize([PermissionsEnum.CREATE_PERMISSION.name])
def create_permission(request):
    try:
        data = request.data
        permission = services.create_permission_service(data)
        response = create_success_response("permission created successfully !", permission)
    except Exception as e:
        response = create_error_response(f"error --> {e}")
    return response


@api_view(["GET"])
@authorize([PermissionsEnum.VIEW_PERMISSION.name])
def view_permission(request):
    try:
        user = request.auth_user
        my_permissions = request.query_params.get("my_permissions")
        permission = services.view_permission_service(user, my_permissions)
        response = create_success_response("permission retrieved successfully !", permission)
    except Exception as e:
        response = create_error_response(f"error --> {e}")
    return response


@api_view(["POST"])
@authorize([PermissionsEnum.DELETE_PERMISSION.name])
def delete_permission(request):
    try:
        data = request.data
        permission = services.delete_permission_service(data)
        response = create_success_response("permission deleted successfully !", permission)
    except Exception as e:
        response = create_error_response(f"error --> {e}")
    return response


