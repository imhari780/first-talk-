from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            "message_id",
            "room_id",
            "sender_id",
            "content",
            "created_at",
            "deleted_at",
            "visibility_state",
        ]
