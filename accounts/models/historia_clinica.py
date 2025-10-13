from django.db import models
from .paciente import Paciente
from .personal_salud import PersonalSalud
from .servicio import Servicio


class HistoriaClinica(models.Model):
    """Modelo para historias clínicas"""
    
    id_historia = models.AutoField(primary_key=True)
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
    fecha_ingreso = models.DateTimeField(verbose_name="Fecha de Ingreso")
    fecha_alta = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de Alta")
    motivo_consulta = models.TextField(verbose_name="Motivo de Consulta")
    diagnostico = models.TextField(blank=True, null=True, verbose_name="Diagnóstico")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")
    
    class Meta:
        db_table = "historia_clinica"
        verbose_name = "Historia Clínica"
        verbose_name_plural = "Historias Clínicas"
    
    def __str__(self):
        return f"Historia {self.id_historia} - {self.id_paciente.nombre_completo}"
