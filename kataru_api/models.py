from django.db import models
from django.utils import timezone

# Create your models here.

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(default=timezone.now, editable=True)

    class Meta:
        abstract = True


