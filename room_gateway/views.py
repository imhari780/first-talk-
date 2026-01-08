from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status

from .models import Room, RoomMember

# -------------------------------
# ROUTING
# -------------------------------
def get_room_route(room):
    return {
        'PUBLIC_CHAT': 'chat-service',
        'OPEN_CHAT': 'chat-service',
        'PRIVATE_DIALOGUE': 'chat-service',
        'AUDIO_BROADCAST': 'audio-service',
    }.get(room.room_type)


# -------------------------------
# EVENT EMITTER (mock)
# -------------------------------
def emit_event(event_type, room, user):
    print({
        "event": event_type,
        "room_id": room.id,
        "room_type": room.room_type,
        "user_id": user.id,
        "timestamp": timezone.now().isoformat()
    })


# -------------------------------
# CREATE ROOM
# -------------------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_room(request):
    room = Room.objects.create(
        name=request.data.get('name'),
        room_type=request.data.get('room_type')
    )

    emit_event("ROOM_CREATED", room, request.user)

    return Response({
        "room_id": room.id,
        "room_type": room.room_type
    }, status=201)


# -------------------------------
# JOIN ROOM  ✅ FIXED
# -------------------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_room(request, room_id):
    user = request.user
    room = get_object_or_404(Room, id=room_id)

    if not room.is_active:
        return Response(status=403)

    # already joined?
    if RoomMember.objects.filter(
        room=room, user=user, left_at__isnull=True
    ).exists():
        return Response(status=204)

    active_count = RoomMember.objects.filter(
        room=room, left_at__isnull=True
    ).count()

    if room.room_type == 'PRIVATE_DIALOGUE' and active_count >= 2:
        return Response(status=403)

    RoomMember.objects.create(
        room=room,
        user=user
    )

    emit_event("USER_JOINED", room, user)

    # CLIENT EXPECTS 204 NO CONTENT
    return Response(status=204)


# -------------------------------
# LEAVE ROOM
# -------------------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def leave_room(request, room_id):
    membership = RoomMember.objects.filter(
        room_id=room_id,
        user=request.user,
        left_at__isnull=True
    ).first()

    if membership:
        membership.left_at = timezone.now()
        membership.save()
        emit_event("USER_LEFT", membership.room, request.user)

    return Response(status=204)
