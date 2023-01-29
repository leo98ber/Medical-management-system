# Django
from django.db import models

# Utilities
from utils.models import BaseModel


class Major(BaseModel):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        """Return major's str representation."""
        return str(self.name)
