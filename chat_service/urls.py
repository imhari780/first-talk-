# from django.urls import path

# from .views import delete_message, send_message

# urlpatterns = [
#     path("chat/message/", send_message),
#     path("chat/message/<str:room_id>/<uuid:message_id>/", delete_message),
# ]
# from django.urls import path
# from .views import send_message

# urlpatterns = [
#     path("messages/send/", send_message, name="send_message"),
# ]
from django.urls import path
from .views import send_message, delete_message

app_name = "chat_service"

urlpatterns = [
    # POST /api/messages/send/
    path(
        "messages/send/",
        send_message,
        name="send_message",
    ),
    # DELETE /api/messages/<room_id>/<message_id>/
    path(
        "messages/<str:room_id>/<str:message_id>/",
        delete_message,
        name="delete_message",
    ),
]
