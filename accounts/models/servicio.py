from django.db import models
from .paciente import Paciente
from .personal_salud import PersonalSalud


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=200, verbose_name="Nombre del Servicio")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    personal_de_salud = models.ForeignKey(
        PersonalSalud,
        on_delete=models.CASCADE,
        verbose_name="Personal de Salud"
    )
    
    class Meta:
        db_table = "servicio"
        verbose_name = "Atención Médica"
        verbose_name_plural = "Atenciones Médicas"
    
    def __str__(self):
        return self.nombre_servicio

# expediente clinico (archivo principal del paciente) (tambien hay de internación)
# Motivos de consulta: cada vez que viene, se añade al expediente clinico
# . historia clinicca - primera vez - laboratorio - gabinete - referente a todo lo que ha pasado en su vida:
# Antecedentes: al nacer, al crecer, al adulto, al envejecer.
# Cuando vas a consulta: por que viene a consulta externa.


# gabinete: tomografias, ecografias, etc.
# laboratorio: examen de sangre, orina, etc.

# segunda consulta: abres su expediente con su historial clinico
# Historia a nivel cornologica, cuando vino. Especialidad: neumologia, cardiologia. 
# Rol de las enfermeras: 
# Hoja de ingreso: una sola, datos del paciente: Presion, signos vitales, etc. Siempre que visita se debe llenar esos datos.
# Hoja de Egreso: una sola vez 
# sistema ordenar 

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
