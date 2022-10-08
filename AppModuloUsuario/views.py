from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppModuloUsuario.forms import UserRegisterForm

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
        form=AuthenticationForm
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

# Create your views here.
