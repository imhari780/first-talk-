import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('participant', 'Participant'),
        ('moderator', 'Moderator'),
    )

    # UUID as public identity
    user_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    role = models.CharField(
        max_length=32,
        choices=ROLE_CHOICES,
        default='participant'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
