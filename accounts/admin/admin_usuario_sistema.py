from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import UsuarioSistema


@admin.register(UsuarioSistema)
class UsuarioSistemaAdmin(UserAdmin):
    list_display = ("username", "email", "rol", "is_active", "fecha_creacion")
    list_filter = ("rol", "is_active")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("-fecha_creacion",)
    
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Sistema Médico", {"fields": ("rol", "fecha_creacion")}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "email", "rol"),
        }),
    )
    
    readonly_fields = ("fecha_creacion", "date_joined", "last_login")
