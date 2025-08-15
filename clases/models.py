from django.core.exceptions import ValidationError
from django.db import models
from socios.models import Socio
from datetime import date


DIAS_SEMANA = [
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miércoles', 'Miércoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
    ('Sábado', 'Sábado'),
    ('Domingo', 'Domingo')
]

class Clase(models.Model):
    nombre_clase = models.CharField(max_length=50)
    instructor = models.CharField(max_length=50)
    capacidad_maxima = models.IntegerField()#capacidad fija

    class Meta:
        verbose_name_plural = "Clases registradas"
    
    @property
    def capacidad_actual(self):
        # Cuenta todas las inscripciones de todos los horarios de esta clase
        return Inscripcion.objects.filter(horario_clase__clase=self).count()
    def __str__(self):
        return f"{self.nombre_clase} - Instructor: {self.instructor}"

    def save(self, *args, **kwargs):
        if self.capacidad_maxima < 1:
            raise ValidationError("La capacidad máxima debe ser al menos 1.")
        super().save(*args, **kwargs)

class Horario_Clases(models.Model):
    clase = models.ForeignKey(Clase, related_name='horarios', on_delete=models.CASCADE)
    dia = models.CharField(max_length=15, choices=DIAS_SEMANA)  # Días predefinidos para evitar errores
    horario = models.TimeField()  # Hora de la clase en ese día específico

    def __str__(self):
        return f"{self.clase.nombre_clase} - {self.dia} - {self.horario}"

    class Meta:
        verbose_name_plural = "Horarios registrados"
        unique_together = ('clase', 'dia', 'horario')  # Evita duplicados de mismo día y horario    

class Inscripcion(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    horario_clase = models.ForeignKey(Horario_Clases, on_delete=models.CASCADE, related_name="inscripciones")
    fecha_inscripcion = models.DateField()

    def __str__(self):
        return f"{self.socio} - {self.horario_clase}"