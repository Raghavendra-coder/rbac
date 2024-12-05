from . import utils
from .serializers import *

def create_permission_service(data):
    name = data["name"].strip()
    data["name"] = name.upper().replace(" ", "_")
    create_permission = utils.add_permission(data)
    data = PermissionSerializer(create_permission).data
    return data


def view_permission_service(user, my_permissions):
    if my_permissions == "true":
        permissions = user.role.permissions.all()
    else:
        permissions = Permissions.objects.all()
    data = PermissionSerializer(permissions, many=True).data
    return data


def delete_permission_service(data):
    name = data["name"].strip()
    final_name = name.upper().replace(" ", "_")
    permission = Role.objects.filter(name=final_name).first()
    if not permission:
        raise Exception(f"No permission found with name - {name}")
    else:
        permission.delete()
        return "DELETED"