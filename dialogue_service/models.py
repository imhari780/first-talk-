from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class DialogueSession(models.Model):
    session_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    def is_active(self):
        return self.ended_at is None


class DialogueMessage(models.Model):
    SENDER_CHOICES = (
        ('user', 'User'),
        ('system', 'System'),
    )

    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey(DialogueSession, on_delete=models.CASCADE, related_name='messages')
    sender_type = models.CharField(max_length=16, choices=SENDER_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
