from datetime import date
from django.db import models

class TaskImcompleteManager(models.Manager):
    """Manager para consultas en el modelo task"""

    def tasks_imcomplete (self):
        """Mostrar tareas no completadas"""

        return self.filter(
            state=False
        )
    def tasks_complete (self):
        """Mostrar tareas completadas"""
        return self.filter(
            state=True
        )    
    
