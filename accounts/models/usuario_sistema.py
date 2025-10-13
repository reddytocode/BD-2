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
    
    # Usar username de AbstractUser como nombre_usuario
    # Usar password de AbstractUser como contrasena
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, verbose_name="Rol")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    
    class Meta:
        db_table = "usuario_sistema"
        verbose_name = "Usuario del Sistema"
        verbose_name_plural = "Usuarios del Sistema"
    
    def __str__(self):
        return f"{self.username} ({self.rol})"
    
    @property
    def nombre_usuario(self):
        """Propiedad para compatibilidad con el nombre anterior"""
        return self.username
    
    @property
    def contrasena(self):
        """Propiedad para compatibilidad con el nombre anterior"""
        return self.password
