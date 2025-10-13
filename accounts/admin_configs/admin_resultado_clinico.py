from django.contrib import admin
from historial_medico.resultado_clinico import ResultadoClinico


@admin.register(ResultadoClinico)
class ResultadoClinicoAdmin(admin.ModelAdmin):
    """Admin configuration for ResultadoClinico"""
    
    list_display = ("id_resultado", "id_orden", "fecha_resultado", "documento")
    list_filter = ("fecha_resultado", "id_orden__tipo")
    search_fields = ("descripcion", "id_orden__id_episodio__id_paciente__nombres")
    ordering = ("-fecha_resultado",)
    
    fieldsets = (
        ("Información del Resultado", {
            "fields": ("id_orden", "fecha_resultado")
        }),
        ("Detalles", {
            "fields": ("descripcion", "documento")
        }),
    )
