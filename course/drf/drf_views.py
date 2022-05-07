import re

from rest_framework import routers
from .filter import drf_containers


def camel_to_dash(camel: str):
    camel = camel.replace('-', '')
    return re.sub(r'([a-z])([A-Z])', r'\1-\2', camel).lower()


router = routers.DefaultRouter()

_sorted_items = sorted(drf_containers.items(), key=lambda i: i[0])
for _key, _container in _sorted_items:
    router.register(_container.name, _container.view_set, basename=_container.name)
    if (dash_name := camel_to_dash(_container.name)) != _container.name:
        router.register(dash_name, _container.view_set, basename=dash_name)
