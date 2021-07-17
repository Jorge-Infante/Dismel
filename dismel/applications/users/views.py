# Imports django
from django.shortcuts import render

# Imports django rest framework
from rest_framework.generics import (
    CreateAPIView,
)

# Import modelo User (usuario)
from . models import User

# Serializados para usuario
from . serializers import UserSerializer

class UserCreateApiView(CreateAPIView):
    """Vista para crear objeto user (usuario)"""    
    serializer_class = UserSerializer