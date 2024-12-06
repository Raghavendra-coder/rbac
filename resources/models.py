from django.db import models
import uuid

# Create your models here.


class Resource(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=36, unique=True, editable=False)
    title = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey('user.User', related_name="created_resources", on_delete=models.SET_NULL, null=True)
    last_modified_by = models.ForeignKey('user.User', related_name="updated_resources", on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title