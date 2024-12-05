from enum import Enum


class StatusTypesEnum(Enum):
    active = "active"
    inactive = "inactive"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class PermissionsEnum(Enum):
    CREATE_PERMISSION = "can create permissions"
    CREATE_USERS = "can create users"
    RETRIEVE_USERS = "can retrieve users"


    @classmethod
    def get_all_permissions(cls):
        return [i.name for i in cls]

    @classmethod
    def get_permissions_info(cls):
        return [{"name": i.name, "description": i.value} for i in cls]


class DefaultRoles(Enum):
    ADMIN = PermissionsEnum.get_all_permissions()
    SUPERVISOR = [PermissionsEnum.RETRIEVE_USERS.name]
    STAFF = [PermissionsEnum.RETRIEVE_USERS.name]