from django.conf import settings
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class sala(models.Model):
    nombre=models.CharField(max_length=60)
  
    def __str__(self):
        return f'{self.nombre}'

class mensaje(models.Model):
    value=models.CharField(max_length=1000)
    date=models.DateTimeField(default=datetime.now, blank=True)
    usuario=models.CharField(max_length=1000)
    sala=models.CharField(max_length=1000)
    
    def __str__(self):
        return f'{self.nombre} - {self.usuario} - {self.sala}' 