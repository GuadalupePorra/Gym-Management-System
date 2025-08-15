from django.contrib import admin
from .models import Membresia

class MembresiaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'precio', 'duracion')
    search_fields = ('tipo',)
    list_filter = ('duracion',)


admin.site.register(Membresia, MembresiaAdmin)
