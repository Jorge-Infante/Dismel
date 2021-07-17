# Importación librerias django
from datetime import date
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# Importación librerias django rest framework
from rest_framework.generics import (
    CreateAPIView,ListAPIView, RetrieveUpdateAPIView
)
# Importación modelo tarea
from . models import Task

# Importación serializador para tareas
from . serializers import TaskSerializer

class TaskCreateApiView(CreateAPIView):
    """Vista para crear objeto task (tarea) """ 

    serializer_class = TaskSerializer

class TaskIncompleteApiView(LoginRequiredMixin, ListAPIView):
    """Vista para listar tareas incompletas (no terminadas)"""

    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.tasks_imcomplete()

class TaskCompleteApiView(LoginRequiredMixin, ListAPIView):
    """Vista para tareas completadas"""

    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.tasks_complete()

class TaskUpdateView(RetrieveUpdateAPIView):
    """Vista para actualizar objeto task (tarea)"""
    
    serializer_class = TaskSerializer
    queryset= Task.objects.all()