from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioSistema(AbstractUser):
    rol = models.CharField(max_length=50, choices=[('Admin', 'Admin'), ('Recepcionista', 'Recepcionista')])

    class Meta:
        verbose_name_plural = "Usuarios registrados"
        db_table = 'usuarios_sistema'  # Nombre específico de la tabla en la base de datos

    def save(self, *args, **kwargs):
        # Solo si la contraseña no está hasheada
        if self.password and not self.password.startswith('pbkdf2_'):
            self.set_password(self.password)

        if self.rol in ['Admin', 'Recepcionista']:
            self.is_staff = True
        else:
            self.is_staff = False

        super().save(*args, **kwargs)

