from django.db import models

# Create your models here.
# response/models.py
import uuid
from django.db import models


class SystemResponse(models.Model):
    """
    Abstract system-originated response.
    No rule traceability, no user identity linkage.
    """

    response_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    room_type = models.CharField(max_length=32)

    text = models.TextField(null=True, blank=True)

    audio_tokens = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "system_responses"

    def __str__(self):
        return f"SystemResponse({self.response_id})"

