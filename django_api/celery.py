# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Establecer el módulo de configuración de Django para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('django_api')

# Cargar la configuración de Celery desde el archivo de configuración de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-descubrir tareas en cada app de Django
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
