from django.urls import path
from AppChat.views import *

urlpatterns = [
    path("listadousuarios/", listadousuarios, name="listadousuarios"),
    path("crearmensaje/<username>", crearmensaje, name="crearmensaje")

]