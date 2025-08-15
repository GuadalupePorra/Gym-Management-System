from django.urls import path
from django.http import HttpResponse
from .views import obtener_precio_membresia

def test_view(request):
    return HttpResponse("Vista de prueba funcionando")

urlpatterns = [
    path('test/', test_view),  # Ruta de prueba
    path('socio/<int:socio_id>/precio/', obtener_precio_membresia, name='obtener_precio'),
]
