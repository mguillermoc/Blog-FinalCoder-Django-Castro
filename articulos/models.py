from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

# Create your models here.

class article(models.Model):
    id = models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=60)
    abstract=models.CharField(max_length=280)
    articulo=RichTextField()
    # caratula
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.titulo} - {self.autor} - {self.creado} '
