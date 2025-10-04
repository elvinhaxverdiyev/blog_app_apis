from django.db import models
from .user_models import CustomUser


class UsersImageModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(verbose_name="Profil Şəkli", blank=True, null=True, upload_to="profil_images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.created_at}"
