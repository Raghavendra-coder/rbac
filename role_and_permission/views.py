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

