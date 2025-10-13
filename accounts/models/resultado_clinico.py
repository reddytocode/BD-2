from django.db import models
from .orden_medica import OrdenMedica


class ResultadoClinico(models.Model):
    """Modelo para resultados clínicos"""
    
    id_resultado = models.AutoField(primary_key=True)
    id_orden = models.ForeignKey(
        OrdenMedica, 
        on_delete=models.CASCADE, 
        verbose_name="Orden Médica"
    )
    fecha_resultado = models.DateTimeField(verbose_name="Fecha del Resultado")
    descripcion = models.TextField(verbose_name="Descripción")
    documento = models.FileField(
        upload_to="resultados_clinicos/", 
        blank=True, 
        null=True, 
        verbose_name="Documento"
    )
    
    class Meta:
        db_table = "resultado_clinico"
        verbose_name = "Resultado Clínico"
        verbose_name_plural = "Resultados Clínicos"
        ordering = ["-fecha_resultado"]
    
    def __str__(self):
        return f"Resultado {self.id_resultado} - {self.fecha_resultado.strftime('%d/%m/%Y')}"
