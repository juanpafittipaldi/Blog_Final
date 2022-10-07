from django.shortcuts import render
from django.utils import timezone
from .models import Posteo



def lista_posteos(request):
    posteos = Posteo.objects.filter(fecha_publicado__lte=timezone.now()).order_by('fecha_creado')
    return render(request, 'html/lista_posteos.html', {'posteos':posteos})

