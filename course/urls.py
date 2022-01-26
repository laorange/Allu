from django.urls import path, reverse, include
from django.views.generic import RedirectView

from . import views
from .drf.drf_views import router

urlpatterns = [
    path('', RedirectView.as_view(url=r'api/')),
    path('api/', include(router.urls)),
]
