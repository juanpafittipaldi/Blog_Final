from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posteos, name='lista_posteos'),
]