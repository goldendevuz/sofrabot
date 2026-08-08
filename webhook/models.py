from django.db import models
import uuid
from django.utils import timezone


class BaseModel(models.Model):
    """
    Abstract base model with UUID PK and timestamps.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created"]
        get_latest_by = "created"

    def __str__(self):
        for attr in ["name", "title", "full_name"]:
            if hasattr(self, attr):
                value = getattr(self, attr)
                if value:
                    return str(value)
        return str(self.id)

    @property
    def age_seconds(self):
        return (timezone.now() - self.created).total_seconds()


class BotUser(BaseModel):
    user_id = models.BigIntegerField(
        unique=True,
        db_index=True,
    )

    name = models.CharField(max_length=120)
    username = models.CharField(
        max_length=120,
        blank=True,
        null=True,
    )

    language = models.CharField(
        max_length=10,
        default="en",
        db_index=True,
    )

    class Meta:
        verbose_name = "Bot User"
        verbose_name_plural = "Bot Users"

    def __str__(self):
        return f"{self.name} ({self.username}) - ID: {self.user_id}"
