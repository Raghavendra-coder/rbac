from .models import Permissions, Role
from enums import PermissionsEnum


def add_permission(data):
    permission = Permissions.objects.filter(name=data["name"]).first()
    if not permission:
        permission = Permissions.objects.create(name=data["name"], description=data["description"])
    role = Role.objects.get(name="ADMIN")
    role.permissions.add(permission)

    return permission
