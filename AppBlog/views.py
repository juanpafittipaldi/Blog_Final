from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Posteo
from .forms import PosteoForm


def lista_posteos(request):
    posteos = Posteo.objects.filter(fecha_publicado__lte=timezone.now()).order_by('fecha_creado')
    return render(request, 'html/lista_posteos.html', {'posteos':posteos})


def detalle_posteo(request, pk):
    posteo = get_object_or_404(Posteo, pk=pk)
    return render(request, 'html/detalle_posteo.html', {'posteo': posteo})

def posteo_nuevo(request):
    form = PosteoForm()
    return render(request, 'html/editar_posteo.html', {'form': form})