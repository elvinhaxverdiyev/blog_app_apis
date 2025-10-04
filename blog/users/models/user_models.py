from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(max_length=55, verbose_name="Ad")
    bio = models.TextField(max_length=2000, blank=True, null=True, verbose_name="Haqqında")

    def __str__(self):
        return self.username
