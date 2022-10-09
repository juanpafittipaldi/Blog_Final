from django import forms
from .models import Posteo

class PosteoForm(forms.ModelForm):

    class Meta:
        model = Posteo
        fields = ('titulo', 'contenido', 'imagen_posteo')