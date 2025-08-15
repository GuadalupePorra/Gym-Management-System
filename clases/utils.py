from .models import Inscripcion

def capacidad_actual_para(clase, horario, fecha):
    """
    Retorna la cantidad de inscriptos en una clase + horario para una fecha específica.
    """
    return Inscripcion.objects.filter(
        clase=clase,
        horario_clase=horario,
        fecha=fecha
    ).count()
