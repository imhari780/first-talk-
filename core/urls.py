# # # from django.contrib import admin
# # # from django.urls import include, path
# # # from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# # # urlpatterns = [
# # #     path("admin/", admin.site.urls),
# # #     # SERVICES
# # #     path("auth/", include("auth_service.urls")),
# # #     path("", include("room_gateway.urls")),
# # #     path("memory/", include("memory_service.urls")),
# # #     path("response/", include("response_engine.urls")),
# # #     path("moderation/", include("moderation_service.urls")),
# # #     path("", include("dialogue_service.urls")),
# # #     path("api/", include("audio_broadcast.urls")),
# # #     path("response-engine/", include("response_engine.urls")),
# # #     path("api/", include("chat_service.urls")),
# # # ]
# # from django.contrib import admin
# # from django.urls import include, path

# # urlpatterns = [
# #     path("admin/", admin.site.urls),

# #     # SERVICES
# #     path("auth/", include("auth_service.urls")),
# #     path("", include("room_gateway.urls")),
# #     path("", include("dialogue_service.urls")),

# #     path("memory/", include("memory_service.urls")),
# #     path("moderation/", include("moderation_service.urls")),

# #     path("response/", include("response_engine.urls")),
# #     path("response-engine/", include("response_engine.urls")),

# #     path("api/", include("audio_broadcast.urls")),
# #     path("api/", include("chat_service.urls")),
# # ]
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer
# from django.utils import timezone
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from .models import Message
# from .serializers import MessageSerializer


# @api_view(["POST"])
# def send_message(request):
#     serializer = MessageSerializer(data=request.data)

#     if serializer.is_valid():
#         message = serializer.save()

#         channel_layer = get_channel_layer()
#         async_to_sync(channel_layer.group_send)(
#             f"chat_{message.room_id}",
#             {
#                 "type": "broadcast_message",
#                 "data": MessageSerializer(message).data,
#             },
#         )

#         return Response(
#             MessageSerializer(message).data,
#             status=status.HTTP_201_CREATED,
#         )

#     return Response(
#         serializer.errors,
#         status=status.HTTP_400_BAD_REQUEST,
#     )


# @api_view(["DELETE"])
# def delete_message(request, room_id, message_id):
#     try:
#         msg = Message.objects.get(
#             message_id=message_id,
#             room_id=room_id,
#         )
#     except Message.DoesNotExist:
#         return Response(
#             {"error": "Message not found"},
#             status=status.HTTP_404_NOT_FOUND,
#         )

#     msg.visibility_state = "deleted"
#     msg.deleted_at = timezone.now()
#     msg.save()

#     return Response(
#         status=status.HTTP_204_NO_CONTENT,
#     )
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # SERVICES
    path("auth/", include("auth_service.urls")),
    path("", include("room_gateway.urls")),
    path("", include("dialogue_service.urls")),
    path("memory/", include("memory_service.urls")),
    path("moderation/", include("moderation_service.urls")),
    path("response/", include("response_engine.urls")),
    path("response-engine/", include("response_engine.urls")),
    path("api/", include("audio_broadcast.urls")),
    path("api/", include("chat_service.urls")),
]
