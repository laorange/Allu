from django.urls import path, reverse, include
from . import views
from .drf.drf_views import router

urlpatterns = [
    path('', include(router.urls)),
]
