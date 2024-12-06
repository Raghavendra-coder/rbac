from .models import User
from django.contrib.auth.hashers import check_password
from role_and_permission.utils import get_role_by_id

def check_user(email: str, password: str):
    user = User.objects.filter(email__iexact=email).first()
    if user:
        res = check_password(password, user.password)
        if not res:
            return False, "incorrect password !"
    else:
        return False, f"user with mail - {email} not found !"
    return True, user


def get_user_by_id(id):
    user = User.objects.get(id=id)
    return user


def create_user(data):
    role = get_role_by_id(data["role_id"])
    user = User.objects.create(
        first_name=data["first_name"],
        last_name=data["last_name"],
        email=data["email"],
        username=data["email"],
        password=data["password"],
        role=role
    )

    return user