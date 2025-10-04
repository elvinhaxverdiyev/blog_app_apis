from django.db import models
from .user_models import UserProfile


class UsersImageModel(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(verbose_name="Profil Şəkli", blank=True, null=True, upload_to="/media")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.created_at}"
