# Create your views here.
import uuid


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ModerationEvent


# --------------------------------------------------
# ROLE CHECK (STEP 3)
# --------------------------------------------------
def is_moderator(request):
    """
    Role is injected by API Gateway / Auth layer
    Do NOT validate JWT here
    """
    role = request.headers.get("X-User-Role")
    return role == "moderator"


# --------------------------------------------------
# MUTE USER
# --------------------------------------------------
@api_view(["POST"])
def mute_user(request):
    if not is_moderator(request):
        return Response(status=status.HTTP_403_FORBIDDEN)

    target_user_id = request.data.get("user_id")
    if not target_user_id:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    ModerationEvent.objects.create(
        moderator_id=request.user.id,
        target_type="user",
        target_id=uuid.UUID(target_user_id),
        action="mute",
    )

    # Silent operation – no UI feedback
    return Response(status=status.HTTP_204_NO_CONTENT)


# --------------------------------------------------
# SOFT DELETE MESSAGE
# --------------------------------------------------
@api_view(["POST"])
def soft_delete_message(request):
    if not is_moderator(request):
        return Response(status=status.HTTP_403_FORBIDDEN)

    message_id = request.data.get("message_id")
    if not message_id:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    ModerationEvent.objects.create(
        moderator_id=request.user.id,
        target_type="message",
        target_id=uuid.UUID(message_id),
        action="soft_delete",
    )

    # Chat Service will silently update visibility
    return Response(status=status.HTTP_204_NO_CONTENT)


# --------------------------------------------------
# TEMPORARY BLOCK USER
# --------------------------------------------------
@api_view(["POST"])
def temp_block_user(request):
    if not is_moderator(request):
        return Response(status=status.HTTP_403_FORBIDDEN)

    target_user_id = request.data.get("user_id")
    if not target_user_id:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    ModerationEvent.objects.create(
        moderator_id=request.user.id,
        target_type="user",
        target_id=uuid.UUID(target_user_id),
        action="temp_block",
    )

    return Response(status=status.HTTP_204_NO_CONTENT)
