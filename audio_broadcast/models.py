from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.utils import timezone

class AudioSession(models.Model):
    session_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_id = models.UUIDField()
    host_id = models.UUIDField()
    scheduled_start = models.DateTimeField()
    scheduled_end = models.DateTimeField()
    is_live = models.BooleanField(default=False)
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    def start(self):
        self.is_live = True
        self.started_at = timezone.now()
        self.save()

    def stop(self):
        self.is_live = False
        self.ended_at = timezone.now()
        self.save()
