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


def create_custom_role_service(data):
    create_role = utils.create_role(data["name"], data.get("permissions", []))
    data = DetailedRoleSerializer(create_role).data
    return data


def get_all_roles_service(user, my_role):
    roles = Role.objects.all()
    if my_role or my_role == "true":
        roles = user.role
        data = DetailedRoleSerializer(roles).data
    else:
        data = DetailedRoleSerializer(roles, many=True).data
    return data


def update_role_service(data):
    role = utils.get_role_by_id(data["id"])
    if role.is_default:
        raise Exception("you cannot modify default roles")
    name = data["name"].strip()
    final_name = name.upper().replace(" ", "_")
    role.name = final_name
    role.save()
    role.permissions.clear()
    permissions = Permissions.objects.filter(name__in=data["permissions"])
    role.permissions.add(*list(permissions))
    data = DetailedRoleSerializer(role).data
    return data


def delete_role_service(data):
    role = utils.get_role_by_id(data["id"])
    if role.is_default:
        raise Exception("default role cannot be deleted")
    role.delete()
    return "DELETED"