from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    token = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.username
