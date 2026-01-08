from django.urls import path
from .views import start_dialogue, send_message, end_dialogue

urlpatterns = [
    path('dialogue/start', start_dialogue),
    path('dialogue/<uuid:session_id>/message', send_message),
    path('dialogue/<uuid:session_id>/end', end_dialogue),
]
