from django.contrib import admin
from historial_medico.paciente import Paciente


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    """Admin configuration for Paciente"""
    
    list_display = ("id_paciente", "ci", "nombres", "apellidos", "fecha_nacimiento", "sexo", "telefono")
    list_filter = ("sexo", "fecha_nacimiento")
    search_fields = ("ci", "nombres", "apellidos", "telefono", "correo")
    ordering = ("apellidos", "nombres")
    
    fieldsets = (
        ("Información Personal", {
            "fields": ("ci", "nombres", "apellidos", "fecha_nacimiento", "sexo")
        }),
        ("Contacto", {
            "fields": ("direccion", "telefono", "correo")
        }),
        ("Sistema", {
            "fields": ("id_usuario",)
        }),
    )
