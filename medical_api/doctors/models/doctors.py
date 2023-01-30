"""User model."""
from datetime import timedelta

# Django
from django.db import models

# Utilities
from utils.models import BaseModel


class Doctor(BaseModel):
    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    biography = models.TextField(max_length=500, blank=True)

    availability = models.DurationField(timedelta(hours=0))

    major = models.ForeignKey('doctors.Major', on_delete=models.CASCADE)

    center = models.ForeignKey('doctors.Center', on_delete=models.CASCADE)

    def __str__(self):
        """Return user's str representation."""
        return str(self.last_name)
