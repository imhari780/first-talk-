from django.urls import path
from .views import store_embedding, query_similar

urlpatterns = [
    path('store/', store_embedding),
    path('query/', query_similar),
]
