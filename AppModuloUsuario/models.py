from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    descripcion=models.CharField(max_length=200)
    paginaweb=models.URLField(max_length=200)
    imagen=models.ImageField(upload_to='imagenes', null=True, blank=True)