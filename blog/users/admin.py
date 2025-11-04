from django.contrib import admin
from .models.user_image_model import UsersImageModel


@admin.register(UsersImageModel)
class UsersImageAdmin(admin.ModelAdmin):
    list_display = ("user", "image", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username", "user__name")
    ordering = ("-created_at",)
