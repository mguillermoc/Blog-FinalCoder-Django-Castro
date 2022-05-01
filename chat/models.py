from django.conf import settings
from django.db import models
from datetime import datetime

# Create your models here.
class sala(models.Model):
    nombre=models.CharField(max_length=60)

class mensaje(models.Model):
    value=models.CharField(max_length=1000)
    date=models.DateTimeField(default=datetime.now, blank=True)
    usuario=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    sala=models.CharField(max_length=1000)