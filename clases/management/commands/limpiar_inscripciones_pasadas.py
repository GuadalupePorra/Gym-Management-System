# clases/management/commands/limpiar_inscripciones_pasadas.py

from django.core.management.base import BaseCommand
from clases.models import Inscripcion
from datetime import date

class Command(BaseCommand):
    help = 'comando que elimina las inscripciones anteriores al día actual'

    def handle(self, *args, **kwargs):
        hoy = date.today()
        inscripciones_eliminadas, _ = Inscripcion.objects.filter(fecha_inscripcion__lt=hoy).delete()
        self.stdout.write(self.style.SUCCESS(f"Se eliminaron {inscripciones_eliminadas} inscripciones antiguas."))
#COMANDO: python manage.py limpiar_inscripciones_pasadas