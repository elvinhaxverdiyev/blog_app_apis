from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=55, verbose_name="Profil adi")
    bio = models.TextField(max_length=2000)

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profillər"

    def __str__(self):
        return self.user.username
