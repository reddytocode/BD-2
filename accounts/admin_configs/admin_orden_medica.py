from django.contrib import admin
from historial_medico.orden_medica import OrdenMedica


@admin.register(OrdenMedica)
class OrdenMedicaAdmin(admin.ModelAdmin):
    """Admin configuration for OrdenMedica"""
    
    list_display = ("id_orden", "id_episodio", "tipo", "estado", "fecha_emision")
    list_filter = ("tipo", "estado", "fecha_emision")
    search_fields = ("descripcion", "id_episodio__id_paciente__nombres")
    ordering = ("-fecha_emision",)
    
    fieldsets = (
        ("Información de la Orden", {
            "fields": ("id_episodio", "tipo", "estado")
        }),
        ("Detalles", {
            "fields": ("descripcion", "fecha_emision")
        }),
    )
