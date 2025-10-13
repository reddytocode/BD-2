from django.contrib import admin
from historial_medico.historia_clinica import HistoriaClinica


@admin.register(HistoriaClinica)
class HistoriaClinicaAdmin(admin.ModelAdmin):
    """Admin configuration for HistoriaClinica"""
    
    list_display = ("id_historia", "id_paciente", "id_profesional", "id_servicio", "fecha_ingreso", "fecha_alta")
    list_filter = ("fecha_ingreso", "id_servicio", "id_profesional__tipo")
    search_fields = ("id_paciente__nombres", "id_paciente__apellidos", "motivo_consulta", "diagnostico")
    ordering = ("-fecha_ingreso",)
    
    fieldsets = (
        ("Información de la Historia", {
            "fields": ("id_paciente", "id_profesional", "id_servicio")
        }),
        ("Fechas", {
            "fields": ("fecha_ingreso", "fecha_alta")
        }),
        ("Detalles Médicos", {
            "fields": ("motivo_consulta", "diagnostico", "observaciones")
        }),
    )
