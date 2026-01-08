from django.db import models

# Create your models here.
import uuid
from django.db import models

class ModerationEvent(models.Model):
    TARGET_CHOICES = (
        ('message', 'Message'),
        ('user', 'User'),
    )

    ACTION_CHOICES = (
        ('mute', 'Mute'),
        ('soft_delete', 'Soft Delete'),
        ('temp_block', 'Temporary Block'),
    )

    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    moderator_id = models.UUIDField()
    target_type = models.CharField(max_length=16, choices=TARGET_CHOICES)
    target_id = models.UUIDField()
    action = models.CharField(max_length=32, choices=ACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "moderation_events"
