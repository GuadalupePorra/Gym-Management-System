from django.db import models
from django.utils import timezone
from socios.models import Socio  

class Ingreso_diario(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(default=timezone.now) 

    class Meta:
        verbose_name = "Ingreso diario"
        verbose_name_plural = "Ingresos registrados"

    def __str__(self):
        return f"Ingreso de {self.socio} en {self.fecha_ingreso}"

    def save(self, *args, **kwargs):
        # Llamamos a la función de decrementar el día antes de guardar el ingreso
        if self.socio.dias_restantes > 0:
            self.socio.decrementar_dia()
            self.socio.save()  # Guardamos la actualización de los días restantes
        else:
            raise ValueError("El socio necesita renovar su membresía para registrar un ingreso.")
        
        message = (
            f"Ingreso registrado exitosamente para el socio: {self.socio.nombre} {self.socio.apellido}\n"
            f"DNI: {self.socio.dni}\n"
            f"Días restantes: {self.socio.dias_restantes}\n"
            f"Fecha de pago: {self.socio.fecha_pago}"
        )

        # Llamamos a super().save() para guardar el objeto
        super().save(*args, **kwargs)

        # Retornamos el mensaje para usarlo en la vista del admin
        return message

