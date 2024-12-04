from rest_framework.response import Response
from django.conf import settings
import jwt

def create_success_response(message: str, data: any):

    response = {
        "success": True,
        "message": message,
        "data": data,
    }

    return Response(response, headers={'Access-Control-Allow-Origin': '*'})


def create_error_response(message: str):

    response = {
        "success": False,
        "message": message,
    }

    return Response(response, headers={'Access-Control-Allow-Origin': '*'})

def get_jwt_token(payload, expiry):
    return jwt.encode({"user": payload, "exp": expiry}, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)