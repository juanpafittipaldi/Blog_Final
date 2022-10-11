from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField

class Posteo(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=500)
    contenido = RichTextField(blank=True, null=True)
    imagen_posteo = models.ImageField(blank=True, null=True, upload_to='media/')
    fecha_creado = models.DateTimeField(default=timezone.now)
    fecha_publicado = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicado = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo