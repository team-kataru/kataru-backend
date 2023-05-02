from django.db import models
from django.utils import timezone

# Create your models here.

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(default=timezone.now, editable=True)

    class Meta:
        abstract = True

class Genre(TimestampedModel):
    level = models.CharField(max_length=30)
    category = models.CharField(max_length=30)

    class Meta:
        db_table = 'genre'

class Prompt(TimestampedModel):
    prompt_text = models.TextField()
    genre = models.ForeignKey("Genre", on_delete=models.PROTECT)

    class Meta:
        db_table = 'prompt'