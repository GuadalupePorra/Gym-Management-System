from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Clase, Horario_Clases

# modelo Horario
class HorarioInline(admin.TabularInline):
    model = Horario_Clases
    extra = 1  # formulario adicional para agregar un horario
    fields = ['dia', 'horario']

# modelo Clase
@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ['nombre_clase', 'instructor', 'capacidad_maxima', 'eliminar_clase']
    search_fields = ['nombre_clase', 'instructor']  # Permite buscar clases por nombre o instructor
    list_filter = ['nombre_clase']  # Permite filtrar por instructor en el panel de admin
    inlines = [HorarioInline]  # Agrega horarios directamente en la clase
    fields = ['nombre_clase', 'instructor', 'capacidad_maxima']
    actions = None

    def eliminar_clase(self, obj):
        url = reverse('admin:clases_clase_delete', args=[obj.pk])
        return format_html('<a class="button" href="{}" style="color:red;">🗑️ Eliminar clase</a>', url)

    eliminar_clase.short_description = 'Eliminar'
    
# Registro de Horario si quieres verlo como modelo independiente en el admin (opcional)
@admin.register(Horario_Clases)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ['clase', 'dia', 'horario','eliminar_horario']
    list_filter = ['dia']  # Permite filtrar por día en el panel de admin
    search_fields = ['clase__nombre_clase', 'dia']
    actions = None

    def eliminar_horario(self, obj):
        url = reverse('admin:clases_horario_clases_delete', args=[obj.pk])
        return format_html('<a class="button" href="{}" style="color:red;">🗑️ Eliminar horario</a>', url)

    eliminar_horario.short_description = 'Eliminar'



    

