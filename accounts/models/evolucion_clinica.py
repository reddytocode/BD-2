from django.db import models
from .historia_clinica import HistoriaClinica
from .personal_salud import PersonalSalud


class EvolucionClinica(models.Model):
    """Modelo para evoluciones clínicas"""
    
    id_evolucion = models.AutoField(primary_key=True)
    id_episodio = models.ForeignKey(
        HistoriaClinica, 
        on_delete=models.CASCADE, 
        verbose_name="Episodio Clínico"
    )
    fecha_registro = models.DateTimeField(verbose_name="Fecha de Registro")
    descripcion = models.TextField(verbose_name="Descripción")
    id_profesional = models.ForeignKey(
        PersonalSalud, 
        on_delete=models.CASCADE, 
        verbose_name="Profesional de Salud"
    )
    
    class Meta:
        db_table = "evolucion_clinica"
        verbose_name = "Evolución Clínica"
        verbose_name_plural = "Evoluciones Clínicas"
        ordering = ["-fecha_registro"]
    
    def __str__(self):
        return f"Evolución {self.id_evolucion} - {self.fecha_registro.strftime('%d/%m/%Y %H:%M')}"
