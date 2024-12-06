from .models import Permissions, Role
from enums import PermissionsEnum


def add_permission(data):
    permission = Permissions.objects.filter(name=data["name"]).first()
    if not permission:
        permission = Permissions.objects.create(name=data["name"], description=data["description"])
    role = Role.objects.get(name="ADMIN")
    role.permissions.add(permission)
    return permission


def create_role(name, permissions):
    name = name.strip()
    final_name = name.upper().replace(" ", "_")
    role = Role.objects.filter(name=final_name)
    if role:
        raise Exception(f"role already exists")
    role = Role.objects.create(name=final_name)
    permission_objects = Permissions.objects.filter(name__in=permissions)
    role.permissions.add(*list(permission_objects))
    return role


def get_role_by_id(id):
    role = Role.objects.filter(id=id).first()
    return role