from django.db import models
from django.contrib.auth.models import AbstractUser


class UsuarioSistema(AbstractUser):
    """Modelo para usuarios del sistema médico"""
    
    ROL_CHOICES = [
        ("Administrador", "Administrador"),
        ("Medico", "Médico"),
        ("Enfermeria", "Enfermería"),
        ("Paciente", "Paciente"),
    ]
    
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50, unique=True, verbose_name="Nombre de Usuario")
    contrasena = models.CharField(max_length=128, verbose_name="Contraseña")
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, verbose_name="Rol")
    email = models.EmailField(verbose_name="Correo Electrónico")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    
    class Meta:
        db_table = "usuario_sistema"
        verbose_name = "Usuario del Sistema"
        verbose_name_plural = "Usuarios del Sistema"
    
    def __str__(self):
        return f"{self.nombre_usuario} ({self.rol})"
