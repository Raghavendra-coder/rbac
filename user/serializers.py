from rest_framework.serializers import ModelSerializer
from .models import User
class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "role"]


class UserJWTSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ('password', 'groups', 'is_staff')