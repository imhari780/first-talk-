from django.urls import path
from . import views

urlpatterns = [
    path('audio/session/create/', views.create_audio_session),
    path('audio/session/<uuid:session_id>/start/', views.start_audio_session),
    path('audio/session/<uuid:session_id>/join/', views.join_audio_session),
    path('audio/session/<uuid:session_id>/stop/', views.stop_audio_session),
]
