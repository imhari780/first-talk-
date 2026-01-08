from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .models import Message

@api_view(["DELETE"])
def delete_message(request, room_id, message_id):
    msg = Message.objects.get(message_id=message_id, room_id=room_id)
    msg.visibility_state = "deleted"
    msg.deleted_at = timezone.now()
    msg.save()
    return Response(status=204)
