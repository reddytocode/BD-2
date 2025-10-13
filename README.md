# Sistema de Historial Médico - UDABOL

Sistema de gestión de historiales médicos desarrollado con Django y SQLite, organizado con modelos individuales en archivos separados.

## Estructura del Proyecto

El proyecto utiliza una estructura modular con cada modelo en su propio archivo dentro de la app `historial_medico`:

### App Principal: `historial_medico`

**Modelos (uno por archivo):**
- `usuario_sistema.py` - Gestión de usuarios del sistema
- `paciente.py` - Información de pacientes
- `personal_salud.py` - Personal médico y administrativo
- `servicio.py` - Servicios hospitalarios y atenciones médicas
- `historia_clinica.py` - Episodios clínicos
- `evolucion_clinica.py` - Notas de evolución
- `orden_medica.py` - Órdenes de laboratorio, imagenología, etc.
- `resultado_clinico.py` - Resultados con archivos adjuntos

**Configuraciones de Admin (en carpeta `admins/`):**
- `admins/admin_usuario_sistema.py` - Admin para UsuarioSistema
- `admins/admin_paciente.py` - Admin para Paciente
- `admins/admin_personal_salud.py` - Admin para PersonalSalud
- `admins/admin_servicio.py` - Admin para Servicio y AtencionMedica
- `admins/admin_historia_clinica.py` - Admin para HistoriaClinica
- `admins/admin_evolucion_clinica.py` - Admin para EvolucionClinica
- `admins/admin_orden_medica.py` - Admin para OrdenMedica
- `admins/admin_resultado_clinico.py` - Admin para ResultadoClinico

## Modelos de Base de Datos

### UsuarioSistema (`usuario_sistema.py`)
- `id_usuario` (PK) - Identificador único
- `nombre_usuario` - Nombre de acceso al sistema
- `contrasena` - Contraseña cifrada
- `rol` - Rol del usuario (Administrador, Médico, Enfermería, Paciente)
- `email` - Correo electrónico
- `fecha_creacion` - Fecha de registro

### Paciente (`paciente.py`)
- `id_paciente` (PK) - Identificador único
- `ci` - Cédula de identidad
- `nombres` - Nombres del paciente
- `apellidos` - Apellidos del paciente
- `fecha_nacimiento` - Fecha de nacimiento
- `sexo` - Sexo (M/F/O)
- `direccion` - Dirección
- `telefono` - Teléfono
- `correo` - Correo electrónico
- `id_usuario` (FK) - Referencia a UsuarioSistema

### PersonalSalud (`personal_salud.py`)
- `id_profesional` (PK) - Identificador único
- `nombres` - Nombres del profesional
- `apellidos` - Apellidos del profesional
- `especialidad` - Especialidad médica
- `matricula` - Matrícula profesional
- `tipo` - Tipo (Doctor, Administrativo, Enfermera, Laboratorista)
- `id_usuario` (FK) - Referencia a UsuarioSistema

### Servicio (`servicio.py`)
- `id_servicio` (PK) - Identificador único
- `nombre_servicio` - Nombre del servicio
- `descripcion` - Descripción del servicio
- `activo` - Estado del servicio
- `fecha_creacion` - Fecha de creación

### AtencionMedica (`servicio.py`)
- `id_atencion` (PK) - Identificador único
- `id_paciente` (FK) - Referencia a Paciente
- `id_profesional` (FK) - Referencia a PersonalSalud
- `id_servicio` (FK) - Referencia a Servicio
- `fecha_inicio` - Fecha de inicio de atención
- `fecha_fin` - Fecha de fin de atención
- `motivo_consulta` - Motivo de la consulta
- `diagnostico` - Diagnóstico

### HistoriaClinica (`historia_clinica.py`)
- `id_historia` (PK) - Identificador único
- `id_paciente` (FK) - Referencia a Paciente
- `id_profesional` (FK) - Referencia a PersonalSalud
- `id_servicio` (FK) - Referencia a Servicio
- `fecha_ingreso` - Fecha de ingreso
- `fecha_alta` - Fecha de alta
- `motivo_consulta` - Motivo de consulta
- `diagnostico` - Diagnóstico principal
- `observaciones` - Observaciones médicas

