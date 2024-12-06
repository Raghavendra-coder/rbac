from enum import Enum


class StatusTypesEnum(Enum):
    active = "active"
    inactive = "inactive"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class PermissionsEnum(Enum):
    CREATE_PERMISSION = "can create permissions"
    VIEW_PERMISSION = "can view permissions"
    DELETE_PERMISSION = "can delete permissions"
    CREATE_USERS = "can create users"
    RETRIEVE_USERS = "can retrieve users"
    CREATE_ROLE = "can create role"
    GET_ROLES = "can retrieve all roles"
    UPDATE_ROLE = "can update role"
    DELETE_ROLE = "can delete role"

    CREATE_RESOURCE = "can create resource"
    GET_RESOURCE = "can retrieve resource"
    UPDATE_RESOURCE = "can update resource"
    DELETE_RESOURCE = "can delete resource"


    @classmethod
    def get_all_permissions(cls):
        return [i.name for i in cls]

    @classmethod
    def get_permissions_info(cls):
        return [{"name": i.name, "description": i.value} for i in cls]


class DefaultRoles(Enum):
    ADMIN = PermissionsEnum.get_all_permissions()
    SUPERVISOR = [PermissionsEnum.RETRIEVE_USERS.name, PermissionsEnum.VIEW_PERMISSION.name, PermissionsEnum.CREATE_PERMISSION.name,
                  PermissionsEnum.GET_RESOURCE.name, PermissionsEnum.UPDATE_RESOURCE.name, PermissionsEnum.DELETE_RESOURCE.name]
    STAFF = [PermissionsEnum.RETRIEVE_USERS.name, PermissionsEnum.VIEW_PERMISSION.name, PermissionsEnum.GET_RESOURCE.name]