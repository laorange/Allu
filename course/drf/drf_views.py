from rest_framework import routers
from .filter import drf_containers

router = routers.DefaultRouter()

_sorted_items = sorted(drf_containers.items(), key=lambda i: i[0])
for _key, _container in _sorted_items:
    router.register(_container.name, _container.view_set, basename=_container.name)
