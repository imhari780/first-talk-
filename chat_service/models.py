import uuid
from django.db import models

class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_id = models.CharField(max_length=100)
    sender_id = models.CharField(max_length=100)
    content = models.TextField()

    visibility_state = models.CharField(max_length=16, default="visible")
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room_id} - {self.sender_id}"
