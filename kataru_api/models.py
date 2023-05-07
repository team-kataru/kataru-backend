from django.db import models
from django.utils import timezone

# Create your models here.

"""Create Timestamp Class Template for All Models"""

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=True)

    class Meta:
        abstract = True

"""Genre Model"""

class Genre(TimestampedModel):
    level = models.CharField(max_length=30)
    category = models.CharField(max_length=30)

    class Meta:
        db_table = 'genre'

"""Prompt Model"""

class Prompt(TimestampedModel):
    prompt_text = models.TextField()
    genre = models.ForeignKey("Genre", on_delete=models.PROTECT)

    class Meta:
        db_table = 'prompt'

"""User Model"""

class User(TimestampedModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    class Meta:
        db_table = 'user_' #trailing underscore to avoid keyword conflict