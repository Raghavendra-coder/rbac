from .models import User
from django.contrib.auth.hashers import check_password

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