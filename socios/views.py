from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Socio
from clases.models import Inscripcion, Clase, Horario_Clases

class PerfilSocio(APIView):
    def post(self, request):
        dni = request.data.get('dni')
        if not dni:
            return Response({"error": "DNI no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            socio = Socio.objects.get(dni=dni)

            if socio.dias_restantes == 0 and socio.fecha_pago <= date.today():
                return Response(
                    {"error": "Tu membresía ha vencido. Por favor, dirigite al gimnasio para renovarla."},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            inscripciones = Inscripcion.objects.filter(socio=socio)

            horarios_inscritos = [
                {
                    "inscripcion_id": insc.pk,
                    "horario_id": insc.horario_clase.pk,
                    "clase_id": insc.horario_clase.clase.pk,
                    "nombre_clase": insc.horario_clase.clase.nombre_clase,
                    "instructor": insc.horario_clase.clase.instructor,
                    "dia": insc.horario_clase.dia,
                    "hora": insc.horario_clase.horario.strftime("%H:%M:%S"),
                    "fecha_inscripcion": insc.fecha_inscripcion.strftime("%Y-%m-%d"),
                }
                for insc in inscripciones
            ]

            horarios_inscritos_ids = [insc.horario_clase.id for insc in inscripciones]

            # Todos los horarios que no están inscritos por el socio
            horarios_disponibles_qs = Horario_Clases.objects.exclude(id__in=horarios_inscritos_ids)

            horarios_disponibles = [
                {
                    "horario_id": h.pk,
                    "clase_id": h.clase.pk,
                    "nombre_clase": h.clase.nombre_clase,
                    "instructor": h.clase.instructor,
                    "dia": h.dia,
                    "hora": h.horario.strftime("%H:%M:%S"),
                    "capacidad_maxima": h.clase.capacidad_maxima,
                    # Si quieres, podés agregar cantidad inscriptos:
                    "cantidad_inscriptos": Inscripcion.objects.filter(horario_clase=h).count()
                }
                for h in horarios_disponibles_qs
            ]

            return Response({
                "socio": f"{socio.nombre} {socio.apellido}",
                "dni": socio.dni,
                "dias_restantes": socio.dias_restantes,
                "proxima_fecha_pago": socio.fecha_pago,
                "horarios_inscritos": horarios_inscritos,
                "horarios_disponibles": horarios_disponibles,
            }, status=status.HTTP_200_OK)

        except Socio.DoesNotExist:
            return Response({"error": "Socio no encontrado"}, status=status.HTTP_404_NOT_FOUND)
