from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.CharField(
        max_length=255,
        default=uuid.uuid4,
        primary_key=True,
        unique=True,
    )

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }
