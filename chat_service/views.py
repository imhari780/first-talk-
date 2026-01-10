# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.utils import timezone
# from .models import Message
# from rest_framework import status
# from .serializers import MessageSerializer

# @api_view(["DELETE"])
# def delete_message(request, room_id, message_id):
#     msg = Message.objects.get(message_id=message_id, room_id=room_id)
#     msg.visibility_state = "deleted"
#     msg.deleted_at = timezone.now()
#     msg.save()
#     return Response(status=204)
# @api_view(["POST"])
# def send_message(request):
#     serializer = MessageSerializer(data=request.data)

#     if serializer.is_valid():
#         message = serializer.save()
#         return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


from .models import Message
from .serializers import MessageSerializer


@api_view(["POST"])
def send_message(request):
    serializer = MessageSerializer(data=request.data)

    if serializer.is_valid():
        message = serializer.save()

        # 🔥 WebSocket Broadcast
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"chat_{message.room_id}",
            {
                "type": "broadcast_message",
                "data": MessageSerializer(message).data,
            }
        )

        return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_message(request, room_id, message_id):
    try:
        msg = Message.objects.get(message_id=message_id, room_id=room_id)
    except Message.DoesNotExist:
        return Response({"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND)

    msg.visibility_state = "deleted"
    msg.deleted_at = timezone.now()
    msg.save()

    return Response(status=status.HTTP_204_NO_CONTENT)
