from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    CitaMedica,
    ExpedienteClinico,
    Gabinete,
    HistoriaClinica,
    Laboratorio,
    Paciente,
    PersonalSalud,
    RegistroGabinete,
    RegistroLaboratorio,
    UsuarioSistema,
)
from .models import HojaIngreso

@admin.register(HojaIngreso)
class HojaIngresoAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha_ingreso", "observaciones_ingreso")


@admin.register(CitaMedica)
class CitaMedicaAdmin(admin.ModelAdmin):
    list_display = ("id", "id_profesional", "fecha_cita", "nota", "historia_clinica")


@admin.register(Gabinete)
class GabineteAdmin(admin.ModelAdmin):
    list_display = ("id", "descripcion")


@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ("id", "descripcion")


@admin.register(RegistroGabinete)
class RegistroGabineteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tipo",
        "gabinete",
        "fecha_registro",
        "descripcion",
        "personal_salud",
    )


@admin.register(RegistroLaboratorio)
class RegistroLaboratorioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tipo",
        "laboratorio",
        "fecha_registro",
        "descripcion",
        "personal_salud",
    )


@admin.register(ExpedienteClinico)
class ExpedienteClinicoAdmin(admin.ModelAdmin):
    list_display = ("id", "id_historia", "id_paciente", "id_gabinete", "id_laboratorio")


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = (
        "id_paciente",
        "ci",
        "nombres",
        "apellidos",
        "fecha_nacimiento",
        "sexo",
        "telefono",
    )
    list_filter = ("sexo", "fecha_nacimiento")
    search_fields = ("ci", "nombres", "apellidos", "telefono", "correo")
    ordering = ("apellidos", "nombres")


@admin.register(PersonalSalud)
class PersonalSaludAdmin(admin.ModelAdmin):
    list_display = (
        "id_profesional",
        "nombres",
        "apellidos",
        "especialidad",
        "matricula",
        "tipo",
    )
    list_filter = ("tipo", "especialidad")
    search_fields = ("nombres", "apellidos", "matricula", "especialidad")
    ordering = ("apellidos", "nombres")

class CitaMedicaInline(admin.TabularInline):
    model = CitaMedica
    extra = 0
    fields = ("id_profesional", "fecha_cita", "nota", "fecha_creacion")
    readonly_fields = ("fecha_creacion",)
    ordering = ("-fecha_cita",)


@admin.register(HistoriaClinica)
class HistoriaClinicaAdmin(admin.ModelAdmin):
    inlines = [CitaMedicaInline]

# correcto1
@admin.register(UsuarioSistema)
class UsuarioSistemaAdmin(UserAdmin):
    """Admin configuration for UsuarioSistema"""

    list_display = ("username", "email", "rol", "is_active", "fecha_creacion")
    list_filter = ("rol", "is_active")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("-fecha_creacion",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Sistema Médico", {"fields": ("rol", "fecha_creacion")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "rol"),
            },
        ),
    )

    readonly_fields = ("fecha_creacion", "date_joined", "last_login")
