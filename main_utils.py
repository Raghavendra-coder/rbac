from rest_framework.response import Response
from django.conf import settings
import jwt
from role_and_permission.models import Role, Permissions
from enums import DefaultRoles, PermissionsEnum

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

def add_all_permissions():
    for permission in PermissionsEnum:
        old_permission = Permissions.objects.filter(name=permission.name).first()
        if not old_permission:
            Permissions.objects.create(name=permission.name, description=permission.value)


def add_default_roles():
    admin = Role.objects.filter(name="ADMIN").first()
    if not admin:
        admin = Role.objects.create(name='ADMIN', is_default=True)
    admin_permissions = Permissions.objects.filter(name__in=DefaultRoles.ADMIN.value)
    admin.permissions.add(*list(admin_permissions))

    supervisor = Role.objects.filter(name="SUPERVISOR").first()
    if not supervisor:
        supervisor = Role.objects.create(name='SUPERVISOR', is_default=True)
    supervisor_permissions = Permissions.objects.filter(name__in=DefaultRoles.SUPERVISOR.value)
    supervisor.permissions.add(*list(supervisor_permissions))

    staff = Role.objects.filter(name="STAFF").first()
    if not staff:
        staff = Role.objects.create(name='STAFF', is_default=True)
    staff_permissions = Permissions.objects.filter(name__in=DefaultRoles.STAFF.value)
    staff.permissions.add(*list(staff_permissions))