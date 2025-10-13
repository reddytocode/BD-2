from django.contrib import admin
from historial_medico.servicio import Servicio, AtencionMedica


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    """Admin configuration for Servicio"""
    
    list_display = ("id_servicio", "nombre_servicio", "activo", "fecha_creacion")
    list_filter = ("activo", "fecha_creacion")
    search_fields = ("nombre_servicio", "descripcion")
    ordering = ("nombre_servicio",)


@admin.register(AtencionMedica)
class AtencionMedicaAdmin(admin.ModelAdmin):
    """Admin configuration for AtencionMedica"""
    
    list_display = ("id_atencion", "id_paciente", "id_profesional", "id_servicio", "fecha_inicio", "fecha_fin")
    list_filter = ("fecha_inicio", "id_servicio", "id_profesional__tipo")
    search_fields = ("id_paciente__nombres", "id_paciente__apellidos", "id_profesional__nombres", "motivo_consulta")
    ordering = ("-fecha_inicio",)
    
    fieldsets = (
        ("Información de la Atención", {
            "fields": ("id_paciente", "id_profesional", "id_servicio")
        }),
        ("Fechas", {
            "fields": ("fecha_inicio", "fecha_fin")
        }),
        ("Detalles Médicos", {
            "fields": ("motivo_consulta", "diagnostico")
        }),
    )
