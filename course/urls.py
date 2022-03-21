from django.urls import path, re_path, include  # reverse
from django.views.generic import TemplateView  # RedirectView,

from . import views
from .drf.drf_views import router

urlpatterns = [
    re_path(r'^index.html/(?P<path>.*)$', TemplateView.as_view(template_name="course/index.html")),
    path('api/', include(router.urls)),
    path('advanced/api/classroom/', views.advanced_classroom_api),
    path('AlluAdmin/', views.alluAdmin),
]
