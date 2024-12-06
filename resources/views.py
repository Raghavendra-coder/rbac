from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from main_utils import create_error_response, create_success_response
from rbac.custom_decorators.auth import authorize
from enums import PermissionsEnum
from . import services

# Create your views here.


@api_view(["POST"])
@authorize([PermissionsEnum.CREATE_RESOURCE.name])
def create_resource(request):
    try:
        user = request.auth_user
        data = request.data
        resource = services.create_resource_service(user, data)
        response = create_success_response("resource created successfully !", resource)
    except Exception as e:
        response = create_error_response(f"resource creation failed --> {e}")
    return response


@api_view(["GET"])
@authorize([PermissionsEnum.GET_RESOURCE.name])
def get_resource(request):
    try:
        user = request.auth_user
        my_resources = request.query_params.get("my_resources")
        resource = services.get_resource_service(user, my_resources)
        response = create_success_response("resource retrieved successfully !", resource)
    except Exception as e:
        response = create_error_response(f"resource retrieval failed --> {e}")
    return response


@api_view(["POST"])
@authorize([PermissionsEnum.UPDATE_RESOURCE.name])
def update_resource(request):
    try:
        user = request.auth_user
        data = request.data
        resource = services.update_resource_service(user, data)
        response = create_success_response("resource updated successfully !", resource)
    except Exception as e:
        response = create_error_response(f"resource update failed --> {e}")
    return response


@api_view(["POST"])
@authorize([PermissionsEnum.DELETE_RESOURCE.name])
def delete_resource(request):
    try:
        user = request.auth_user
        data = request.data
        resource = services.delete_resource_service(data)
        response = create_success_response("resource deleted successfully !", resource)
    except Exception as e:
        response = create_error_response(f"resource deletion failed --> {e}")
    return response