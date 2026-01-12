from rest_framework import serializers

from .models import AudioSession


class AudioSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioSession
        fields = "__all__"
