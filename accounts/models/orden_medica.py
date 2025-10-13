from django.db import models
from .historia_clinica import HistoriaClinica


class OrdenMedica(models.Model):
    """Modelo para órdenes médicas"""
    
    TIPO_CHOICES = [
        ("laboratorio", "Laboratorio"),
        ("imagenologia", "Imagenología"),
        ("interconsulta", "Interconsulta"),
        ("medicamento", "Medicamento"),
        ("procedimiento", "Procedimiento"),
    ]
    
    ESTADO_CHOICES = [
        ("pendiente", "Pendiente"),
        ("en_proceso", "En Proceso"),
        ("completada", "Completada"),
        ("cancelada", "Cancelada"),
    ]
    
    id_orden = models.AutoField(primary_key=True)
    id_episodio = models.ForeignKey(
        HistoriaClinica, 
        on_delete=models.CASCADE, 
        verbose_name="Episodio Clínico"
    )
    tipo = models.CharField(
        max_length=20, 
        choices=TIPO_CHOICES, 
        verbose_name="Tipo de Orden"
    )
    descripcion = models.TextField(verbose_name="Descripción")
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES, 
        default="pendiente",
        verbose_name="Estado"
    )
    fecha_emision = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Emisión")
    
    class Meta:
        db_table = "orden_medica"
        verbose_name = "Orden Médica"
        verbose_name_plural = "Órdenes Médicas"
        ordering = ["-fecha_emision"]
    
    def __str__(self):
        return f"Orden {self.id_orden} - {self.get_tipo_display()}"
