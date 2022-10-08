from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posteos, name='lista_posteos'),
    path('posteo/<int:pk>/', views.detalle_posteo, name='detalle_posteo'),
    path('posteo/nuevo/', views.posteo_nuevo, name='posteo_nuevo'),
]


