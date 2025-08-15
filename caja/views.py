from django.http import JsonResponse
from socios.models import Socio

def obtener_precio_membresia(request, socio_id):
    print(f"Vista llamada con socio_id: {socio_id}")
    try:
        socio = Socio.objects.get(pk=socio_id)
        print(f"Vista llamada con socio_id: {socio_id}")
        precio = socio.id_membresia.precio if socio.id_membresia else None
        return JsonResponse({'precio': precio})
    except Socio.DoesNotExist:
        return JsonResponse({'error': 'Socio no encontrado'}, status=404)