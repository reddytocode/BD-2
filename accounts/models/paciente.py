from django.db import models
from .usuario_sistema import UsuarioSistema


class Paciente(models.Model):
    """Modelo para pacientes del sistema médico"""
    
    SEXO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro"),
    ]
    
    id_paciente = models.AutoField(primary_key=True)
    ci = models.CharField(max_length=20, unique=True, verbose_name="Cédula de Identidad")
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name="Sexo")
    direccion = models.TextField(verbose_name="Dirección")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    correo = models.EmailField(verbose_name="Correo Electrónico")
    id_usuario = models.OneToOneField(
        UsuarioSistema, 
        on_delete=models.CASCADE, 
        verbose_name="Usuario del Sistema"
    )
    
    class Meta:
        db_table = "paciente"
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
    
    def __str__(self):
        return f"{self.nombres} {self.apellidos} (CI: {self.ci})"
    
    @property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"
