from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from AppModuloUsuario.forms import *

# Create your views here.

def login_request(request):
    if request.method== "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppModuloUsuario/logueado.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppModuloUsuario/login.html",{"formulario":form, "mensaje":"usuario o contaseña incorrectos 2"})
        else:
            return render(request, "AppModuloUsuario/login.html",{"formulario":form, "mensaje":"usuario o contaseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "AppModuloUsuario/login.html",{"formulario":form})

def register(request):
    if request.method == "POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            formlogin=AuthenticationForm()
            return render(request,"AppModuloUsuario/login.html",{"formulario":formlogin,"mensaje":"Usuario creado correctamente"})
        else:
            form=UserRegisterForm()
            return render(request,"AppModuloUsuario/register.html",{"formulario":form,"mensaje":"Error al registrarse, vuelva a intentarlo"})
    else:
        form=UserRegisterForm()
        return render(request, "AppModuloUsuario/register.html",{"formulario":form})


def editarperfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.descripcion=info["descripcion"]
            usuario.paginaweb=info["paginaweb"]
            usuario.imagen=info["imagen"]
            usuario.save()
            return render(request,"AppModuloUsuario/logueado.html",{"mensaje":"Perfil editado correctamente"})
        else:
            return render(request, "AppModuloUsuario/editarperfil.html",{"formulario":form,"usuario":usuario, "mensaje":"formulario invalido, vuelva a intentarlo"})
    else:
        form=UserEditForm(instance=usuario)
    return render(request, "AppModuloUsuario/editarperfil.html",{"formulario":form,"usuario":usuario})

def cambiopassword(request):
    usuario=request.user
    if request.method=="POST":
        form=CambioPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return render(request,"AppModuloUsuario/logueado.html",{"mensaje":"Contraseña cambiada correctamente"})
        else:
            return render(request, "AppModuloUsuario/cambiopassword.html",{"formulario":form,"usuario":usuario, "mensaje":"formulario invalido, vuelva a intentarlo"})
    else:
        form=CambioPasswordForm(user=request.user)
    return render(request, "AppModuloUsuario/cambiopassword.html",{"formulario":form,"usuario":usuario})

# Create your views here.
