# Import all models
from .usuario_sistema import UsuarioSistema
from .paciente import Paciente
from .personal_salud import PersonalSalud
from .servicio import Servicio, AtencionMedica
from .historia_clinica import HistoriaClinica
from .evolucion_clinica import EvolucionClinica
from .orden_medica import OrdenMedica
from .resultado_clinico import ResultadoClinico


__all__ = [
    "UsuarioSistema",
    "Paciente",
    "PersonalSalud",
    "Servicio",
    "AtencionMedica",
    "HistoriaClinica",
    "EvolucionClinica",
    "OrdenMedica",
    "ResultadoClinico",
]


from django.db import models

class Gabinete(models.Model):
    """Expediente de gabinete, aqui van las tomografias, ecografias, etc."""
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(verbose_name="Descripción")

TIPO_GABINETE_CHOICES = [
    ("tomografia", "Tomografía"),
    ("ecografia", "Ecografía"),
]

class RegistroGabinete(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100, choices=TIPO_GABINETE_CHOICES, verbose_name="Tipo")
    gabinete = models.ForeignKey(Gabinete, on_delete=models.CASCADE, verbose_name="Gabinete")
    fecha_registro = models.DateTimeField(verbose_name="Fecha de Registro")
    descripcion = models.TextField(verbose_name="Descripción")


TIPO_LABORATORIO_CHOICES = [
    ("sangre", "Sangre"),
    ("orina", "Orina"),
    ("heces", "Heces"),
]
class Laboratorio(models.Model):
    """Expediente de laboratorio"""
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(verbose_name="Descripción")

class RegistroLaboratorio(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100, choices=TIPO_LABORATORIO_CHOICES, verbose_name="Tipo")
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, verbose_name="Laboratorio")
    fecha_registro = models.DateTimeField(verbose_name="Fecha de Registro", auto_now_add=True)
    descripcion = models.TextField(verbose_name="Descripción")

class ExpedienteClinico(models.Model):
    id = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    id_historia = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE, verbose_name="Historia Clínica")
    id_gabinete = models.ForeignKey(Gabinete, on_delete=models.CASCADE, verbose_name="Gabinete")
    id_laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, verbose_name="Laboratorio")
    