"""DjangoProjectSettings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    path(r'favicon.ico', RedirectView.as_view(url=r'static/favicon.ico')),
    path(r'robots.txt', RedirectView.as_view(url=r'static/robots.txt')),

    path('admin/', admin.site.urls),
    path(r'help/', include_docs_urls(title='接口文档', description="中欧航空工程师学院 课程管理系统")),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),

    path(r'', include('index.urls')),
    path(r'course/', include('course.urls')),
]
