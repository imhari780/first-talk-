# Create your views here.
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import AudioSession
from .serializers import AudioSessionSerializer


# -------------------------------
# HOST creates scheduled session
# -------------------------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_audio_session(request):
    data = request.data

    session = AudioSession.objects.create(
        room_id=data["room_id"],
        host_id=request.user.user_id,
        scheduled_start=data["scheduled_start"],
        scheduled_end=data["scheduled_end"],
    )

    return Response(
        AudioSessionSerializer(session).data, status=status.HTTP_201_CREATED
    )


# -------------------------------
# Scheduler starts live stream
# -------------------------------
@api_view(["POST"])
def start_audio_session(request, session_id):
    try:
        session = AudioSession.objects.get(session_id=session_id)
    except AudioSession.DoesNotExist:
        return Response(
            {"error": "Session not found"}, status=status.HTTP_404_NOT_FOUND
        )

    if session.is_live:
        return Response({"error": "Already live"}, status=status.HTTP_400_BAD_REQUEST)

    # ---- FIX STARTS HERE ----
    now = timezone.now()

    start = session.scheduled_start
    end = session.scheduled_end

    # make scheduled times timezone-aware (UTC)
    if timezone.is_naive(start):
        start = timezone.make_aware(start, timezone.utc)

    if timezone.is_naive(end):
        end = timezone.make_aware(end, timezone.utc)

    if not (start <= now <= end):
        return Response(
            {
                "error": "Outside scheduled window",
                "now": now,
                "scheduled_start": start,
                "scheduled_end": end,
            },
            status=status.HTTP_403_FORBIDDEN,
        )
    # ---- FIX ENDS HERE ----

    session.start()
    return Response({"status": "LIVE"}, status=status.HTTP_200_OK)


# -------------------------------
# Listener joins live stream
# -------------------------------
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def join_audio_session(request, session_id):
    try:
        AudioSession.objects.get(session_id=session_id, is_live=True)
    except AudioSession.DoesNotExist:
        return Response(
            {"error": "No active session"}, status=status.HTTP_404_NOT_FOUND
        )

    # Silent join – no DB entry
    return Response(status=status.HTTP_200_OK)


# -------------------------------
# Stop live stream
# -------------------------------
@api_view(["POST"])
def stop_audio_session(request, session_id):
    try:
        session = AudioSession.objects.get(session_id=session_id)
    except AudioSession.DoesNotExist:
        return Response(
            {"error": "Session not found"}, status=status.HTTP_404_NOT_FOUND
        )

    session.stop()
    return Response({"status": "ENDED"}, status=status.HTTP_200_OK)
