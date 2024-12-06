from .models import *
from rest_framework.serializers import ModelSerializer

class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permissions
        fields = "__all__"


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class DetailedRoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        depth = 1
        fields = "__all__"