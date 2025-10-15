from this import d
from django.db import models

from .paciente import Paciente
from .personal_salud import PersonalSalud
from django.utils import timezone


class HojaIngreso(models.Model):
    id_hoja_ingreso = models.AutoField(primary_key=True)
    fecha_ingreso = models.DateTimeField(verbose_name="Fecha de Ingreso")
    observaciones_ingreso = models.TextField(verbose_name="Observaciones de Ingreso")
    peso = models.FloatField(verbose_name="Peso")
    talla = models.FloatField(verbose_name="Talla")
    presion_arterial = models.FloatField(verbose_name="Presión Arterial")
    frecuencia_cardiaca = models.FloatField(verbose_name="Frecuencia Cardiaca")
    frecuencia_respiratoria = models.FloatField(verbose_name="Frecuencia Respiratoria")
    temperatura = models.FloatField(verbose_name="Temperatura")
    saturacion_oxigeno = models.FloatField(verbose_name="Saturación de Oxígeno")


class HistoriaClinica(models.Model):
    id_historia = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(
        Paciente, on_delete=models.CASCADE, verbose_name="Paciente"
    )
    id_profesional = models.ForeignKey(
        PersonalSalud, on_delete=models.CASCADE, verbose_name="Profesional de Salud"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")
    fecha_ingreso = models.DateTimeField(verbose_name="Fecha de Ingreso")

    class Meta:
        db_table = "historia_clinica"
        verbose_name = "Historia Clínica"
        verbose_name_plural = "Historias Clínicas"

    def __str__(self):
        return f"Historia {self.id_historia} - {self.id_paciente.nombre_completo}"


class CitaMedica(models.Model):
    id = models.AutoField(primary_key=True)
    id_profesional = models.ForeignKey(
        PersonalSalud, on_delete=models.CASCADE, verbose_name="Profesional de Salud"
    )
    fecha_cita = models.DateTimeField(verbose_name="Fecha de Cita")
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación"
    )
    nota = models.TextField(verbose_name="Nota")
    historia_clinica = models.ForeignKey(
        HistoriaClinica, on_delete=models.CASCADE, verbose_name="Historia Clínica"
    )
    hoja_ingreso = models.ForeignKey(
        HojaIngreso, on_delete=models.CASCADE, verbose_name="Hoja de Ingreso", null=True, blank=True
    )

    class Meta:
        db_table = "cita_medica"
        verbose_name = "Cita Médica"
        verbose_name_plural = "Citas Médicas"
