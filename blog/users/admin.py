from django.contrib import admin
from .models.user_image_model import UsersImageModel


@admin.register(UsersImageModel)
class UsersImageAdmin(admin.ModelAdmin):
    list_display = ("user", "image", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username", "user__name")
    ordering = ("-created_at",)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.user_models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "username", "name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "date_joined")
    search_fields = ("email", "username", "name")
    ordering = ("-date_joined",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("username", "name", "bio")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "name", "password1", "password2", "is_staff", "is_active"),
        }),
    )
