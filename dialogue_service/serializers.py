from rest_framework import serializers

from .models import DialogueSession


class DialogueSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DialogueSession
        fields = ["session_id", "started_at"]


class DialogueMessageInputSerializer(serializers.Serializer):
    content = serializers.CharField()
