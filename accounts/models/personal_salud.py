from django.db import models
from .usuario_sistema import UsuarioSistema


class PersonalSalud(models.Model):
    """Modelo para personal de salud del sistema médico"""
    
    TIPO_CHOICES = [
        ("Doctor", "Doctor"),
        ("Administrativo", "Administrativo"),
        ("Enfermera", "Enfermera"),
        ("Laboratorista", "Laboratorista"),
    ]
    
    id_profesional = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    especialidad = models.CharField(max_length=100, verbose_name="Especialidad")
    matricula = models.CharField(max_length=50, unique=True, verbose_name="Matrícula")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, verbose_name="Tipo")
    id_usuario = models.OneToOneField(
        UsuarioSistema, 
        on_delete=models.CASCADE, 
        verbose_name="Usuario del Sistema"
    )
    
    class Meta:
        db_table = "personal_salud"
        verbose_name = "Personal de Salud"
        verbose_name_plural = "Personal de Salud"
    
    def __str__(self):
        return f"Dr. {self.nombres} {self.apellidos} - {self.especialidad}"
    
    @property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"
