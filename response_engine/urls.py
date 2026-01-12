from django.urls import path

from .views import response_engine

urlpatterns = [
    path("generate/", response_engine),
]
