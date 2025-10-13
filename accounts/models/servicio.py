from django.db import models
from .paciente import Paciente
from .personal_salud import PersonalSalud


class Servicio(models.Model):
    """Modelo para servicios hospitalarios"""
    
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=200, verbose_name="Nombre del Servicio")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    
    class Meta:
        db_table = "servicio"
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
    
    def __str__(self):
        return self.nombre_servicio


class AtencionMedica(models.Model):
    """Modelo para atenciones médicas (relación entre paciente, profesional y servicio)"""
    
    id_atencion = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(
        Paciente, 
        on_delete=models.CASCADE, 
        verbose_name="Paciente"
    )
    id_profesional = models.ForeignKey(
        PersonalSalud, 
        on_delete=models.CASCADE, 
        verbose_name="Profesional de Salud"
    )
    id_servicio = models.ForeignKey(
        Servicio, 
        on_delete=models.CASCADE, 
        verbose_name="Servicio"
    )
    fecha_inicio = models.DateTimeField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de Fin")
    motivo_consulta = models.TextField(verbose_name="Motivo de Consulta")
    diagnostico = models.TextField(blank=True, null=True, verbose_name="Diagnóstico")
    
    class Meta:
        db_table = "atencion_medica"
        verbose_name = "Atención Médica"
        verbose_name_plural = "Atenciones Médicas"
    
    def __str__(self):
        return f"Atención {self.id_atencion} - {self.id_paciente.nombre_completo}"
