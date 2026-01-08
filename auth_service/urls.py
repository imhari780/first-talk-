from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginView, RoleView

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("role/", RoleView.as_view()),
]
