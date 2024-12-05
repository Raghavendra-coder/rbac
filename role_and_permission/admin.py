from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

# Register your models here.
class RoleAdmin(ModelAdmin):
    filter_horizontal = ["permissions"]

admin.site.register(Role, RoleAdmin)
admin.site.register(Permissions)
