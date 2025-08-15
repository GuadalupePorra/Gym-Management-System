from django.utils.html import format_html
from django.urls import reverse
from django.contrib import admin
from django.utils import timezone
from django import forms
from .models import Socio,Membresia

# ✅ 1. Formulario personalizado para Socio
class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['dni', 'nombre', 'apellido', 'id_membresia']  # ocultamos fecha_pago
        labels = {
            'id_membresia': 'Membresía',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 🧼 Usar un Select plano sin widgets relacionados
        self.fields['id_membresia'].widget = forms.Select(
            choices=self.fields['id_membresia'].choices            
            )

# ✅ 2. Admin personalizado
class SocioAdmin(admin.ModelAdmin):
    form = SocioForm
    search_fields = ['dni', 'nombre','apellido']  # Permite filtrar por instructor en el panel de admin

    list_display = ('nombre', 'apellido', 'dni', 'fecha_pago', 'id_membresia', 'acciones')  # opcional
    actions = None  # Esto desactiva el select y el boton ir
    

    # ✅ Permitir ver los datos
    def has_view_permission(self, request, obj=None):
        return True
    def acciones(self, obj):
        editar_url = reverse('admin:socios_socio_change', args=[obj.pk])
        eliminar_url = reverse('admin:socios_socio_delete', args=[obj.pk])
        return format_html(
            f'<a class="button" href="{editar_url}">✏️ Editar socio</a> &nbsp; '
            f'<a class="button" href="{eliminar_url}" style="color:red;">🗑️ Eliminar socio</a>'
        )
    acciones.short_description = 'Editar o eliminar'
    acciones.allow_tags = True

    def save_model(self, request, obj, form, change):
        if not change:  # solo al crear
            obj.fecha_pago = timezone.now().date()  # Asignar fecha actual al crear
        super().save_model(request, obj, form, change)

# ✅ 3. Registrar el modelo con su Admin
admin.site.register(Socio, SocioAdmin)

