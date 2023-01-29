# Django
from django.db import models

# Utilities
from utils.models import BaseModel


class Center(BaseModel):
    name = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        """Return center's str representation."""
        return str(self.name)
