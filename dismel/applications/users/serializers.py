from rest_framework import serializers
from django.contrib.auth.models import User
from . models import User

class UserSerializer(serializers.ModelSerializer):
    """Serializador para creacion de usuario, el campo password no se guarda como texto plano"""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'email',
            'nombres',
            'apellidos',
            'genero',
            'is_staff',
            'is_active',
        )

    def create(self, validated_data):
        """Validar dato password"""
        
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        """Capturar password"""

        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user    
        