from datetime import date, timedelta, timezone
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status

from clases.utils import capacidad_actual_para
from .models import  Clase , Inscripcion,Horario_Clases
from socios.models import Socio 
from .serializers import ClaseSerializer, InscripcionSerializer  
from datetime import date, timedelta  # ← AGREGALO

DIAS_SEMANA = {
    'Lunes': 0,
    'Martes': 1,
    'Miércoles': 2,
    'Jueves': 3,
    'Viernes': 4,
    'Sábado': 5,
    'Domingo': 6
}

def obtener_fecha_proxima_para_dia(nombre_dia):
    hoy = date.today()
    dia_target = DIAS_SEMANA[nombre_dia]
    delta_dias = dia_target - hoy.weekday()
    if delta_dias < 0:
        delta_dias += 7
    return hoy + timedelta(days=delta_dias)

class InscribirseClase(APIView):
     def post(self, request, formato=None):
        dni = request.data.get("dni")
        horario_id = request.data.get('horario_clase_id')

        if not dni or not horario_id:
            return Response({'error': 'Faltan datos obligatorios.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            horario = Horario_Clases.objects.get(id=horario_id)
        except Horario_Clases.DoesNotExist:
            return Response({'error': 'El horario indicado no existe.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            socio = Socio.objects.get(dni=dni)
        except Socio.DoesNotExist:
            return Response({'error': 'El socio no existe.'}, status=status.HTTP_404_NOT_FOUND)

        clase = horario.clase  # Se deduce la clase desde el horario

        # Calcular la próxima fecha de clase (puede ser más complejo si usás lógica por día de semana)
        fecha = obtener_fecha_proxima_para_dia(horario.dia)
        # Validar capacidad del horario
        cantidad_inscriptos = Inscripcion.objects.filter(horario_clase=horario, fecha_inscripcion=fecha).count()
        if cantidad_inscriptos >= clase.capacidad_maxima:
            return Response({'error': 'El horario ya está completo.'}, status=status.HTTP_400_BAD_REQUEST)

        # Validar si ya está inscripto en ese horario en esa fecha
        if Inscripcion.objects.filter(socio=socio, horario_clase=horario, fecha_inscripcion=fecha).exists():
            return Response({'error': 'Ya estás inscripto en esta clase para esta fecha.'}, status=status.HTTP_400_BAD_REQUEST)

        # Registrar la inscripción
        inscripcion = Inscripcion.objects.create(
            socio=socio,
            horario_clase=horario,
            fecha_inscripcion=fecha
        )

        return Response({'mensaje': 'Inscripción realizada correctamente.'}, status=status.HTTP_201_CREATED)

class DarseBajaClase(APIView):
    def post(self, request, formato=None):
        dni = request.data.get('dni')
        horario_id = request.data.get('horario_clase_id')

        if not dni or not horario_id:
            return Response({'error': 'Faltan datos obligatorios.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            socio = Socio.objects.get(dni=dni)
        except Socio.DoesNotExist:
            return Response({'error': 'El socio no existe.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            horario = Horario_Clases.objects.get(id=horario_id)
        except Horario_Clases.DoesNotExist:
            return Response({'error': 'El horario indicado no existe.'}, status=status.HTTP_404_NOT_FOUND)

        fecha = obtener_fecha_proxima_para_dia(horario.dia)

        try:
            inscripcion = Inscripcion.objects.get(socio=socio, horario_clase=horario, fecha_inscripcion=fecha)
            inscripcion.delete()
            return Response({'mensaje': 'Desinscripción realizada correctamente.'}, status=status.HTTP_200_OK)
        except Inscripcion.DoesNotExist:
            return Response({'error': 'No existe una inscripción para ese horario en la fecha actual.'}, status=status.HTTP_404_NOT_FOUND)