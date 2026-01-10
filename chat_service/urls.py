from django.urls import path
from .views import send_message, delete_message

urlpatterns = [
    path("chat/message/", send_message),
    path("chat/message/<str:room_id>/<uuid:message_id>/", delete_message),
]
