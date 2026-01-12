# Create your models here.
import uuid

from django.db import models


class VectorEntry(models.Model):
    vector_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    embedding = models.JSONField()
    source_type = models.CharField(max_length=32)
    source_id = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source_type} - {self.vector_id}"


class VectorMetadata(models.Model):
    vector = models.ForeignKey(VectorEntry, on_delete=models.CASCADE)
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=255)
