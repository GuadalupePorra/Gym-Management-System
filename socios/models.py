from django.db import models
from django.utils import timezone
from datetime import timedelta
from membresias.models import Membresia

class Socio(models.Model):
    dni = models.CharField(max_length=8, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    id_membresia = models.ForeignKey(Membresia, on_delete=models.SET_NULL, null=True)
    fecha_pago = models.DateField()  # Fecha del último pago
    dias_restantes = models.IntegerField(default=0)  # Días de membresía restantes

    class Meta:
        verbose_name = "Socio"
        verbose_name_plural = "Socios registrados"
        permissions = [
            ("view", "Puede ver socios"),
            ("add","Agregar socio"),
            ("change", "Editar socio"),
            ("delete", "Eliminar socio"),
        ]

    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"
    

    def decrementar_dia(self):
        """Restar un día a la membresía del socio"""
        if self.dias_restantes > 0:
            self.dias_restantes -= 1
        else:
            # Notificar que debe renovar membresía
            raise ValueError("No quedan días en la membresía, es necesario renovar.")
        
    def es_dia_pago(self):
        # Verificar si es día de pago
        return self.dias_restantes <= 0

    def actualizar_fecha_pago(self):
        """Calcula la nueva fecha de pago sumando la duración de la membresía a la fecha de pago actual."""
        if self.id_membresia:
            self.fecha_pago = timezone.now() + timedelta(days=self.id_membresia.duracion)
            self.dias_restantes = self.id_membresia.duracion
            self.save()
        else:
            raise ValueError("El socio no tiene una membresía asignada.")
        
    def save(self, *args, **kwargs):
        """Sobreescribir el método save para que se actualicen automáticamente los días restantes al asignar una membresía"""
         # Solo inicializar dias_restantes cuando se crea el socio
        if self.id_membresia and self._state.adding and self.dias_restantes == 0:
            self.dias_restantes = self.id_membresia.duracion

        super().save(*args, **kwargs)