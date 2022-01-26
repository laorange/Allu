from django.urls import path  # , reverse, include
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
]
