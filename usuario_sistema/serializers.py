from rest_framework import serializers
from .models import UsuarioSistema

class UsuarioSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioSistema
        fields = ['id', 'username', 'email', 'password', 'rol']
        extra_kwargs = {
            'password': {'write_only': True}  # Ocultar el campo password en respuestas GET
        }

    def create(self, validated_data):
        usuario = UsuarioSistema(
            username=validated_data['username'],
            email=validated_data['email'],  # Agregar el campo email
            rol=validated_data['rol']
        )
        usuario.set_password(validated_data['password'])  # Encripta la contraseña
        usuario.save()
        return usuario
