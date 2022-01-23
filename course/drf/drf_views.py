from rest_framework import routers
from .filter import drf_containers

router = routers.DefaultRouter()

for container in drf_containers.values():
    router.register(container.name, container.view_set, basename=container.name)
