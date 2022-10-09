from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from AppModuloUsuario.models import User

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):

    email = forms.EmailField()
    first_name =forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    descripcion=forms.CharField(max_length=200)
    paginaweb=forms.URLField(max_length=200)
    imagen=forms.ImageField(label="Imagen")
    password1=None
    password2=None

    class Meta:
        model = User
        fields = ["email","first_name","last_name","descripcion","paginaweb","imagen"]
        help_texts = {k:"" for k in fields}

class CambioPasswordForm(PasswordChangeForm):
    old_password= forms.CharField(label="Ingrese su contraseña actual", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="Ingrese su nueva Contraseña", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["old_password","new_password1", "new_password2"]
        help_texts = {k:"" for k in fields}
