from .models import *
from .serializers import *
from . import utils

def create_resource_service(user, data):
    resource = utils.create_resource(user, data)
    data = ResourceSerializer(resource).data
    return data


def get_resource_service(user, my_resources):
    resources = Resource.objects.all()
    if my_resources == "true":
        resources = resources.filter(created_by=user)
    data = ResourceSerializer(resources, many=True).data
    return data


def update_resource_service(user, data):
    resource = utils.get_resource_by_id(data["id"])
    resource.title = data["title"]
    resource.description = data["description"]
    resource.last_modified_by = user
    resource.save()
    data = ResourceSerializer(resource).data
    return data


def delete_resource_service(data):
    resource = utils.get_resource_by_id(data["id"])
    resource.delete()
    return "DELETED"