from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    mobile = models.CharField(max_length=13, blank=True, null=True)
    role = models.OneToOneField('role_and_permission.Role',on_delete=models.SET_NULL, null=True,
                              related_name="users")



