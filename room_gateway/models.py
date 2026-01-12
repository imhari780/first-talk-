from django.conf import settings
from django.db import models


class Room(models.Model):
    ROOM_TYPES = [
        ("PUBLIC_CHAT", "Public Chat"),
        ("AUDIO_BROADCAST", "Audio Broadcast"),
        ("PRIVATE_DIALOGUE", "Private Dialogue"),
        ("OPEN_CHAT", "Open Chat"),
    ]

    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RoomMember(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    left_at = models.DateTimeField(null=True, blank=True)
