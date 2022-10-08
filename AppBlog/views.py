from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PosteoForm
from .models import Posteo

def lista_posteos(request):
    posteos = Posteo.objects.filter(fecha_publicado__lte=timezone.now()).order_by('fecha_creado')
    return render(request, 'html/lista_posteos.html', {'posteos':posteos})


def detalle_posteo(request, pk):
    posteo = get_object_or_404(Posteo, pk=pk)
    return render(request, 'html/detalle_posteo.html', {'posteo': posteo})

def posteo_nuevo(request):
    if request.method == "POST":
        form = PosteoForm(request.POST)
        if form.is_valid():
            posteo = form.save(commit=False)
            posteo.autor = request.user
            posteo.save()
            return redirect('detalle_posteo', pk=posteo.pk)
    else:
        form = PosteoForm()
    return render(request, 'html/editar_posteo.html', {'form': form})

def editar_posteo(request, pk):
    posteo = get_object_or_404(Posteo, pk=pk)
    if request.method == "POST":
        form = PosteoForm(request.POST, instance=posteo)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('detalle_posteo', pk=posteo.pk)
    else:
        form = PosteoForm(instance=posteo)
    return render(request, 'html/editar_posteo.html', {'form': form})

def posteo_borradores(request):
    posteos = Posteo.objects.filter(fecha_publicado__isnull=True).order_by('-fecha_creado')
    return render(request, 'html/posteo_borradores.html', {'posteos': posteos})

def publicar_posteo(request, pk):
    posteo = get_object_or_404(Posteo, pk=pk)
    posteo.publicar()
    return redirect('detalle_posteo', pk=pk)

def eliminar_posteo(request, pk):
    posteo = get_object_or_404(Posteo, pk=pk)
    posteo.delete()
    return redirect('lista_posteos')
    