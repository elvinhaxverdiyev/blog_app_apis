from django.contrib.auth.models import AbstractUser
from django.db import models

from .user_manager import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=55, unique=True)
    name = models.CharField(max_length=55, blank=True, null=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "name"] 

    objects = CustomUserManager()

    def __str__(self):
        return self.email
