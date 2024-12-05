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