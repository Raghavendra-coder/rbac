from .models import Permissions
from enums import PermissionsEnum

def add_all_permissions():
    for permission in PermissionsEnum:
        old_permission = Permissions.objects.filter(name=permission.name).first()
        if not old_permission:
            Permissions.objects.create(name=permission.name, description=permission.value)