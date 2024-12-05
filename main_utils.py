from rest_framework.response import Response
from django.conf import settings
import jwt
from role_and_permission.models import Role
from enums import DefaultRoles

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

def add_default_roles():
    admin = Role.objects.filter(name="ADMIN").first()
    if not admin:
        admin = Role.objects.create(name='ADMIN', permissions=DefaultRoles.ADMIN.value)
    supervisor = Role.objects.filter(name="SUPERVISOR").first()
    if not supervisor:
        supervisor = Role.objects.create(name='SUPERVISOR', permissions=DefaultRoles.SUPERVISOR.value)
    staff = Role.objects.filter(name="STAFF").first()
    if not staff:
        staff = Role.objects.create(name='STAFF', permissions=DefaultRoles.STAFF.value)