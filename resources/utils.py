from .models import *

def create_resource(user, data):
    resource = Resource.objects.create(title=data["title"], description=data.get("description"), created_by=user)
    return resource


def get_resource_by_id(id):
    resource = Resource.objects.filter(id=id).first()
    return resource