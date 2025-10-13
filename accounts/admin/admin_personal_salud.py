from django.contrib import admin
from historial_medico.personal_salud import PersonalSalud


@admin.register(PersonalSalud)
class PersonalSaludAdmin(admin.ModelAdmin):
    """Admin configuration for PersonalSalud"""
    
    list_display = ("id_profesional", "nombres", "apellidos", "especialidad", "matricula", "tipo")
    list_filter = ("tipo", "especialidad")
    search_fields = ("nombres", "apellidos", "especialidad", "matricula")
    ordering = ("apellidos", "nombres")
    
    fieldsets = (
        ("Información Personal", {
            "fields": ("nombres", "apellidos")
        }),
        ("Información Profesional", {
            "fields": ("especialidad", "matricula", "tipo")
        }),
        ("Sistema", {
            "fields": ("id_usuario",)
        }),
    )
