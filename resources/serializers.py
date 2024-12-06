from rest_framework.serializers import ModelSerializer
from .models import Resource


class ResourceSerializer(ModelSerializer):

    class Meta:
        model = Resource
        fields = "__all__"