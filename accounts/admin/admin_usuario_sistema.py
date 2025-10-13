from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import UserAccount


@admin.register(UserAccount)
class UserAccountAdmin(UserAdmin):
    """Admin configuration for UserAccount"""
    
    list_display = ("username", "email", "role", "is_verified", "is_active", "created_at")
    list_filter = ("role", "is_verified", "is_active", "created_at")
    search_fields = ("username", "email", "first_name", "last_name", "phone")
    ordering = ("-created_at",)
    
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "phone", "birth_date", "address")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Sistema Médico", {"fields": ("role", "is_verified", "created_at", "updated_at")}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "email", "role"),
        }),
    )
    
    readonly_fields = ("created_at", "updated_at", "date_joined", "last_login")
