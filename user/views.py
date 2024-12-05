from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import services
from main_utils import *

# Create your views here.

@api_view(["post"])
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