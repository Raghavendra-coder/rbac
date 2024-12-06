from .models import *
from rest_framework.serializers import ModelSerializer, SerializerMethodField

class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permissions
        fields = "__all__"

class RolePermissionSerializer(ModelSerializer):
    class Meta:
        model = Permissions
        fields = ["name"]


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class DetailedRoleSerializer(ModelSerializer):
    permissions = SerializerMethodField()
    class Meta:
        model = Role
        fields = "__all__"

    def get_permissions(self, obj):
        permissions = list(obj.permissions.all().values('name'))
        data = [i["name"] for i in permissions]
        return data