### EvolucionClinica (`evolucion_clinica.py`)
- `id_evolucion` (PK) - Identificador único
- `id_episodio` (FK) - Referencia a HistoriaClinica
- `fecha_registro` - Fecha del registro
- `descripcion` - Descripción de la evolución
- `id_profesional` (FK) - Referencia a PersonalSalud

### OrdenMedica (`orden_medica.py`)
- `id_orden` (PK) - Identificador único
- `id_episodio` (FK) - Referencia a HistoriaClinica
- `tipo` - Tipo de orden (laboratorio, imagenología, interconsulta, etc.)
- `descripcion` - Descripción de la orden
- `estado` - Estado (pendiente, en proceso, completada, cancelada)
- `fecha_emision` - Fecha de emisión

### ResultadoClinico (`resultado_clinico.py`)
- `id_resultado` (PK) - Identificador único
- `id_orden` (FK) - Referencia a OrdenMedica
- `fecha_resultado` - Fecha del resultado
- `descripcion` - Descripción del resultado
- `documento` - Archivo adjunto (PDF, JPG, PNG)

## Instalación y Configuración

### Requisitos
- Python 3.11+
- uv (package manager)

### Instalación
```bash
# Clonar el repositorio
git clone <repository-url>
cd proy_historial

# Instalar dependencias
uv sync

# Ejecutar migraciones
uv run python manage.py migrate

# Crear superusuario
uv run python manage.py createsuperuser

# Ejecutar servidor de desarrollo
uv run python manage.py runserver
```

### Acceso al Admin
- URL: http://127.0.0.1:8000/admin/
- Usuario: admin
- Contraseña: (la que configuraste al crear el superusuario)

## Características

- ✅ **Modelos individuales** - Cada modelo en su propio archivo
- ✅ **Admin personalizado** - Configuración de admin para cada modelo
- ✅ **Modelo de usuario personalizado** con roles
- ✅ **Gestión completa de pacientes**
- ✅ **Gestión de personal de salud**
- ✅ **Sistema de servicios hospitalarios**
- ✅ **Historias clínicas detalladas**
- ✅ **Evoluciones médicas**
- ✅ **Órdenes médicas**
- ✅ **Resultados clínicos con archivos adjuntos**
- ✅ **Interfaz de administración Django**
- ✅ **Base de datos SQLite**
- ✅ **Migraciones automáticas**

## Tecnologías Utilizadas

- **Django 5.2.7** - Framework web
- **SQLite** - Base de datos
- **uv** - Gestor de paquetes Python
- **Python 3.11** - Lenguaje de programación

## Estructura de Archivos

```
proy_historial/
├── manage.py
├── pyproject.toml
├── db.sqlite3
├── proy_historial/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── admin.py
├── historial_medico/
│   ├── models.py (importa todos los modelos)
│   ├── admin.py (archivo de compatibilidad)
│   ├── usuario_sistema.py
│   ├── paciente.py
│   ├── personal_salud.py
│   ├── servicio.py
│   ├── historia_clinica.py
│   ├── evolucion_clinica.py
│   ├── orden_medica.py
│   └── resultado_clinico.py
└── admins/
    ├── admin.py (importa todas las configuraciones de admin)
    ├── admin_usuario_sistema.py
    ├── admin_paciente.py
    ├── admin_personal_salud.py
    ├── admin_servicio.py
    ├── admin_historia_clinica.py
    ├── admin_evolucion_clinica.py
    ├── admin_orden_medica.py
    └── admin_resultado_clinico.py
```

## Ventajas de esta Estructura

1. **Modularidad** - Cada modelo está en su propio archivo
2. **Mantenibilidad** - Fácil localizar y modificar modelos específicos
3. **Escalabilidad** - Fácil agregar nuevos modelos
4. **Organización** - Admin configurations separadas en carpeta `admins/`
5. **Separación de responsabilidades** - Modelos en `historial_medico/`, admins en `admins/`
6. **Claridad** - Estructura clara y fácil de entender

## Próximos Pasos

1. Implementar vistas y templates para la interfaz de usuario
2. Agregar autenticación y autorización por roles
3. Implementar APIs REST con Django REST Framework
4. Agregar validaciones de negocio
5. Implementar reportes y estadísticas
6. Agregar tests unitarios y de integración