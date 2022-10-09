from datetime import timezone
from django.db import models
from AppModuloUsuario.models import User
# Create your models here.

class Mensajes(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    remitente=models.CharField(max_length=60)
    destinatario=models.CharField(max_length=60)
    titulo=models.CharField(max_length=40)
    texto=models.CharField(max_length=2000)
