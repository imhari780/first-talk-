from django.db import models

# Create your models here.
import uuid
from django.db import models

class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_id = models.UUIDField()
    sender_id = models.UUIDField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    visibility_state = models.CharField(max_length=16, default="visible")

    class Meta:
        ordering = ["created_at"]
