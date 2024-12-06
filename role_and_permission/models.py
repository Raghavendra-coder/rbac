from django.db import models
import uuid

# Create your models here.


class Permissions(models.Model):
    id = models.CharField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False, max_length=36)
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    id = models.CharField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False, max_length=36)
    name = models.CharField(max_length=200, null=True, blank=True)
    is_default = models.BooleanField(default=False, null=True, blank=True)
    permissions = models.ManyToManyField(Permissions, related_name="in_roles", null=True, blank=True)

    def __str__(self):
        return self.name

