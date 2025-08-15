from django.db import models
from django.core.exceptions import ValidationError

def validate_tipo(value):
    if not value.isalpha():
        raise ValidationError('Este campo debe solo debe contener letras.')
    
def validate_precio(value):
    if value < 0 :
        raise ValidationError('El precio debe ser un número positivo.')

def validate_duracion(value):
    if value < 0:
        raise ValidationError('La duración debe ser un número positivo.')
    
class Membresia(models.Model):
    tipo = models.CharField(max_length=20, validators=[validate_tipo]) 
    precio = models.FloatField(validators=[validate_precio])  
    duracion = models.IntegerField(validators=[validate_duracion])  # En días

    class Meta:
        verbose_name_plural = "Membresias registradas"
    def __str__(self):
        return f"{self.tipo} - ${self.precio}"
