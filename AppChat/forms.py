from django import forms

class MensajeForm(forms.Form):
    titulo=forms.CharField(max_length=40)
    mensaje=forms.CharField(max_length=2000)
