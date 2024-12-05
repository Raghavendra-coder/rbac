from . import utils
from .serializers import *

def create_permission_service(data):
    name = data["name"].strip()
    data["name"] = name.upper().replace(" ", "_")
    create_permission = utils.add_permission(data)
    data = PermissionSerializer(create_permission).data
    return data