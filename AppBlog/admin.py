from django.contrib import admin
from .models import Posteo


"""
El decorador @admin.register() 
realiza la misma función que admin.site.register() que reemplaza 

https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#the-register-decorator

"""

@admin.register(Posteo)
class PosteoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicado')