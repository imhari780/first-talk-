from django.urls import path

from .views import query_similar, store_embedding

urlpatterns = [
    path("store/", store_embedding),
    path("query/", query_similar),
]
