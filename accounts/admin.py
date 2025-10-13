from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioSistema, HistoriaClinica, Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ("id_paciente", "ci", "nombres", "apellidos", "fecha_nacimiento", "sexo", "telefono")
    list_filter = ("sexo", "fecha_nacimiento")
    search_fields = ("ci", "nombres", "apellidos", "telefono", "correo")
    ordering = ("apellidos", "nombres")



@admin.register(HistoriaClinica)
class HistoriaClinicaAdmin(admin.ModelAdmin):
    list_display = ("id_historia", "id_paciente", "id_profesional", "id_servicio", "fecha_ingreso", "fecha_alta")
    list_filter = ("fecha_ingreso", "id_servicio", "id_profesional__tipo")
    search_fields = ("id_paciente__nombres", "id_paciente__apellidos", "motivo_consulta", "diagnostico")
    ordering = ("-fecha_ingreso",)


# correcto1
@admin.register(UsuarioSistema)
class UsuarioSistemaAdmin(UserAdmin):
    """Admin configuration for UsuarioSistema"""
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