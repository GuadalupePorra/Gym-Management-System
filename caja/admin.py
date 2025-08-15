from django.contrib import admin
from django import forms
from .models import Pago, Caja
from socios.models import Socio
from django.utils.html import format_html
from django.utils import timezone



class PagoForm(forms.ModelForm):
    monto_formateado = forms.CharField(label='Monto ($)', required=False, disabled=True)

    class Meta:
        model = Pago
        fields = ['socio', 'medio_pago']

    class Media:
        js = ('caja/js/pago_admin.js',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

         # ⛔️ Mostrar solo socios cuya membresía venció
        hoy = timezone.now().date()
        self.fields['socio'].queryset = Socio.objects.filter(fecha_pago__lte=hoy)


        self.fields['socio'].widget.can_add_related = False
        self.fields['socio'].widget.can_change_related = False
        self.fields['socio'].widget.can_view_related = False

        if self.instance.pk:
            socio = self.instance.socio
            if socio and socio.id_membresia:
                precio = socio.id_membresia.precio
                self.fields['monto_formateado'].initial = f"${precio:,.0f}".replace(",", ".")

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    form = PagoForm
    readonly_fields = ('fecha_pago',)
    fields = ('socio', 'medio_pago', 'monto_formateado', 'fecha_pago')
    actions = None
    list_display = ('socio', 'monto', 'medio_pago', 'fecha_pago', 'ver_recibo')  # 👈 AGREGAMOS ACA

    def has_add_permission(self, request):
        return True  

    def has_delete_permission(self, request, obj=None):
        return False 
    
    def has_change_permission(self, request, obj=None):
        return True if obj else False
    
    def ver_recibo(self, obj):
        if obj.ruta_recibo:
            return format_html('<a class="button" href="{}" target="_blank">📄 Ver recibo</a>', obj.ruta_recibo.url)
        return "—"
    ver_recibo.short_description = "Recibo"
    ver_recibo.allow_tags = True

    

