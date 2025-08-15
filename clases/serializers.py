from rest_framework import serializers
from .models import Clase, Horario_Clases, Inscripcion

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['id', 'dia', 'hora', 'clase']


class HorarioClasesSerializer(serializers.ModelSerializer):
    clase = ClaseSerializer(read_only=True)

    class Meta:
        model = Horario_Clases
        fields = ['id', 'dia', 'hora', 'clase']

class InscripcionSerializer(serializers.ModelSerializer):
    horario_clase = HorarioClasesSerializer(read_only=True)
    horario_clase_id = serializers.PrimaryKeyRelatedField(
        queryset=Horario_Clases.objects.all(),
        source='horario_clase',
        write_only=True
    )

    class Meta:
        model = Inscripcion
        fields = ['id', 'socio', 'horario_clase', 'horario_clase_id', 'fecha_inscripcion']