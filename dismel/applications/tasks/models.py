from django.db import models
from model_utils.models import TimeStampedModel
from . managers import TaskImcompleteManager


# Create your models here.
class Task(TimeStampedModel):
    """Modelo para registrar Task (tarea)"""
    name = models.CharField(
        max_length=50
    )
    description = models.CharField(
        max_length=200
    )
    start_date = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=False)
    end_date = models.DateField(blank=True,null=True)
    
    objects =TaskImcompleteManager()
    class Meta:
        verbose_name= 'Task'
        verbose_name_plural = 'Tasks'
    
    def __str__(self):
        return str(self.id)+ ' - '+ self.name + str(self.start_date)