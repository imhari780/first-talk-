from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import DialogueSession, DialogueMessage
from .serializers import DialogueSessionSerializer, DialogueMessageInputSerializer
from .services import generate_system_response


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def start_dialogue(request):
    # Enforce single active session
    if DialogueSession.objects.filter(user=request.user, ended_at__isnull=True).exists():
        return Response(
            {"error": "Active session already exists"},
            status=status.HTTP_409_CONFLICT
        )

    session = DialogueSession.objects.create(user=request.user)
    serializer = DialogueSessionSerializer(session)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request, session_id):
    serializer = DialogueMessageInputSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        session = DialogueSession.objects.get(
            session_id=session_id,
            user=request.user,
            ended_at__isnull=True
        )
    except DialogueSession.DoesNotExist:
        return Response(
            {"error": "Invalid or ended session"},
            status=status.HTTP_404_NOT_FOUND
        )

    # Store USER message
    DialogueMessage.objects.create(
        session=session,
        sender_type='user',
        content=serializer.validated_data['content']
    )

    # Generate SYSTEM response
    system_reply = generate_system_response(serializer.validated_data['content'])

    DialogueMessage.objects.create(
        session=session,
        sender_type='system',
        content=system_reply
    )

    # ❌ No history returned
    return Response(
        {"content": system_reply},
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def end_dialogue(request, session_id):
    try:
        session = DialogueSession.objects.get(
            session_id=session_id,
            user=request.user,
            ended_at__isnull=True
        )
    except DialogueSession.DoesNotExist:
        return Response(
            {"error": "Session not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    session.ended_at = timezone.now()
    session.save()

    return Response(status=status.HTTP_204_NO_CONTENT)
