from django.urls import path
from . import views
from .models import Posteo

urlpatterns = [
    path('', views.lista_posteos, name='lista_posteos'),
    path('posteo/<int:pk>/', views.detalle_posteo, name='detalle_posteo'),
    path('posteo/nuevo/', views.posteo_nuevo, name='posteo_nuevo'),
    path('posteo/<int:pk>/editar/', views.editar_posteo, name='editar_posteo'),
    path('borradores/', views.posteo_borradores, name='posteo_borradores'),
    path('posteo/<pk>/publicar/', views.publicar_posteo, name='publicar_posteo'),
    path('posteo/<pk>/eliminar/', views.eliminar_posteo, name='eliminar_posteo'),
    path('about/',views.about,name="about")
]


