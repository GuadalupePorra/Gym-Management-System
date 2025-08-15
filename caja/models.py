from django.db import models
from django.utils import timezone
from django.db.models import Sum
from socios.models import Socio  # Asumimos que el modelo Socio está en la app socios
from django.template.loader import render_to_string

from django.core.files.base import ContentFile

# Opciones para medio de pago
class MedioPago:
    EFECTIVO = 'EF'
    DEBITO = 'DB'
    TRANSFERENCIA = 'TR'

    CHOICES = [
        (EFECTIVO, 'Efectivo'),
        (DEBITO, 'Débito'),
        (TRANSFERENCIA, 'Transferencia'),
        
    ]

class Caja(models.Model):
    fecha = models.DateField(unique=True, default=timezone.now)

    def __str__(self):
        return f"Caja del {self.fecha}"

    @property
    def total_pagos(self):
        return self.pagos.aggregate(total=Sum('monto'))['total'] or 0


class Pago(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField(default=timezone.now)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    medio_pago = models.CharField(max_length=2, choices=MedioPago.CHOICES)
    ruta_recibo = models.FileField(upload_to='', null=True, blank=True)
    caja = models.ForeignKey(Caja, related_name='pagos', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Pagos registrados"

    def __str__(self):
        return f"Pago de {self.socio} - ${self.monto} - {self.fecha_pago.strftime('%d/%m/%Y')}"

    def save(self, *args, **kwargs):
        if not self.monto and self.socio and self.socio.id_membresia:
            self.monto = self.socio.id_membresia.precio

        # Asignar la caja del día
        fecha_caja = self.fecha_pago.date()
        caja, _ = Caja.objects.get_or_create(fecha=fecha_caja)
        self.caja = caja

        is_new = self.pk is None

        # 3. Guardar primero para tener el ID del pago
        super().save(*args, **kwargs)

        # 4. Actualizar la fecha de pago del socio
        self.socio.actualizar_fecha_pago()

        if is_new:
            # 🧾 Generar PDF y actualizar socio solo si es un nuevo pago
            from caja.utils import generar_pdf_pago
            pdf_bytes = generar_pdf_pago(
                self.socio,
                self.monto,
                self.medio_pago,
                self.fecha_pago
            )


            self.ruta_recibo.save(f"recibo_socio_{self.socio.dni}.pdf", ContentFile(pdf_bytes), save=False)

            self.socio.actualizar_fecha_pago()
            self.socio.save()

            super().save(update_fields=["ruta_recibo"])  # Guardar solo el PDF

