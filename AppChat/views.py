from django.shortcuts import render
from django.contrib.auth import get_user_model
from AppChat.forms import *
from django.contrib.auth.decorators import login_required
from AppChat.models import Mensajes
from AppModuloUsuario.models import User

# Create your views here.
@login_required
def listadousuarios(request):
    User = get_user_model()
    users = User.objects.all()
    usuariologueado=request.user
    return render(request,"AppChat/listadousuarios.html",{"usuarios":users, "usuariologueado":usuariologueado})

def Elegirdestinatario(request, usuario_destino):
    destinatario = usuario_destino

@login_required
def crearmensaje(request, username):
    if request.method=="POST":
        form=MensajeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            destinatario=username
            remitente=request.user.username
            titulo=info["titulo"]
            texto=info["mensaje"]
            Mensaje=Mensajes(remitente=remitente,destinatario=destinatario,titulo=titulo,texto=texto)
            Mensaje.save()
            return render(request,"AppChat/listadousuarios.html",{"mensaje":"creaste un mensaje"})
        else:
            formulario=MensajeForm()
            return render(request,"AppChat/crearmensaje.html",{"formulario":formulario,"mensaje":"vuelva a intentarlo"})
    else:
        mensajes_enviados=Mensajes.objects.filter(remitente=request.user.username)
        mensajes_recibidos=Mensajes.objects.filter(destinatario=request.user.username)
        user=username
        formulario=MensajeForm()
        return render(request, "AppChat/crearmensaje.html",{"formulario":formulario,"username":user,"mensajes_enviados":mensajes_enviados,"mensajes_recibidos":mensajes_recibidos})
