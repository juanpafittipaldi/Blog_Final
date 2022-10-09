from django.urls import path
from AppModuloUsuario.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name="login"),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(template_name="AppModuloUsuario/logout.html"), name="Logout"),
    path("editarperfil/",editarperfil,name="editarperfil"),
    path("cambiopassword/",cambiopassword,name="cambiopassword"),
    path("datosusuario/",datosusuario,name="datosusuario"),
    path("perfil/<username>",perfil,name="perfil")

]