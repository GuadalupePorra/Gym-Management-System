from django.contrib import admin
from django.contrib import messages  # Importamos messages
from .models import Ingreso_diario

@admin.register(Ingreso_diario)
class Ingreso_diarioAdmin(admin.ModelAdmin):
    list_display = ('socio', 'fecha_ingreso')  # Mostramos el socio y la fecha del ingreso
    search_fields = ('socio__dni',)  # Podemos buscar por el DNI del socio

    def save_model(self, request, obj, form, change):
        # Guardar el ingreso y obtener el mensaje de éxito
        try:
            message = obj.save()  # Guardamos el ingreso y obtenemos el mensaje de éxito
            # Mostrar el mensaje en el panel de admin
            messages.success(request, message)
        except Exception as e:
            # En caso de error, mostramos el mensaje de error
            messages.error(request, f"Error: {str(e)}")

