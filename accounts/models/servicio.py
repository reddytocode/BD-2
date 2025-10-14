from django.db import models
from .paciente import Paciente
from .personal_salud import PersonalSalud

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
