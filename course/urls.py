from django.urls import path, include  # reverse
from django.views.generic import RedirectView

from . import views
from .drf.drf_views import router

urlpatterns = [
    path('', RedirectView.as_view(url=r'api/')),
    path('api/', include(router.urls)),
    path('advanced/api/classroom/', views.advanced_classroom_api)
]
