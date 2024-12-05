from .serializers import *
from . import utils
from main_utils import get_jwt_token
from datetime import datetime
from django.conf import settings

def login_service(data):
    email = data["email"]
    password = data["password"]
    found, data = utils.check_user(email, password)
    if not found:
        return False, data
    user_data = UserSerializer(data).data
    jwt_data = UserJWTSerializer(data).data
    print(jwt_data)
    user_data['access_token'] = get_jwt_token(
        jwt_data, datetime.utcnow() + settings.JWT_ACCESS_TOKEN_LIFETIME)
    user_data['refresh_token'] = get_jwt_token(
        jwt_data, datetime.utcnow() + settings.JWT_REFRESH_TOKEN_LIFETIME)
    return True, user_data