from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "codice_amico", "email", "is_staff", "is_superuser")
    search_fields = ("username", "codice_amico", "email")
    ordering = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Informazioni personali", {"fields": ("email", "codice_amico")}),
        ("Permessi", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Date importanti", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "codice_amico", "password1", "password2"),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
