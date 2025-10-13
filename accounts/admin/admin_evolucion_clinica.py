from django.contrib import admin
from historial_medico.evolucion_clinica import EvolucionClinica


@admin.register(EvolucionClinica)
class EvolucionClinicaAdmin(admin.ModelAdmin):
    """Admin configuration for EvolucionClinica"""
    
    list_display = ("id_evolucion", "id_episodio", "fecha_registro", "id_profesional")
    list_filter = ("fecha_registro", "id_profesional__tipo")
    search_fields = ("descripcion", "id_episodio__id_paciente__nombres", "id_profesional__nombres")
    ordering = ("-fecha_registro",)
    
    fieldsets = (
        ("Información de la Evolución", {
            "fields": ("id_episodio", "id_profesional")
        }),
        ("Detalles", {
            "fields": ("fecha_registro", "descripcion")
        }),
    )
